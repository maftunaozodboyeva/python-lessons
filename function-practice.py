# 2.
def kvadrat_kub_hisobla(son):
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son} ning kvadrati: {kvadrat}, kubi: {kub}")

son = int(input("Son kiriting: "))
kvadrat_kub_hisobla(son)
# 3.
def tekshir_son():
    son = int(input("Son kiriting: "))
    
    if son % 2 == 0:
        print("Bu son juft")
    else:
        print("Bu son toq")

tekshir_son(son)

# 4.
def solishtirish(a, b):
    if a > b:
        print(f"{a} katta {b} dan.")
    elif a < b:
        print(f"{b} katta {a} dan.")
    else:
        print("Ikkala son teng.")

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))

# 5.
def daraja_hisobla(son, daraja=2):
    natija = son ** daraja
    print(f"{son} ning {daraja} darajasi: {natija}")

x = int(input("Asos son kiriting: "))
y = int(input("Daraja kiriting: "))
daraja_hisobla(x, y)

# 6.
def kvadrat_perimetr(son):
    perimetr = 4 * son
    print(f"{son} ning kvadratining perimetri: {perimetr}")

son = int(input("Kvadratning tomonini kiriting: "))
kvadrat_perimetr(son)

# 7.
def bolinish(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")

a = int(input("Xohlagan son kiriting: "))
bolinish(a)