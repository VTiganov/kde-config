#ifndef GRAPH_ALGORITHMS_H
#define GRAPH_ALGORITHMS_H

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
    double lon, lat;
    std::vector<std::pair<int, double>> neighbors;
};

struct Graph {
    std::unordered_map<std::string, int> node_map;
    std::vector<Node> nodes;

    int find_or_create_node(double lat, double lon);
    void load_from_file(const std::string& filename);
    int find_closest_node(double lat, double lon);
};

void print_path(const std::unordered_map<int, int>& came_from, int goal, const std::vector<Node>& nodes);
void bfs(const std::vector<Node>& nodes, int start, int goal);
void dfs(const std::vector<Node>& nodes, int start, int goal);
void dijkstra(const std::vector<Node>& nodes, int start, int goal);

#endif
