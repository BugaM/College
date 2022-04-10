//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_NODE_H
#define LABTREE_NODE_H

#ifndef shp
#define shp  std::shared_ptr
#endif

#ifndef mshp
#define mshp std::make_shared
#endif

#include <memory>

class Node {
public:
    Node();
    ~Node() = default;
    Node(double key, long idx);
    friend class RedBlackTree;

private:
    double _key;
    long _idx;
    bool red;
    shp <Node> left;
    shp <Node> right;
    shp <Node> parent;
};


#endif //LABTREE_NODE_H
