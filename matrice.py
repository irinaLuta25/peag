import numpy

#definirea unei matrice de dimensiune 4x5 cu elemente de zero
mat = numpy.zeros([4, 5], dtype="double")
print(mat)

#citire din fisier si populare matrice
mat[:4, :4] = numpy.genfromtxt("mat2.txt")
print("Matricea dupa citirea din fisier txt: \n")
print(mat)

#pe ultima coloana calculez suma elementelor de pe fiecare linii
for i in range(4):
    mat[i, 4] = numpy.sum(mat[i, :4])
print("Matricea dupa calculul ultimei coloane: \n")
print(mat)

#generarea unei matrice cu valori aleatoare (din distributia uniforma, pe intervalul 0-1), de dimensiune 5x3
mat_aleator = numpy.random.uniform(0, 1, [5, 3])
print("Matricea cu valori aleatoare: \n")
print(mat_aleator)

