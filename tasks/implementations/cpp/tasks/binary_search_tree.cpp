#include <fstream>
#include <iostream>
#include <string>

struct Node {
    int value;
    Node* left;
    Node* right;
    explicit Node(int v) : value(v), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int value) {
    if (!root) return new Node(value);
    Node* node = root;
    while (true) {
        if (value < node->value) {
            if (!node->left) { node->left = new Node(value); return root; }
            node = node->left;
        } else if (value > node->value) {
            if (!node->right) { node->right = new Node(value); return root; }
            node = node->right;
        } else return root;
    }
}

bool contains(Node* root, int value) {
    Node* node = root;
    while (node) {
        if (value < node->value) node = node->left;
        else if (value > node->value) node = node->right;
        else return true;
    }
    return false;
}

void free_tree(Node* root) {
    if (!root) return;
    free_tree(root->left);
    free_tree(root->right);
    delete root;
}

void run_binary_search_tree(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/bst/" + size + ".txt");
    int insert_count = 0;
    file >> insert_count;
    Node* root = nullptr;
    for (int i = 0; i < insert_count; ++i) {
        int value = 0;
        file >> value;
        root = insert(root, value);
    }
    int query_count = 0;
    file >> query_count;
    long long total = 0;
    for (int i = 0; i < query_count; ++i) {
        int value = 0;
        file >> value;
        if (contains(root, value)) total += value;
    }
    free_tree(root);
    std::cout << total << std::endl;
}
