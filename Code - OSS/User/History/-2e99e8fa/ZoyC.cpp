#include "graph_algorithms.h"

int Graph::find_or_create_node(double lat, double lon) {
    std::string key = std::to_string(lat) + "," + std::to_string(lon);
    if (node_map.find(key) == node_map.end()) {
        Node new_node = {lon, lat};
        nodes.push_back(new_node);
        node_map[key] = nodes.size() - 1;
    }
    return node_map[key];
}

void Graph::load_from_file(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string from_node, to_nodes;

        std::getline(ss, from_node, ':');
        std::getline(ss, to_nodes);

        double from_lon, from_lat;
        sscanf(from_node.c_str(), "%lf,%lf", &from_lon, &from_lat);
        int from = find_or_create_node(from_lat, from_lon);

        std::stringstream neighbors_stream(to_nodes);
        std::string neighbor_info;
        while (std::getline(neighbors_stream, neighbor_info, ';')) {
            double to_lon, to_lat, weight;
            sscanf(neighbor_info.c_str(), "%lf,%lf,%lf", &to_lon, &to_lat, &weight);
            int to = find_or_create_node(to_lat, to_lon);
            nodes[from].neighbors.push_back({to, weight});
        }
    }
}

int Graph::find_closest_node(double lat, double lon) {
    int closest = -1;
    double min_distance = std::numeric_limits<double>::max();
    for (int i = 0; i < nodes.size(); ++i) {
        double distance = std::sqrt(std::pow(nodes[i].lat - lat, 2) + std::pow(nodes[i].lon - lon, 2));
        if (distance < min_distance) {
            closest = i;
            min_distance = distance;
        }
    }
    return closest;
}

void print_path(const std::unordered_map<int, int>& came_from, int goal, const std::vector<Node>& nodes) {
    if (came_from.find(goal) != came_from.end()) {
        std::vector<int> path;
        for (int at = goal; at != -1; at = came_from.at(at)) {
            path.push_back(at);
        }
        std::reverse(path.begin(), path.end());
        for (int node : path) {
            std::cout << "(" << nodes[node].lat << ", " << nodes[node].lon << ") -> ";
        }
        std::cout << "end\n";
    } else {
        std::cout << "Path not found\n";
    }
}


void bfs(const std::vector<Node>& nodes, int start, int goal) {
    auto start_time = std::chrono::high_resolution_clock::now();

    std::queue<int> q;
    std::unordered_map<int, int> came_from;
    q.push(start);
    came_from[start] = -1;

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        if (current == goal) break;
        for (const auto& neighbor : nodes[current].neighbors) {
            int next = neighbor.first;
            if (came_from.find(next) == came_from.end()) {
                q.push(next);
                came_from[next] = current;
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "BFS Time: " << duration.count() << " ms\n";
    print_path(came_from, goal, nodes);
}

void dfs(const std::vector<Node>& nodes, int start, int goal) {
    auto start_time = std::chrono::high_resolution_clock::now();

    std::stack<int> s;
    std::unordered_map<int, int> came_from;
    s.push(start);
    came_from[start] = -1;

    while (!s.empty()) {
        int current = s.top();
        s.pop();
        if (current == goal) break;
        for (const auto& neighbor : nodes[current].neighbors) {
            int next = neighbor.first;
            if (came_from.find(next) == came_from.end()) {
                s.push(next);
                came_from[next] = current;
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "DFS Time: " << duration.count() << " ms\n";
    print_path(came_from, goal, nodes);
}

void dijkstra(const std::vector<Node>& nodes, int start, int goal) {
    auto start_time = std::chrono::high_resolution_clock::now();

    std::unordered_map<int, double> distances;
    std::unordered_map<int, int> came_from;
    std::set<std::pair<double, int>> priority_queue;

    distances[start] = 0.0;
    priority_queue.insert({0.0, start});

    while (!priority_queue.empty()) {
        int current = priority_queue.begin()->second;
        priority_queue.erase(priority_queue.begin());
        if (current == goal) break;

        for (const auto& neighbor : nodes[current].neighbors) {
            int next = neighbor.first;
            double weight = neighbor.second;
            double new_distance = distances[current] + weight;

            if (distances.find(next) == distances.end() || new_distance < distances[next]) {
                priority_queue.erase({distances[next], next});
                distances[next] = new_distance;
                came_from[next] = current;
                priority_queue.insert({new_distance, next});
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "Dijkstra Time: " << duration.count() << " ms\n";

    if (came_from.find(goal) != came_from.end()) {
        print_path(came_from, goal, nodes);
    } else {
        std::cout << "Path not found\n";
    }
}
