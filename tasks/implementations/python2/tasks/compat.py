import io
import os
import sys


def join_path(*parts):
    return os.path.join(*parts)


def read_text(path):
    handle = io.open(path, 'r', encoding='utf-8')
    try:
        return handle.read()
    finally:
        handle.close()


def read_lines(path):
    return read_text(path).splitlines()


def open_text(path):
    return io.open(path, 'r', encoding='utf-8')


def walk_text_files(root, suffix='.txt'):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for filename in sorted(filenames):
            if filename.endswith(suffix):
                yield os.path.join(dirpath, filename)


def emit(value):
    sys.stdout.write(str(value) + '\n')
