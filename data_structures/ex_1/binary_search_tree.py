class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = []
    #enqueue
    stack.append(self)
    # dequeue if not empty
    while len(stack) > 0:
      curr = stack.pop()
    # check is curr is on the right
      if curr.right:
        stack.append(curr.right)
        print("right", curr.right.value)
    # check is curr is on the left 
      if curr.left:
        stack.append(curr.left)
        print("left", curr.left.value)
    # call cb on curr.alue
      cb(curr.value)


  def breadth_first_for_each(self, cb):
    queue = []
    # enqueue
    queue.append(self)
    while len(queue) > 0:
      #pop first item 
      curr = queue.pop(0)
      # if curr is curr.left enqueue
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
      #call cb
      cb(curr.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
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
