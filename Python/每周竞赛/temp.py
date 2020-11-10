inventory =  [773160767]
orders = 252264991

temp = (inventory[0] + (inventory[0] - orders + 1)) * orders // 2
print(int(temp % (10 ** 9 + 7)))