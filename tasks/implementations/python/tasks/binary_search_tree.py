from pathlib import Path

class Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def _insert(root, value: int) -> Node:
    if root is None:
        return Node(value)
    node = root
    while True:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return root
            node = node.left
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return root
            node = node.right
        else:
            return root


def _contains(root, value: int) -> bool:
    node = root
    while node is not None:
        if value < node.value:
            node = node.left
        elif value > node.value:
            node = node.right
        else:
            return True
    return False


def run(size: str, fixtures_root: str) -> None:
    tokens = [int(x) for x in Path(fixtures_root, "generated", "bst", f"{size}.txt").read_text(encoding="utf-8").split()]
    insert_count = tokens[0]
    inserts = tokens[1:1 + insert_count]
    query_count_idx = 1 + insert_count
    query_count = tokens[query_count_idx]
    queries = tokens[query_count_idx + 1:query_count_idx + 1 + query_count]
    root = None
    for value in inserts:
        root = _insert(root, value)
    total = 0
    for value in queries:
        if _contains(root, value):
            total += value
    print(total)
