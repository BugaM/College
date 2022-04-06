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
            root->left->parent = root;
        }
        else{
            add(key, idx, root->right);
            root->right->parent = root;
        }
    }
}

void BlackRedTree::leftRotate(Node *&x){
    Node* y;
    y = x->right;
    x->right = y->left;
    if (y->left){
        y->left->parent = x;
    }
    y->parent = x->parent;
    if (!x->parent){
        _root = y;
    }
    else if (x == x->parent->left){
        x->parent->left = y;
    }
    else{
        x->parent->right = y;
    }
    y->left = x;
    x->parent = y;
}

void BlackRedTree::rightRotate(Node *&x){
    Node* y;
    y = x->left;
    x->left = y->right;
    if (y->right){
        y->right->parent = x;
    }
    y->parent = x->parent;
    if (!x->parent){
        _root = y;
    }
    else if (x == x->parent->right){
        x->parent->right = y;
    }
    else{
        x->parent->left = y;
    }
    y->right = x;
    x->parent = y;
}

long BlackRedTree::size(Node *node){
    if (!node){
        return 0;
    }
    else {
        return 1 + size(node->left) + size(node->right);
    }
}
