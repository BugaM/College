//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_NODE_H
#define LABTREE_NODE_H


class Node {
public:
    Node(double key, long idx, bool black=true);
    friend class BlackRedTree;

private:
    double _key;
    long _idx;
    bool _black;
    Node *left;
    Node *right;
};


#endif //LABTREE_NODE_H
