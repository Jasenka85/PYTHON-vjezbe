def PrebrojiSlova(x, y):
    #prebacimo sve u velika slova i spojimo u jedan string
    x = x.upper()
    y = y.upper()
    nizslova = x + y       
    print("\n" + nizslova)

    #napravimo niz brojeva iste duljine kao taj string i postavimo da svi elementi u početku budu 1
    k = len(nizslova)
    nizbrojeva =[]               
    for i in range(0,k):
        nizbrojeva.insert(i,1)

    #gledamo slova s lijeva na desno
    for i in range(0,k):     
        n = 1
        while n <= i:
            #ako se npr. 5. slovo podudara s 3. slovom
            if nizslova[i] == nizslova[i - n]:     
                #povećamo 3. član u nizu brojeva za 1
                nizbrojeva[i - n]+=1
                #i izjednačimo 5. član s 3. članom                 
                nizbrojeva[i] = nizbrojeva[i-n]       
            n+=1        
            #n se povećava dok ne dođemo do slova na 0. mjestu
            #kada je to gotovo, prelazimo na sljedeće slovo (i se poveća za 1)
    
    print()
    s=""
    for i in range(0,k):
        #ispišemo sve članove niza brojeva i u isto vrijeme od našeg niza pravimo string
        print(nizbrojeva[i], end=" ")
        s = s + str(nizbrojeva[i])

    print()
    #taj string na kraju rastavljamo - to je važno jer se može pojaviti npr. 13, a mi ga moramo gledati kao 1 i 3
    l=len(s)
    noviniz=[]
    for i in range(0,l):
        noviniz.insert(i,int(s[i]))

    return noviniz



def Sansa(niz):
    t = ""
    k = len(niz)
    #ako je duljina niza parna: m=k/2
    if k%2==0:
        m=int(k/2)
    #ako je duljina niza neparna m=k/2+1
    else:
        m=int(k/2+1)
    #kreiramo novi niz brojeva duljine m
    poluniz =[]
    for i in range(0,m):
        #ovo je srednji član kada je niz neparne duljine
        if i == k - i - 1:
            #ne želimo da ga zbroji sam sa sobom
            poluniz.insert(i,niz[i])      
        else:
            #inače zbrajamo vanjske članove
            poluniz.insert(i, niz[i] + niz[k - i - 1])
        #također koristimo for petlju da ispišemo novi niz i napravimo string (opet npr. 13 treba rastaviti na 1 i 3)
        print(poluniz[i], end=" ")        
        t = t + str(poluniz[i])
    
    print()
    l=len(t)
    noviniz=[]
    for i in range(0,l):
        noviniz.insert(i,int(t[i]))

    if len(noviniz) <= 2:
        print("Šansa za vašu ljubav je {0}{1} %".format(noviniz[0], noviniz[1]))
        return noviniz
    
    else:
        return Sansa(noviniz)


a = input("Unesi svoje ime: ")
b = input("Unesi ime svoje simpatije: ")

c=PrebrojiSlova(a, b)
d=Sansa(c)
