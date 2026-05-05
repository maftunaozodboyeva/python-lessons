# # lambda function - anonymus(maxfiy, noma'lum) function
# # syntax:
# # lambda arguments: expression(ifoda)
# x = lambda a : a % 5
# print(x(12))  # 2
        
# import math as m
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(m.pi, 5))  # 31.41592653589793

# product = lambda x, y : x ** y
# print(product(3, 2))  # 9

# def daraja(n):
#     return lambda x : x ** n
# kvadrat = daraja(2)
# print(kvadrat(5))

sonlar = [2, -2, 4]
# sonlar2 = []
# for son in sonlar:
#     sonlar2.append(sonlar ** 2)
# print(sonlar2)

print(list(map(lambda x : x * 2, sonlar)))
