//
// Created by buga on 05/04/2022.
//

#include "RedBlackTree.h"
#include <iostream>


RedBlackTree::RedBlackTree() {
    NIL = mshp<Node>();
    _root = NIL;
}

//void RedBlackTree::add(double key, long idx, Node *&root) {
//    if (!root){
//        root = new Node(key, idx);
//    }
//    else {
//        if (key < root->_key){
//            add(key, idx, root->left);
//            root->left->parent = root;
//        }
//        else{
//            add(key, idx, root->right);
//            root->right->parent = root;
//        }
//    }
//}

void RedBlackTree::add(double key, long idx) {
    shp<Node> y = NIL;
    shp<Node> x = _root;
    shp<Node> z = mshp<Node>(key, idx);
    while (x.get() != NIL.get()){
        y = x;
        if (key < x->_key){
            x = x->left;
        }
        else{
            x = x->right;
        }
    }
    z->parent = y;
    if (y.get() == NIL.get()){
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
    z->red = true;
    insertFixUp(z);
}

void RedBlackTree::insertFixUp(shp<Node> z){
    shp<Node> y;
    while (z->parent->red){
        if (z->parent.get() == z->parent->parent->left.get()){
            y = z->parent->parent->right;
            if (y->red) {
                z->parent->red = false;
                y->red = false;
                z->parent->parent->red = true;
                z = z->parent->parent;
            }
            else if (z.get() == z->parent->right.get()){
                z = z->parent;
                leftRotate(z);
            }
            else{
                z->parent->red = false;
                z->parent->parent->red = true;
                rightRotate(z->parent->parent);
            }
        }
        else {
            y = z->parent->parent->left;
            if (y->red) {
                z->parent->red = false;
                y->red = false;
                z->parent->parent->red = true;
                z = z->parent->parent;
            }
            else if (z.get() == z->parent->left.get()){
                z = z->parent;
                rightRotate(z);
            }
            else{
                z->parent->red = false;
                z->parent->parent->red = true;
                leftRotate(z->parent->parent);
            }
        }
    }
    _root->red = false;
}

void RedBlackTree::leftRotate(shp<Node> x){
    shp<Node> y;
    y = x->right;
    x->right = y->left;
    if (y->left){
        y->left->parent = x;
    }
    y->parent = x->parent;
    if (x->parent.get() == NIL.get()){
        _root = y;
    }
    else if (x.get() == x->parent->left.get()){
        x->parent->left = y;
    }
    else{
        x->parent->right = y;
    }
    y->left = x;
    x->parent = y;
}

void RedBlackTree::rightRotate(shp<Node> x){
    shp<Node> y;
    y = x->left;
    x->left = y->right;
    if (y->right){
        y->right->parent = x;
    }
    y->parent = x->parent;
    if (x->parent.get() == NIL.get()){
        _root = y;
    }
    else if (x.get() == x->parent->right.get()){
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

long RedBlackTree::size(shp<Node> &node){
    if (node.get() == NIL.get()){
        return 0;
    }
    else {
        return 1 + size(node->left) + size(node->right);
    }
}

void RedBlackTree::find(std::vector<long> &res, double first, double last ){
    smartInOrder(_root , res, first, last);
}

void RedBlackTree::smartInOrder(shp<Node> &node, std::vector<long> &res, double first, double last ){
    if (node.get() == NIL.get()) {
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

