//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_BLACKREDTREE_H
#define LABTREE_BLACKREDTREE_H


#include "Node.h"

class BlackRedTree {
public: BlackRedTree();
        void add(double key, long idx, Node*& root);
        Node*& getRoot();
        long size(Node* node);
private:
        Node *_root;

};


#endif //LABTREE_BLACKREDTREE_H
