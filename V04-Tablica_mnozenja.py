def dotjeraj(p):
    s="   "+str(p)
    t=len(s)
    return s[t-3:]



ime=input("Upiši svoje dragocjeno ime: ")

for i in range(0,9):
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
        print("----------------------------------------------")
    else: 
        if i == 1:
            print(" : : : : : : : TABLICA MNOŽENJA : : : : : : :")
        else: 
            if i == 3:
                print("  * |", end=" ")
                for k in range(1,11):
                    print(dotjeraj(k), end=" ")
                print()
            else: 
                if i == 5:
                    for l in range(1,11):
                        if l == 10:
                            print(" "+ str(l) + " |", end=" ")
                            for m in range(1,11):
                                print(dotjeraj(l*m), end=" ")
                            print("\n")
                        else:
                            print("  " + str(l) + " |", end=" ")
                            for n in range(1,11):
                                print(dotjeraj(l*n), end=" ")
                            print("\n")
                else: 
                    if i == 7:
                        u = " :  :  :  :  :  :  :  :  :  :  :  :  :  :  :  :  :  by: " + ime
                        v = len(u)
                        print(u[v-45:])





