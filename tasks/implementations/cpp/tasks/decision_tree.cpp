#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct DTNode {
    bool leaf;
    int value;
    int feature;
    int threshold;
    DTNode* left;
    DTNode* right;
};

static const int DT_THRESHOLDS[3] = {250, 500, 750};

double dt_gini(const std::vector<std::vector<int>>& rows) {
    if (rows.empty()) return 0.0;
    int ones = 0;
    for (const auto& row : rows) ones += row[3];
    int zeros = static_cast<int>(rows.size()) - ones;
    double p0 = static_cast<double>(zeros) / rows.size();
    double p1 = static_cast<double>(ones) / rows.size();
    return 1.0 - p0 * p0 - p1 * p1;
}

int dt_majority(const std::vector<std::vector<int>>& rows) {
    int ones = 0;
    for (const auto& row : rows) ones += row[3];
    return ones * 2 >= static_cast<int>(rows.size()) ? 1 : 0;
}

DTNode* dt_leaf(int value) {
    return new DTNode{true, value, 0, 0, nullptr, nullptr};
}

DTNode* dt_build(const std::vector<std::vector<int>>& rows, int depth) {
    if (depth == 0 || rows.empty()) return dt_leaf(rows.empty() ? 0 : dt_majority(rows));
    bool pure = true;
    for (const auto& row : rows) if (row[3] != rows[0][3]) { pure = false; break; }
    if (pure) return dt_leaf(rows[0][3]);
    double best_score = 1e9;
    DTNode* best = nullptr;
    for (int feature = 0; feature < 3; ++feature) {
        for (int threshold : DT_THRESHOLDS) {
            std::vector<std::vector<int>> left;
            std::vector<std::vector<int>> right;
            for (const auto& row : rows) {
                if (row[feature] <= threshold) left.push_back(row); else right.push_back(row);
            }
            if (left.empty() || right.empty()) continue;
            double score = (left.size() * dt_gini(left) + right.size() * dt_gini(right)) / rows.size();
            if (score < best_score) {
                if (best && !best->leaf) { /* leaked old tree acceptable for benchmark build-time simplicity */ }
                best_score = score;
                best = new DTNode{false, 0, feature, threshold, dt_build(left, depth - 1), dt_build(right, depth - 1)};
            }
        }
    }
    return best ? best : dt_leaf(dt_majority(rows));
}

int dt_predict(DTNode* node, const std::vector<int>& row) {
    if (node->leaf) return node->value;
    return dt_predict(row[node->feature] <= node->threshold ? node->left : node->right, row);
}

void run_decision_tree(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/decision_tree/" + size + ".csv");
    std::string line;
    std::getline(file, line);
    std::vector<std::vector<int>> rows;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string part;
        std::vector<int> row;
        while (std::getline(ss, part, ',')) row.push_back(std::stoi(part));
        rows.push_back(row);
    }
    DTNode* tree = dt_build(rows, 3);
    long long correct = 0;
    long long pred_sum = 0;
    for (int i = 0; i < static_cast<int>(rows.size()); ++i) {
        int pred = dt_predict(tree, rows[i]);
        if (pred == rows[i][3]) correct += 1;
        pred_sum += static_cast<long long>(pred) * (i + 1LL);
    }
    std::cout << correct * 100000LL + pred_sum << std::endl;
}
