def twice (function) :
   return lambda x: function(function (x))
def f(x) :
   return x+3

g=twice(f)

print(g(7))

# a. Tuliskan output program
# B. Apakah konsep utama pemrograman fungsional yang diimplementasikan?
# C. Kondisi apa yang menandakan adanya konsep tersebut?