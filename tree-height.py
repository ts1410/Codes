# python3
from collections import namedtuple

tree = namedtuple('tree', 'parent height')

class TreeHeight:


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())
