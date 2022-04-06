//
// Created by buga on 05/04/2022.
//

#include "BlackRedTree.h"
#include <iostream>

BlackRedTree::BlackRedTree() {
    _root = nullptr;
}

Node*& BlackRedTree::getRoot(){
    return _root;
}

void BlackRedTree::add(double key, long idx, Node *&root) {
    if (!root){
        root = new Node(key, idx);
    }
    else {
        if (key < root->_key){
            add(key, idx, root->left);
        }
        else{
            add(key, idx, root->right);
        }
    }
}

long BlackRedTree::size(Node *node){
    if (!node){
        return 0;
    }
    else {
        return 1 + size(node->left) + size(node->right);
    }
}
