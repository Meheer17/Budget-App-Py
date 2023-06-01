import math
class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def __str__(self):
        text_list = []
        text = ""
        for i in self.ledger:
            if len(i["description"]) < 23:    
                text_list.append(i["description"].ljust(23, " ") + ("%.2f" % i["amount"]).rjust(7, " "))
            else:    
                text_list.append(i["description"][:23] + ("%.2f" % i["amount"]).rjust(7, " "))
        text += self.name.center(30, '*')
        for i in text_list:
            text += f"\n{i}"
        text += f"\nTotal: {self.get_balance()}"
        return text
    
    def deposit(self, amt, des=""):
        self.ledger.append({"amount": amt, "description": des})
    
    def withdraw(self, amt, des=""):
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": des})
            return True
        else:
            return False

    def get_balance(self):
        bal = 0
        for i in self.ledger:
            if float(i["amount"]) > 0:
                bal += float(i["amount"])
            elif float(i["amount"]) < 0:
                bal += float(i["amount"])
        return bal
    
    def transfer(self, amt, name):
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": f'Transfer to {name.name}'})
            name.ledger.append({"amount": amt, "description": f'Transfer from {self.name}'})
            return True
        else:
            return False
    
    def check_funds(self, amt):
        bal = self.get_balance()
        if amt > bal: 
            return False
        else:
            return True



def create_spend_chart(categories):
  s = "Percentage spent by category\n"

  total = 0
  cats = {}
  for cat in categories:
    cat_total = 0
    for item in cat.ledger:
      amount = item["amount"]
      if amount < 0:
        total += abs(amount)
        cat_total += abs(amount)

    cats[cat.name] = cat_total

  cats = {
    k: (v / total) * 100
    for k, v in cats.items()
  }

  dash_width = len(cats) * 3 + 1
  spaces = dash_width - 1
  for n in range(100, -1, -10):
    s += f"{n:>3}| "
    bar_row = []
    for val in cats.values():
      row_val = [' '] * 3
      if val >= n:
        row_val[0] = "o"
      bar_row += row_val
    s += f"{''.join(bar_row)}{' ' * (spaces - len(bar_row))}\n"
    
  s += f"{' ' * 4}{'-' * dash_width}\n"

  cat_names = [list(name) for name in cats]
  while any(cat_names):
    s += f"{' ' * 4}"
    for name in cat_names:
      s += f" {' ' if not name else name.pop(0)} "
    s += " \n"
  # Need to add strip to remove the newline character for last line and then add back the spaces. If anyone has a better solution, let me know :)
  s = s.strip() + '  '

  # print(s)
  return s
