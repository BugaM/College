//
// Created by buga on 05/04/2022.
//

#include "Node.h"


Node::Node(double key, long idx, bool black) {
    _black = black;
    _key = key;
    _idx = idx;
    left = nullptr;
    right = nullptr;
}