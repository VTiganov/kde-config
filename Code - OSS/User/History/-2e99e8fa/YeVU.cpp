#include "graph_algorithms.h"

int Graph::find_or_create_node(double lat, double lon) { // 8 байт каждая переменная типа double
    std::string key = std::to_string(lat) + "," + std::to_string(lon); // размер строки зависит от содержимого
    if (node_map.find(key) == node_map.end()) {
        Node new_node = {lon, lat}; // 16 байт (2 * 8 байт)
        nodes.push_back(new_node);
        node_map[key] = nodes.size() - 1; // 4 байта для int
    }
    return node_map[key]; // 4 байта для int
}

void Graph::load_from_file(const std::string& filename) { // размер строки зависит от содержимого
    std::ifstream file(filename); // 8 байт для указателя на файл
    std::string line; // размер строки зависит от содержимого

    while (std::getline(file, line)) {
        std::stringstream ss(line); // размер строки зависит от содержимого
        std::string from_node, to_nodes; // размер строки зависит от содержимого

        std::getline(ss, from_node, ':'); 
        std::getline(ss, to_nodes); // размер строки зависит от содержимого

        double from_lon, from_lat; // 8 байт каждая переменная типа double
        sscanf(from_node.c_str(), "%lf,%lf", &from_lon, &from_lat); // Преобразование строки для дальнейшей работы с ней
        int from = find_or_create_node(from_lat, from_lon); // 4 байта для int

        std::stringstream neighbors_stream(to_nodes); // размер строки зависит от содержимого
        std::string neighbor_info; // размер строки зависит от содержимого
        while (std::getline(neighbors_stream, neighbor_info, ';')) {
            double to_lon, to_lat, weight; // 8 байт каждая переменная типа double
            sscanf(neighbor_info.c_str(), "%lf,%lf,%lf", &to_lon, &to_lat, &weight); // Преобразование строки для дальнейшей работы с ней
            int to = find_or_create_node(to_lat, to_lon); // 4 байта для int
            nodes[from].neighbors.push_back({to, weight}); // 12 байт (4 байта для int + 8 байт для double)
        }
    }
}

int Graph::find_closest_node(double lat, double lon) { // 8 байт каждая переменная типа double
    int closest = -1; // 4 байта
    double min_distance = std::numeric_limits<double>::max(); // 8 байт
    for (int i = 0; i < nodes.size(); ++i) { // 4 байта для int
        double distance = std::sqrt(std::pow(nodes[i].lat - lat, 2) + std::pow(nodes[i].lon - lon, 2)); // 8 байт
        if (distance < min_distance) {
            closest = i; // 4 байта
            min_distance = distance; // 8 байт
        }
    }
    return closest; // 4 байта
}

void print_path(const std::unordered_map<int, int>& came_from, int goal, const std::vector<Node>& nodes) { // 4 байта для int
    if (came_from.find(goal) != came_from.end()) {
        std::vector<int> path; // 4 байта на элемент
        for (int at = goal; at != -1; at = came_from.at(at)) { // 4 байта на итерацию
            path.push_back(at); // 4 байта на элемент
        }
        std::reverse(path.begin(), path.end());
        for (int node : path) { // 4 байта
            std::cout << "(" << nodes[node].lat << ", " << nodes[node].lon << ") -> ";
        }
        std::cout << "end\n";
    } else {
        std::cout << "Path not found\n";
    }
}

void bfs(const std::vector<Node>& nodes, int start, int goal) { // 4 байта для int
    auto start_time = std::chrono::high_resolution_clock::now();

    std::queue<int> q; // 4 байта на каждый элемент
    std::unordered_map<int, int> came_from; // 24 байта на каждый элемент
    q.push(start); // 4 байта на элемент
    came_from[start] = -1; // 24 байта

    while (!q.empty()) {
        int current = q.front(); // 4 байта
        q.pop();
        if (current == goal) break;
        for (const auto& neighbor : nodes[current].neighbors) { // 12 байт на пару
            int next = neighbor.first; // 4 байта
            if (came_from.find(next) == came_from.end()) {
                q.push(next); // 4 байта на элемент
                came_from[next] = current; // 24 байта
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "BFS Time: " << duration.count() << " ms\n";
    print_path(came_from, goal, nodes);
}

void dfs(const std::vector<Node>& nodes, int start, int goal) { // 4 байта для int
    auto start_time = std::chrono::high_resolution_clock::now();

    std::stack<int> s; // 4 байта на каждый элемент
    std::unordered_map<int, int> came_from; // 24 байта на каждый элемент
    s.push(start); // 4 байта на элемент
    came_from[start] = -1; // 24 байта

    while (!s.empty()) {
        int current = s.top(); // 4 байта
        s.pop();
        if (current == goal) break;
        for (const auto& neighbor : nodes[current].neighbors) { // 12 байт на пару
            int next = neighbor.first; // 4 байта
            if (came_from.find(next) == came_from.end()) {
                s.push(next); // 4 байта на элемент
                came_from[next] = current; // 24 байта
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "DFS Time: " << duration.count() << " ms\n";
    print_path(came_from, goal, nodes);
}

void dijkstra(const std::vector<Node>& nodes, int start, int goal) { // 4 байта для int
    auto start_time = std::chrono::high_resolution_clock::now();

    std::unordered_map<int, double> distances; // 32 байта на каждый элемент (int + double)
    std::unordered_map<int, int> came_from; // 24 байта на каждый элемент
    std::set<std::pair<double, int>> priority_queue; // 24 байта на каждый элемент

    distances[start] = 0.0; // 32 байта
    came_from[start] = -1; // 24 байта
    priority_queue.insert({0.0, start}); // 24 байта на элемент

    while (!priority_queue.empty()) {
        int current = priority_queue.begin()->second; // 4 байта
        priority_queue.erase(priority_queue.begin());
        if (current == goal) break;

        for (const auto& neighbor : nodes[current].neighbors) { // 12 байт на пару
            int next = neighbor.first; // 4 байта
            double weight = neighbor.second; // 8 байт
            double new_distance = distances[current] + weight; // 8 байт

            if (distances.find(next) == distances.end() || new_distance < distances[next]) {
                priority_queue.erase({distances[next], next}); // 24 байта
                distances[next] = new_distance; // 32 байта
                came_from[next] = current; // 24 байта
                priority_queue.insert({new_distance, next}); // 24 байта
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
