ime = input("Kako se zoveš? ")
print("Pozdrav, " + ime +"!")

grad = input("Odakle si? ")
print(grad + " je lijep grad!")

broj = input("Koji je tvoj članski broj? ")

#različiti načini ispisa
print("Član broj %s zove se %s i dolazi iz %s." % (broj, ime, grad))
print("Član broj {} zove se {} i dolazi iz {}.".format(broj, ime, grad))
print("Član broj {0} zove se {1} i dolazi iz {2}.".format(broj, ime, grad))
print("Član broj {b} zove se {i} i dolazi iz {g}.".format(b=broj, i=ime, g=grad))
print("Član broj",broj, "zove se",ime, "i dolazi iz",grad,".")

#integer
a = 9
print(a, "=>", type(a))

#float
b = 3.14
print(b, "=>", type(b))

#complex number
x = 7+2j
print(x, "=>", type(x))

#elemente liste navodimo u uglatim zagradama, mogu biti različitog tipa
lista=[a,b,x,grad, bool(1)]
print(lista)

#dijelovi liste
y = [1,2,3,4,5,6,7,8,9]
print(y)
print("y[2] = ", y[2])
print("y[0:3] = ", y[0:3])
print("y[5:] = ", y[5:])

#ako dodamo element s indexom 0, svi elementi liste će se pomaknuti
y.insert(0,-1)
print(y)

# brisanje zadnjeg elementa liste
del y[len(y)-1]
print(y)

# elementi liste se mogu mijenjati (mutable)
y[2]=7
print(y)

# tuple (ntorka) je isto što i lista, ali elementi se ne mogu mijenjati (immutable)
# elemente navodimo u oblim zagradama
tupko=(8,0.543,x, ime, bool(0))
print(tupko)

z = (1,2,3,4,5,6,7,8,9)
print(z)
print("z[5] = ", z[5])
print("z[4:7] = ", z[4:7])
print("z[3:] = ", z[3:])

# tuple se ne može mijenjati (TypeError: 'tuple' object does not support item assignment)
#z[2]=7
#print(z)

# set (skup) je isto što i lista, ali elementi mogu biti jedinstveni
# elemente seta navodimo u vitičastim zagradama

w = {1,2,2,3,3,3,4,4,4,4}
print(w)
w=sorted(w, reverse=True)
print(w)
w.insert(3,5)
print(w)
w=sorted(w)
print(w)

# dictionary (json look-alike)
d={"name":"Bruno","years": 50}
print(d)
print(d["name"])

# combination (kao Praskaton)
f=100
data = {
    "id": f,
    "grades": (2,2,3,2,3,2,3,2,3,2),
    "points": [7,8,7,6,5,6,7,6,5,6],
    "items": {1,2,3,4,5,6,7,8,9,10}
    }
print(data)

# Array of characters (String)
s="NIGHTSHADOW"
print(s)
print(s[4])   
print(s[3:7])
print(s[5:])    
print(s * 2)
print(s + " 2024") # Prints concatenated string

#String cannot be modified (immutable)
#TypeError: 'str' object does not support item assignment
#s[2]="B"
t=list(s)
t[2]="B"
t="".join(t)
print(id(t))
print(t)
t=t.replace("H","M")
print(id(t))
print(t)

# conversions


string=str(5.351)
print(string)

lista=list(string)
print(lista)

skup=set(string)
print(skup)

ntorka=tuple(string)
print(ntorka)

rjecnik=dict([("x1",1),("x2",1)])
print(rjecnik)


#ugrađene funkcije:
#https://docs.python.org/3/library/functions.html
