# a;lksdjf;alksgh[oaiuehrg'laijf;laksrj;alrkjh string by Sean Valdivia

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # given this, and cb

    #if there is a value, and it's not equal to none, put that value into the CB.

    if not self.value == None:
      cb(self.value)

    # this.value is the value of left i.e traverse left tree recursively.

    if self.left:
      # we have given CB above self.value, so if we call cb(that has the value of left/ right) it can go to the left calling that value from cb
      
      self.left.depth_first_for_each(cb)

    if self.right:
      # if we go left, we have to have the abilitiy to go across the row

      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    pass

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
    # base case

    if self.value == target:
      return True

    # call recursively 

    if self.left:
      if self.left.contains(target):
        return True

    # if target doesn't exist in the left at any point

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
