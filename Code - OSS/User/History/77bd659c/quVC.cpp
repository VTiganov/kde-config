#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits>
#include <set>
#include <algorithm>
#include <chrono>


struct Node {
    double lon, lat; // 16 байт
    std::vector<std::pair<int, double>> neighbors; // (8 байт на указатель + 12 байт на каждую пару)
};


struct Graph {
    std::unordered_map<std::string, int> node_map; //  (24 байта на каждый элемент: строка + int)
    std::vector<Node> nodes; // (16 байт на узел + память для соседей)

    
    int find_or_create_node(double lat, double lon) {
        std::string key = std::to_string(lat) + "," + std::to_string(lon); // 40 байт
        if (node_map.find(key) == node_map.end()) {
            Node new_node = {lon, lat}; // 16 байт
            nodes.push_back(new_node); 
            node_map[key] = nodes.size() - 1; // 24 байта
        }
        return node_map[key];
    }

    
    void load_from_file(const std::string& filename) {
        std::ifstream file(filename); // 8 байт
        std::string line;

        while (std::getline(file, line)) { // ~~100 байт, строки длинные
            std::stringstream ss(line); 
            std::string from_node, to_nodes;

            std::getline(ss, from_node, ':'); //~40 байт
            std::getline(ss, to_nodes); 

            double from_lon, from_lat;
            sscanf(from_node.c_str(), "%lf,%lf", &from_lon, &from_lat); // Преобразование строки для дальнейшей работы с ней.
            int from = find_or_create_node(from_lat, from_lon);

            std::stringstream neighbors_stream(to_nodes);
            std::string neighbor_info;
            while (std::getline(neighbors_stream, neighbor_info, ';')) { 
                double to_lon, to_lat, weight;
                sscanf(neighbor_info.c_str(), "%lf,%lf,%lf", &to_lon, &to_lat, &weight);
                int to = find_or_create_node(to_lat, to_lon);
                nodes[from].neighbors.push_back({to, weight}); // 12 байт
            }
        }
    }

    
    int find_closest_node(double lat, double lon) {
        int closest = -1; // 4 байта
        double min_distance = std::numeric_limits<double>::max(); // 8 байт
        for (int i = 0; i < nodes.size(); ++i) { //  4 байта
            double distance = std::sqrt(std::pow(nodes[i].lat - lat, 2) + std::pow(nodes[i].lon - lon, 2)); 
            if (distance < min_distance) {
                closest = i; // 4 байта
                min_distance = distance; // 8 байт
            }
        }
        return closest;
    }
};


void print_path(const std::unordered_map<int, int>& came_from, int goal, const std::vector<Node>& nodes) {
    if (came_from.find(goal) != came_from.end()) {
        std::vector<int> path; //  4 байта на элемент
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


void bfs(const std::vector<Node>& nodes, int start, int goal) {
    auto start_time = std::chrono::high_resolution_clock::now();

    std::queue<int> q; //  4 байта на каждый элемент
    std::unordered_map<int, int> came_from; // 24 байта на каждый элемент
    q.push(start); // 4 байта на элемент
    came_from[start] = -1; // 24 байта

    while (!q.empty()) {
        int current = q.front(); // 4 байта
        q.pop();
        if (current == goal) break;
        for (const auto& neighbor : nodes[current].neighbors) { //  12 байт на пару
            int next = neighbor.first; // 4 байта
            if (came_from.find(next) == came_from.end()) {
                q.push(next); // 4 байта на элемент
                came_from[next] = current; // 24 байта
            }
        }
    }
}

void dfs(const std::vector<Node>& nodes, int start, int goal) {
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

}


void dijkstra(const std::vector<Node>& nodes, int start, int goal) {
    auto start_time = std::chrono::high_resolution_clock::now();

    std::unordered_map<int, double> distances; // 32 байта на каждый элемент int + double)
    std::unordered_map<int, int> came_from; // 24 байта на каждый элемент
    std::set<std::pair<double, int>> priority_queue; // 24 байта на каждый элемент

    distances[start] = 0.0; // 32 байта
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
}
