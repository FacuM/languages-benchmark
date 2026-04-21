from tasks.compat import emit, join_path, read_text


class Node(object):
    __slots__ = ('value', 'left', 'right')

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _insert(root, value):
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


def _contains(root, value):
    node = root
    while node is not None:
        if value < node.value:
            node = node.left
        elif value > node.value:
            node = node.right
        else:
            return True
    return False


def run(size, fixtures_root):
    tokens = [int(x) for x in read_text(join_path(fixtures_root, 'generated', 'bst', '%s.txt' % size)).split()]
    insert_count = tokens[0]
    inserts = tokens[1:1 + insert_count]
    query_idx = 1 + insert_count
    query_count = tokens[query_idx]
    queries = tokens[query_idx + 1:query_idx + 1 + query_count]
    root = None
    for value in inserts:
        root = _insert(root, value)
    total = 0
    for value in queries:
        if _contains(root, value):
            total += value
    emit(total)
