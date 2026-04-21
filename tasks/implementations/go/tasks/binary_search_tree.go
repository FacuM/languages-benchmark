package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

type BSTNode struct {
    value int
    left  *BSTNode
    right *BSTNode
}

func bstInsert(root *BSTNode, value int) *BSTNode {
    if root == nil { return &BSTNode{value: value} }
    node := root
    for {
        if value < node.value {
            if node.left == nil { node.left = &BSTNode{value: value}; return root }
            node = node.left
        } else if value > node.value {
            if node.right == nil { node.right = &BSTNode{value: value}; return root }
            node = node.right
        } else {
            return root
        }
    }
}

func bstContains(root *BSTNode, value int) bool {
    node := root
    for node != nil {
        if value < node.value { node = node.left } else if value > node.value { node = node.right } else { return true }
    }
    return false
}

func RunBinarySearchTree(size string, fixturesRoot string) {
    text, _ := os.ReadFile(filepath.Join(fixturesRoot, "generated", "bst", size+".txt"))
    tokens := strings.Fields(string(text))
    insertCount, _ := strconv.Atoi(tokens[0])
    var root *BSTNode
    for i := 0; i < insertCount; i++ {
        value, _ := strconv.Atoi(tokens[1+i])
        root = bstInsert(root, value)
    }
    queryIndex := 1 + insertCount
    queryCount, _ := strconv.Atoi(tokens[queryIndex])
    total := 0
    for i := 0; i < queryCount; i++ {
        value, _ := strconv.Atoi(tokens[queryIndex+1+i])
        if bstContains(root, value) { total += value }
    }
    fmt.Println(total)
}
