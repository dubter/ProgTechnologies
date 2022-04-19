#!/usr/bin/python
import sys
import json

header_path = sys.argv[1]
src_path = sys.argv[2]
print("First program")
### Generate .hpp
header_template = """#pragma once
bool less(const int& x, const int& y);
"""
with open(header_path, 'w') as f:
f.write(header_template)
### Generate .cpp
source_template = """
bool less(const int& x, const int& y) {
return (x < y);
}
"""
with open(src_path, 'w') as f:
f.write(source_template)
