//
// Created by buga on 05/04/2022.
//

#include "RedBlackTree.h"

RedBlackTree::RedBlackTree() {
    NIL = new Node();
    _root = NIL;
}

RedBlackTree::~RedBlackTree() {
    destroyTree(_root);
    delete NIL;
}

void RedBlackTree::destroyTree(Node* &node){
    if (node != NIL) {
        destroyTree(node->left);
        destroyTree(node->right);
        delete node;
    }
}

void RedBlackTree::add(double key, long idx) {
    Node* y = NIL;
    Node* x = _root;
    Node* z = new Node(key, idx);
    while (x != NIL){
        y = x;
        if (key < x->_key){
            x = x->left;
        }
        else{
            x = x->right;
        }
    }
    z->parent = y;
    if (y == NIL){
        _root = z;
    }
    else if (key < y->_key) {
        y->left = z;
    }
    else{
        y->right = z;
    }
    z->left = NIL;
    z->right = NIL;
    z->color = RED;
    insertFixUp(z);
}

void RedBlackTree::insertFixUp(Node* z){
    Node* y;
    while (z->parent->color == RED){
        if (z->parent == z->parent->parent->left){
            y = z->parent->parent->right;
            if (y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            }
            else if (z == z->parent->right){
                z = z->parent;
                leftRotate(z);
            }
            else{
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                rightRotate(z->parent->parent);
            }
        }
        else {
            y = z->parent->parent->left;
            if (y->color == RED) {
                z->parent->color = BLACK;
                y->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            }
            else if (z == z->parent->left){
                z = z->parent;
                rightRotate(z);
            }
            else{
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                leftRotate(z->parent->parent);
            }
        }
    }
    _root->color = BLACK;
}

void RedBlackTree::leftRotate(Node* x){
    Node* y;
    y = x->right;
    x->right = y->left;
    if (y->left){
        y->left->parent = x;
    }
    y->parent = x->parent;
    if (x->parent == NIL){
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

void RedBlackTree::rightRotate(Node* x){
    Node* y;
    y = x->left;
    x->left = y->right;
    if (y->right){
        y->right->parent = x;
    }
    y->parent = x->parent;
    if (x->parent == NIL){
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

long RedBlackTree::size(){
    return size(_root);
}

long RedBlackTree::size(Node* &node){
//    Auxiliar recursive function for binary tree size
    if (node == NIL){
        return 0;
    }
    else {
        return 1 + size(node->left) + size(node->right);
    }
}

void RedBlackTree::find(std::vector<long> &res, double first, double last ){
    smartInOrder(_root , res, first, last);
}

void RedBlackTree::smartInOrder(Node* &node, std::vector<long> &res, double first, double last ){
//    auxiliar recursive function for a "smart" inorder for the given problem
    if (node == NIL) {
        return;
    }
    if (node->_key < first){
        smartInOrder(node->right, res, first, last);
    }
    else{
        smartInOrder(node->left, res, first, last);
        if (node->_key <= last) {
            res.push_back(node->_idx);
            smartInOrder(node->right, res, first, last);
        }
    }
}

