#!/usr/bin/python
import sys
import json

path = sys.argv[1]
src = sys.argv[2]
tmp = """#pragma once
bool less(int& x, int& y);
"""
with open(path, 'w') as f:
    f.write(tmp)
source_template = """
bool less(int& x, int& y) {
    return (x < y);
}
"""
with open(src, 'w') as f:
    f.write(source_template)
