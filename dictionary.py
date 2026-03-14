# Data types (ma'lumot turlari)
# 1. integer(butun son) 2. float 3. string 4. booleon 5. list 6. tuple 7. dictionary
cars = ['audi', 'chevrolet', 'BYD', 'tesla']

# Dictionary (lug'at)
# key-value pair (kalit-qiymat juftligi)
car = {
    'brand': "Ford",
    'name': "Mustang",
    'year': 2000,
    'color': "crimson"
}
print(car)
print(type(car)) # <class 'dict'>

student = {
    'fullname': 'Jon Doe',
    'age': '20',
    'course': 3,
    'favourite_books': ["Atomic habits", "O'tgan kunlar", "Dunyoning ishlari"],
    'is_completed': False,
    'is_married': True
}

# 1. Qiymatlarni olish
print(student['fullname'])
print(student['age'])
print(student['favourite_books'])

for book in student['favourite_books']:
    print(book)

# 2. Qiymatlarni o'zgartirish
student['age'] = 21
print(student)

# 3. Yangi key-value qo'shish
student['hobbies'] = ["Reading a book"]
print(student)

# 4. Key-valueni o'chirish
del student['is_married']
print(student)

# 5. Empty diict (bo'sh lug'at)
talaba_1 = {}

talaba_1['ism'] = 'maftuna ozodboyeva'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}

print(telefonlar.get('vali')) # 'galaxy s9'
print(telefonlar.get('akmal')) # None