x = int(input("Unesi neki broj do 100: "))
if x==50:
    print("Broj je jednak 50. \n")
else:
    if x > 50:
        print("Broj je veći od 50. \n")
    else:
        print("Broj je manji od 50. \n")


#Note that in Python, we use indentation (typically 4 spaces) to define code blocks.
    

guess = int(input("Pogodi koliko imam godina: "))
if guess == 38:
    print("Pogodio si, bravo! \n")
else: 
    if guess > 30 and guess < 45:
        print("Bio si blizu! \n")
    else:
        print("Nisi ni blizu! \n")


imena = ["Abby", "Brenda", "Cindy", "Diddy"]

for ime in imena:
    print("Moje ime je",ime)
print("\n")

for i in range(1, 11):
    print(i*i, end=" ")
print("\n")


moj_broj = 5
pokusaj = 0
print("Zamislio sam jedan broj između 1 i 10.")
while pokusaj != moj_broj:
    pokusaj = int(input("Pogodi! "))
    if pokusaj != moj_broj:
        print("Nisi pogodio.")
print("Pogodio si! Bravo! \n")


