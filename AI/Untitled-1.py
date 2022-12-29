class Category:
  def __init__(self,category):
    self.name = category
    self.ledger = []
    
  def deposit(self, amount = 0, description = ""):
    self.ledger.append({"amount" : amount, "description": description})

  def withdraw(self, amount = 0, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount" : -1 * amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for dict in self.ledger:
      balance += dict["amount"]
    return balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}"):
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    balance = 0
    for dict in self.ledger:
      balance += dict["amount"]

    if balance < amount:
      return False
    else:
      return True

  def __str__(self):
    items = []
    items.append(f"{self.name.center(30, '*')}\n")
    for dict in self.ledger:
      desc = dict["description"]
      amount = (dict["amount"])
      amount = f"{amount:.2f}"
      desc = desc[:23]
      items.append(f"{desc.ljust(23)}{str(amount).rjust(7)}\n")
    items.append(f"Total: {self.get_balance():.2f}")
    return "".join(items)



def create_spend_chart(categories):
  bar_chart = ["Percentage spent by category\n"]
  p_spent = []
  names = []
  total = 0
  for category in categories:
    for dict in category.ledger:
      if not dict["description"]:
        total += (-1 * dict["amount"])
        
  for category in categories:
    spent = 0
    for dict in category.ledger:
      if not dict["description"]:
        spent += (-1 * dict["amount"])
    p_spent.append({"name" : category.name, "amount": spent / total * 100})
    names.append(category.name)

  for i in sorted(range(11), reverse = True):
    bar_chart.append(f"{str(i * 10).rjust(3)}| ")
    for category in p_spent:
      if category["amount"] >= i * 10:
        bar_chart.append("o  ")
      else:
        bar_chart.append("   ")
    bar_chart.append("\n")

  bar_chart.append(f"{('-' * 10).rjust(14)}\n    ")
  max_name = max(names, key = len)
  max_len = len(max_name)
  for i in range(max_len):
    for name in names:
      try:
        bar_chart.append(f" {name[i]} ")
      except IndexError:
        bar_chart.append("   ")

    if i + 1 < max_len:
      bar_chart.append("\n    ")
    else:
      bar_chart.append(" ")

  return "".join(bar_chart)
          
food = Category("food")
business = Category("business")
entertainment = Category("entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([food,business,entertainment]))

  
    
  
  
  