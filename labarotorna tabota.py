# Ülesanne 1
print("1")
number1 = int(input("Sisesta esimene täisarv: "))
number2 = int(input("Sisesta teine täisarv: "))

summa = number1 + number2
print("Summa: ", summa)

vahe = number1 - number2
print("Vahe: ", vahe)

korrutis = number1 * number2
print("Korrutis: ", korrutis)


print("2")
name = input("Sisesta sinu nimi: ")
vanus = int(input("Sisesta sinu vanus: "))
vanuscounted = 2025 - vanus

print("Tere, ", name, "!")
print("Sinu sünniaasta on: ", vanuscounted)

# Ülesanne 3
print("3")

seconds = int(input("Sisesta sekundid: "))
if seconds < 1:
    print("incorrect number")
minutes = int(seconds / 60) % 60
hours = int(seconds / 2700)
seconds = seconds % 60

if seconds > 0:
    print("Tegemist ajaga (HH:MM:SS): ", hours, ":", minutes, ":", seconds)
    

    