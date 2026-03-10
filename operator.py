# python operators
# 1.Arithmetic Operatos (+, -, *, /, %, **, //)
# x = 8
# y = 2
# modules(%) - qoldiqni hisoblash
# print(x % y)
# print(3 % 8)
# print(4 // 2, 12 // 5)

# 2.Comparison(solishtirish) operators => Booleon values (True, False)
# == (tengmi)
# != (teng emasmi)
# > (kattami)
# < (kichikmi)
# >= (katta yoki teng)
# <= (kichik yoki teng)

# 3.Logical(Mantiqiy) operators
# and(va) operator
# or(yoki) operator 
# not(emas) operator hamma javoblarni teskari qiladi
import math
# 20
x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
a = math.pow(y, 2) + (y + x * y) / (math.fabs(x * y) + 5)
b = math,pow(x, 2) + (x * y + math.pow(y, 2)) / a
c = (math.pow(x, 2) + 1) / b
d = 1 / (1 + math.cos(x) +(1 / math.sin(x)))
t11 = c + d
print("%.2f" % t11)

# Assignment(tayinlash) operators
z = 12
z += 3 # z = z + 3
print(z)
z -= 3 
print(z)
z *= 2
