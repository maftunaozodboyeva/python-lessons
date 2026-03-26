# Function - ma'lum vazifani bajaruvchi kod bloki.
# Funksiya yaratish uchun def kalit so'zidan foydalanamiz.
# Pythondagi tayyor funksiyalar - print(), len(), input() va boshqalar.
print("Hello world")
# Funksiyani e'lon qilish(declaration)
def salom_ber():
    print("Salom, do'stlar!")
    return "Salom, do'stlar!" # Funksiyadan qiymat qaytarish

# Funksiyani chaqirish(call)
salom_ber() # Natija: Salom, do'stlar!

# Funksiyada parametrlar, ardumentlar
def salom_ber(ism):
    print(f"Assalomu aleykum, {ism}!")

salom_ber("Maftuna")

# Calculator funksiyasi
def yigindi(a, b):
    print(a + b)
yigindi(5, 10)

# Defoult parametrlar
def calculate_age(birth_year, name):
    age = 2026 - birth_year
    print(f"{name}ning yoshi {age} da.")

calculate_age(2010, "Maftuna")

def yosh_hisobla(tugilgan_yil, joriy_yil=2026):
    print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz.")
