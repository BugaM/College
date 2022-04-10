//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_NODE_H
#define LABTREE_NODE_H

#define RED true
#define BLACK false


class Node {
public:
    Node();
    ~Node() = default;
    Node(double key, long idx);
    friend class RedBlackTree;

private:
    double _key;
    long _idx;
    bool color;
    Node* left;
    Node* right;
    Node* parent;
};


#endif //LABTREE_NODE_H
