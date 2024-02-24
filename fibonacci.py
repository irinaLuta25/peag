#sirul lui Fibonacci a[0] = 0, a[1] = 1, a[n] = a[n-1] + a[n-2]
#a[2] = 1

#functie care sa calculeze primii n termeni ai sirului lui Fibonacci

def fibL(n):
    f = [0, 1]
    for i in range(2, n):
        f = f + [f[i-1] + f[i-2]]
    return f

print(fibL(10))
#functie care sa calculeze recursiv al n-lea termen al sirului
def fibR(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibR(n-1) + fibR(n-2)

print(fibR(5))
#pentru rulare in consola executati

#import fibonacci
#fibonacci.fibR(20)
#fibonacci.fibL(20)