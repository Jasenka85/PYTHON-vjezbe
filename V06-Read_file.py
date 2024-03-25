
#ovako nam dale listu stringova:
f = open("zivotinje.txt", "r")
lines = f.readlines()
print(lines)

#možemo isprintati jedan po jedan element i usput maknuti \n
for line in lines:
    line = line.replace("\n", "")
    print(line)
print()


#Drugi način - jedno ispod drugog
with open("zivotinje.txt") as f:
    content = f.readlines()
for line in content:
    print(line, end="")
print()


#Treći način - u istom redu
with open("zivotinje.txt") as f:
    content = f.read().splitlines()
for line in content:
    print(line, end=" ")


#Prvo provjera postoji li taj file
import os.path
filename = "zivotinje.txt"

if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        content = f.read().splitlines()
    for line in content:
        print(line)