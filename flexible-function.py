# # Return function
# def sum_list(lst):
#     s = 0
#     for element in lst:
#         s += element

#     return s
# print(sum_list([1, 2, 3, 4]))
# # Flexible(moslashuvchan) function
# *args usuli
# def summa(*numbers):
#     # print(type(numbers))
#     s = 0
#     for element in numbers:
#         s += element
#     return s
# print(summa(12, 34, 56, 78))

# def my_func(*people):
#     print(f"The youndest person is {people[1]}")
# my_func("Ali", "Vali", "Guli")


# **kwargs(keyword arguments) usuli
# def my_func(kompaniya, model, **malumotlar):
#     print(malumotlar)
#     print(type(malumotlar))

# avto_info("GM Uzbekistan", "Cobalt", rang="oq", yil=2020, narh=15000)

# Amaliyot
1.    

def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(2, 3, 4))

# 2.
def talaba_malumoti(ism, familiya, **kwargs):
    talaba = {
        "ism": Maftuna,
        "familiya": Ozodboyeva
    }

    for kalit, qiymat in kwargs.items():
        talaba[kalit] = qiymat
    
    return talaba
