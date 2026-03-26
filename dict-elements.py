# Dictionary elementlari bilan ishlash
# phone = {
#     'brand': 'IPhone 17 Pro Max',
#     'model': 'Galaxy S21',
#     'year': 2021,
#     'color': 'Phantom Gray',
#     'price': 799
# }
# # 1. get metodi - kalit orqali qiymatni olish
# print(phone.get('brand')) # IPhone 17 Pro Max
# print(phone.get('model')) # Galaxy S21
# print(phone.get('year')) # 2021
# print(phone.get('battery')) # None
# print("battery", "Kalit topilmadi") # Kalit topilmadi

# 2. items() metodi - lug'at elementlarini (kalit-qiymat juftlarini) olish
# print(phone.items()) # dict_items([('brand', 'IPhone 17 Pro Max'), ('model', 'Galaxy S21'), ('year', 2021), ('color', 'Phantom Gray'), ('price', 799)])
# for key, value in phone.items():
#     print(f"{key}: {value}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# 3. keys() metodi - lug'atning barcha kalitlarini olish
# print(phone.keys()) # dict_keys(['brand', 'model', 'year', 'color', 'price'])
# print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = {
    'olma': 10000,
    'anor': 15000,
    'uzum': 12000,
    'anjir': 20000,
    'shaftoli': 18000
}

# print(mahsulotlar.keys())
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori - kalitning lug'atda mavjudligini tekshirish
# fruits = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']
# print('olma' in fruits) # True
# print('tarvuz' in fruits) # False

# fruit = input("Qaysi meva yoqadi? ")
# if fruit in fruits:
#     print(f"{fruit.title()} do'konimizda bor.")
# else:
#     print(f"{fruit.title()} do'konimizda yo'q.")

bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     print(mahsulot) # lug'atning kalitlari bo'ladi

# mahsulotlar - lug'at, bozorlik - ro'yxat, mahsulot - lug'atning kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} - {mahsulotlar[mahsulot]} so'm")

# 5. values() metodi - lug'atning barcha qiymatlarini olish
print(phone.values()) # dict_values(['IPhone 17 Pro Max', 'Galaxy S21', 2021, 'Phantom Gray', 799])
print(telefonlar.values()) # dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokia 3310'])

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida': 'galaxy s9'
}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ')
for tel in telefonlar.values():
    print(tel)

# vazifa
# 1-mashq
lugat = {
    "array": "Bir turdagi elementlardan tashkil topgan tartibli to‘plam",
    "boolean": "True yoki False qiymatlarini oluvchi ma'lumot turi",
    "class": "Obyektlar yaratish uchun shablon",
    "dictionary": "Kalit-qiymat juftliklaridan iborat ma'lumot tuzilmasi",
    "function": "Qayta ishlatiladigan kod bloki",
    "integer": "Butun sonlar turi",
    "list": "Tartibli va o‘zgaruvchan elementlar ro‘yxati",
    "loop": "Kod blokini bir necha marta bajarish uchun ishlatiladi",
    "string": "Matnli ma'lumot turi",
    "tuple": "O‘zgarmas (immutable) tartibli to‘plam"
}

# Lug'atni alifbo tartibida chiqaramiz
for kalit in sorted(lugat.keys()):
    print(f"{kalit.title()} -> {lugat[kalit]}")

# 2-mashq
# Davlatlar va poytaxtlar lug'ati
davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSh": "Vashington",
    "Fransiya": "Parij",
    "Germaniya": "Berlin",
    "Yaponiya": "Tokio",
    "Italiya": "Rim",
    "Ispaniya": "Madrid",
    "Angliya": "London",
    "Xitoy": "Pekin",
    "Rossiya": "Moskva"
}

# Davlatlarni alifbo tartibida chiqarish
print("Davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)

# Poytaxtlarni alifbo tartibida chiqarish
print("\nPoytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)