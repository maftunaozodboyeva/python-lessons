# Amaliyot

# 1-mashq
otam = {
    'ism': "Mavlutdin",
    't_yili': "1934",
    't_shahri': "Samarqand",
}
print(otam)

# 2-mashq
taomlar = {
    'onam': "somsa",
    'dadam': "mastava",
    'singlim': "osh",
    'men': "gamburger",
    'buvim': "osh"
}
print(taomlar['men'])
print(taomlar['singlim'])
print(taomlar['buvim'])

# 3-mashq
dictionary = {
    'if': "agar",
    'integer': "butun son",
    'float': "onlik son",
    'string': "matn",
    'booleon': "mantiqiy qiymat",
    'key': "kalit"
}
print(dictionary['integer'])
print(dictionary['if'])
print(dictionary['float'])
print(dictionary['string'])
print(dictionary['booleon'])

# 4-mashq
python_dictionary = {
    'if': "agar",
    'integer': "butun son",
    'float': "onlik son",
    'string': "matn",
    'booleon': "mantiqiy qiymat",
    'key': "kalit"
}
text = input("Kalit so'zni kiriting")
print(python_dictionary.get(text))
if python_dictionary.get(text) == None:
    print("Bunday kalit so'z mavjud emas.")
else:
    print(python_dictionary.get(text))