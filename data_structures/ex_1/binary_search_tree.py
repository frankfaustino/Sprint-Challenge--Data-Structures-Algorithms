from stack import Stack
from queue import Queue


class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if self is None:
      return
    stack = Stack()


    pass    

  def breadth_first_for_each(self, cb):
    if self is None:
      return
    queue = Queue()
    queue.enqueue(self)
    while queue.len() > 0:
      current = queue.dequeue()
      cb(current.value)

      if current.left:
        queue.enqueue(current.left)
      if current.right:
        queue.enqueue(current.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value



bst = BinarySearchTree(5)
bst.insert(9)
bst.insert(2)
bst.insert(3)
bst.insert(8)
bst.insert(4)
bst.insert(7)
bst.insert(6)
bst.breadth_first_for_each(print)
