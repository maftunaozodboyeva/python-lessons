# # Ma'lumot turlari (Data types)
# # 1.String (matn)
# # 2.Number (son) => 1. Integer(butun son) 2. Float(o'nlik son)
# # 3.Boolean (Mantiqiy qiymat) => 1.True(haqiqat) 2.False(yolg'on)

#  a = 20
#  b = -30
#  c = a + b
#  print(c)

# pi = 3.14159 # o'nlik son (float)
# radius = 10  # butun son (integer)
# diametr = 2 * radius
# yuza = pi * radius ** 2
# print(diametr)
# print(yuza)

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

# x, y, z = 7, -5, 10
# print(x + y - z)

# kv_tomon = int(input("Kvadrat tomoni kiriting: ")) # 5 => "5" = 5
# print(kv_tomon ** 2)

# ism = "Jobir"
# yoshi = 36
# xabar = ism + "" + str(yoshi) + "yoshda"
# print(xabar)

# print(int(5.5)) # 5

# t_yil = int(input("Tug'ilgan yilingizni kiriting:"))
# yosh = 2025 - t_yil
# print(yosh)

# x = int(input("Istalgan son kiriting:"))
# print(x, "ning kvadrati", x ** 2, "ga kubi esa" + x ** 3 + "ga teng")
# xabar = str(x) + "ning kvadrati", + str(x ** 2) + "ga kubi esa", + str(x ** 3) + "ga teng"
# print(xabar)

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
j1 = str(x) + str(y)
j2 = str(x) - str(y)
j3 = str(x) * str(y)
j4 = str(x) / str(y)
print()