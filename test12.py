costRub = int(input())
costKop = int(input())
cont = int(input())
costInKop = costRub * 100 + costKop
price = costInKop * cont
print(price // 100, price % 100)
