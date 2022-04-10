//
// Created by buga on 05/04/2022.
//

#include "Node.h"

Node::Node() {
    left = nullptr;
    right = nullptr;
    parent = nullptr;
    red = false;
}

Node::Node(double key, long idx) {
    red = true;
    _key = key;
    _idx = idx;
    left = nullptr;
    right = nullptr;
    parent = nullptr;
}