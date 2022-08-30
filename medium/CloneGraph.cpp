/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

#include <map>
using namespace std;

class Solution {
public:
    Node* cloneNodeandNeighbours(Node* node, map<int, Node*>* nodes) {
        if (nodes->count(node->val) == 0) {
            cout << node->val << endl;
            (*nodes)[node->val] = new Node{node->val};
            for (auto n:node->neighbors) {
                (*nodes)[node->val]->neighbors.emplace_back(cloneNodeandNeighbours(n, nodes));
            }
        }
        return (*nodes)[node->val];
    }
    Node* cloneGraph(Node* node) {
        // whenever you create a new node, place it in a dictionary
        // before creating a new node, check if it is in the dictionary already
        if (node == NULL) return NULL;
        map<int, Node*> nodes;
        return cloneNodeandNeighbours(node, &nodes);
    }
};
