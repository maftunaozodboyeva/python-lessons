# def is_even(number = 8):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(4))  # Output: True
# result = is_even(7)
# print(result)  # Output: False
# print(is_even())  # Output: True

# Ternary operator yordamidagi is_even unksiyasini qisqartirish mumkin:
def is_even(number = 8):
    return "Juft" if number % 2 == 0 else "Toq"

print(is_even(4))  # "Juft"
print(is_even(7))  # "Toq"

vowels = ["a", "e", "i", "o", "u"]
def count_vowels(text):
    count = 0
    for char in text:
        if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("frontender"))

# string bo'yicha for loop ishlatish
text = "Hello"
for char in text:
    print(char)

