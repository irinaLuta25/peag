import numpy

#facem o fct care determina daca e fezabil sau nu ca individ\
#x-individ
#n-nr gene
#c-costuri
#v-valori

#pasul 1
def ok(x,n,c,v,cmax):
    val = 0 #pt calcul fitness individ x
    cost = 0 #pt calcul cost
    for i in range(n):
        val = val + x[i]*v[i]
        cost = cost + x[i] * c[i]
    return cost <=cmax, val # prima returneaza 1 sau 0, e un if implicit, a 2 a returneaza fotnessul

#pasul 2
#fc = fisier cost, fv = fisier valori
def gen(fc,fv,cmax,dim):
        c = numpy.genfromtxt(fc)
        v = numpy.genfromtxt(fv)
        n = len(c)
        pop = [] #populatia care va fi populata cu indivizi
        for i in range(dim):
            flag = False
            while flag == False:
                x = numpy.random.randint(0,2,n) #se ia fara capatul din dreapta => val de la 0 la 1
                #x = numpy.random.uniform(0,1,n) #interval [0,1)
                #nr val pe care vrem sa le genereze = n
                flag,val = ok(x,n,c,v,cmax)
            #iese din while cand gaseste un individ fezabil => vreau sa il pun in populatie
            x = list(x) #cast la list
            x = x + [val] #[] => il adauga ca elem la sfarsit
            pop = pop + [x] #il introduc in populatie
        return numpy.asarray(pop)
