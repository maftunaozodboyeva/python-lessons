text = "Hey guys, welcome to my course"
# print(len(text)) # 34
# print(text[0]) # H
# print(text[1]) # e
# print(text[2]) # y
# print(text[3]) #
# print(text[4]) # g
# print(text[5]) # u
# print(text[6]) # y
# print(text[7]) # s
# print(text[-1]) # !
# print(text[-2]) # e
# print(text[-3]) # r


# length = len(text)
# print(text[length - 1]) # !

#for loop yordamida string ichidagi belgilarni alohida-alohida chiqarish

# 1-usul
# for char in text:
#     print(char)
# 2-usul
# for i in range(len(text)):
#     print(i, text[i])

# in operatori yordamida string ichida ma'lum bir belgi yoki matn bor-yo'qligini tekshirish
print("welcome" in text) # True
print("hey" in text) # False
print("$" in text) # False