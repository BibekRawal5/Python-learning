import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, n):
    balls_taken = []
    con = self.contents.copy()
    if n > len(con):
      return con
    for i in range(n):
      k = random.randrange(len(con))
      v = con.pop(k)
      balls_taken.append(v)
    return balls_taken
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    m = 0
    balls_drawn = hat.draw(num_balls_drawn)
    for k,v in expected_balls.items():
      if v <= balls_drawn.count(k):
        m += 1
        print("m = ", m)
    if m == len(expected_balls):
      count += 1
      print("count = ", count)
  return count/num_experiments



hat = Hat(blue=3,red=2,green=6)

print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
