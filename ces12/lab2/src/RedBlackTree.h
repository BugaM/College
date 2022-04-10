//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_REDBLACKTREE_H
#define LABTREE_REDBLACKTREE_H

#include "Node.h"
#include <vector>

class RedBlackTree {
public:
        RedBlackTree();
        ~RedBlackTree();
        void add(double key, long idx);
        void destroyTree(Node* &node);
        void leftRotate(Node* x);
        void rightRotate(Node* x);
        void insertFixUp(Node* z);
        long size();
        void find(std::vector<long> &res, double first, double last );
        void smartInOrder(Node* &node, std::vector<long> &res, double first, double last);
private:
        Node* _root;
        Node* NIL;
        long size(Node* &node);

};


#endif //LABTREE_REDBLACKTREE_H
