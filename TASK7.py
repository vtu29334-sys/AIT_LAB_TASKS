class MonkeyBananaProblem:

  def __init__(self, monkey_pos, box_pos, banana_pos):
    self.monkey_pos = monkey_pos
    self.box_pos = box_pos
    self.banana_pos = banana_pos
    self.monkey_level = "Down"  # 'Down' or 'OnBox'
    self.has_banana = False
    self.actions = []

  def walk(self, dest):
    self.actions.append(f"walk({self.monkey_pos}, {dest})")
    self.monkey_pos = dest

  def push_box(self, dest):
    if self.monkey_pos == self.box_pos and self.monkey_level == "Down":
      self.actions.append(f"push_box({self.box_pos}, {dest})")
      self.box_pos = dest
      self.monkey_pos = dest
    else:
      raise ValueError("Monkey must be at the box and on the floor to push.")

  def climb_box(self):
    if self.monkey_pos == self.box_pos:
      self.actions.append("climb_box()")
      self.monkey_level = "OnBox"
    else:
      raise ValueError("Monkey must be at the box location to climb.")

  def grasp_banana(self):
    if (
        self.monkey_pos == self.banana_pos
        and self.box_pos == self.banana_pos
        and self.monkey_level == "OnBox"
    ):
      self.actions.append("grasp_banana()")
      self.has_banana = True
    else:
      raise ValueError("Conditions to grasp banana not met.")

  def solve(self):
    if self.monkey_pos != self.box_pos:
      self.walk(self.box_pos)
    if self.box_pos != self.banana_pos:
      self.push_box(self.banana_pos)
    if self.monkey_level != "OnBox":
      self.climb_box()
    if not self.has_banana:
      self.grasp_banana()
    return self.actions


# Example execution for Scenario 1 (Monkey: 0, Box: 2, Banana: 3)
game = MonkeyBananaProblem(monkey_pos=0, box_pos=2, banana_pos=3)
plan = game.solve()
print("Action Sequence:", plan)
