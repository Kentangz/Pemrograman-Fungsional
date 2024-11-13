# sum
# for x in my_list:
#     sum
# print (sum)


# a. Apakah output dari code tersebut jika my_list = [1, 2, 3, 4, 5] ?
my_list = [ 1,2,3,4,5]
sum = 0

for x in my_list:
    sum += x
print(sum)


# b. Tambahkan fungsi untuk memberikan output pangkat dan double/kali dua, untuk setiap nilai dari my_list!
my_list = [1, 2, 3, 4, 5]

def pangkat(x):
    return x ** 2
def kali(x):
    return x * 2

squares = list(map(pangkat, my_list))
doubles = list(map(kali, my_list))

print("Squares:", squares)
print("Doubles:", doubles)


# c. Ubah code tersebut menggunakan gaya penulisan fungsional, dengan mengimplementasikan functools, lambda, list, map.
from functools import reduce

my_list = [1, 2, 3, 4, 5]

total = reduce(lambda var, x: var + x, my_list)

squares = list(map(lambda x: x ** 2, my_list))
doubles = list(map(lambda x: x * 2, my_list))

print("Total:", total)
print("Squares:", squares)
print("Doubles:", doubles)


print(" \n Total:", total)
print("Squares:", squares)
print("Doubles:", doubles)
