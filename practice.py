import numpy

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#concat using +
helloworld= "hello" + " "+ "world"
print(helloworld)
#multiply strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

#concat lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
#multiply lists
print([1,2,3]*4)

#string formatting
name = "Irina"
age = 20
print("Hello, %s!" % name)
print("%s is %d years old." % (name,age))
#an obj which is not a string can be formatted with %s as well!
list = [1,2,3]
print("List: %s" % list)
'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''

#example of string format
data = ("John","Doe","53.44")
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

#string operations
name = "Lala1234"
print(len(name))
print(name.count("a"))
print(name.index("a"))
print(name.upper())
print(name.lower())
#prints la1
print(name[2:5])
#prints l2 - skips 2
print(name[2:6:3])
#reverse string
print(name[::-1])
print(name.startswith("Lala"))
print(name.endswith("000"))
string = "Lala mmmm"
#prints ['Lala', 'mmmm']
print(string.split(" "))

#calcul primii n termeni fibonacci
def fib(n):
    f=[0,1]
    for i in range (2,n):
        f=f+[f[i-1]+f[i-2]]
    return f

print(fib(10))

#calcul al n lea termen recursiv
def fibR(n):
    if n==0:
        return 0
    else:
        if n==1:
            return 1
        else:
            return fibR(n-1)+fibR(n-2)

print(fibR(5))

#matrice

#definirea unei matrice de dimensiune 4x5 cu elemente de zero
mat = numpy.zeros([5,6],dtype="double")
print(mat)

#citire din fisier si populare matrice
print("Matricea dupa citirea din fisier txt: \n")
mat[:5,:5] = numpy.genfromtxt("mat2.txt")
print(mat)

#pe ultima coloana calculez suma elementelor de pe fiecare linii
for i in range(5):
    mat[i,5]=numpy.sum(mat[i,:5])
print("Matricea dupa calcul ultima coloana: \n")
print(mat)
#generarea unei matrice cu valori aleatoare (din distributia uniforma, pe intervalul 0-1), de dimensiune 5x3
mat_random = numpy.random.uniform(0,1,[6,7])
print("Matricea generata aleator: \n")
print(mat_random)
