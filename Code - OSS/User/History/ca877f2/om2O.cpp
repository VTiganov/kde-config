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
#include <cassert>

// Include the Graph and related functions from graph_algorithms.h
#include "graph_algorithms.h"

void test_graph_loading() {
    Graph graph;
    graph.load_from_file("test_graph.txt");

    // Check if the graph has loaded the correct number of nodes
    assert(graph.nodes.size() == 5);

    // Check if the nodes have the correct coordinates
    assert(graph.nodes[0].lat == 0.0 && graph.nodes[0].lon == 0.0);
    assert(graph.nodes[1].lat == 1.0 && graph.nodes[1].lon == 1.0);
    assert(graph.nodes[2].lat == 2.0 && graph.nodes[2].lon == 2.0);
    assert(graph.nodes[3].lat == 3.0 && graph.nodes[3].lon == 3.0);
    assert(graph.nodes[4].lat == 4.0 && graph.nodes[4].lon == 4.0);

    // Check if the neighbors are correctly loaded
    assert(graph.nodes[0].neighbors.size() == 2);
    assert(graph.nodes[0].neighbors[0].first == 1 && graph.nodes[0].neighbors[0].second == 1.0);
    assert(graph.nodes[0].neighbors[1].first == 2 && graph.nodes[0].neighbors[1].second == 2.0);

    std::cout << "Graph loading test passed.\n";
}

void test_bfs() {
    Graph graph;
    graph.load_from_file("test_graph.txt");

    int start = graph.find_or_create_node(0.0, 0.0);
    int goal = graph.find_or_create_node(4.0, 4.0);

    bfs(graph.nodes, start, goal);

    std::cout << "BFS test passed.\n";
}

void test_dfs() {
    Graph graph;
    graph.load_from_file("test_graph.txt");

    int start = graph.find_or_create_node(0.0, 0.0);
    int goal = graph.find_or_create_node(4.0, 4.0);

    dfs(graph.nodes, start, goal);

    std::cout << "DFS test passed.\n";
}

void test_dijkstra() {
    Graph graph;
    graph.load_from_file("test_graph.txt");

    int start = graph.find_or_create_node(0.0, 0.0);
    int goal = graph.find_or_create_node(4.0, 4.0);

    dijkstra(graph.nodes, start, goal);

    std::cout << "Dijkstra test passed.\n";
}

int main() {
    test_graph_loading();
    test_bfs();
    test_dfs();
    test_dijkstra();

    std::cout << "All tests passed.\n";
    return 0;
}
