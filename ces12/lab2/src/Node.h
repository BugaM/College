//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_NODE_H
#define LABTREE_NODE_H


class Node {
public:
    Node();
    ~Node() = default;
    Node(double key, long idx);
    friend class RedBlackTree;

private:
    double _key;
    long _idx;
    bool red;
    Node* left;
    Node* right;
    Node* parent;
};


#endif //LABTREE_NODE_H
