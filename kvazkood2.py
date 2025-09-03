print(1+1)
print ("1"+"1")
#andme tüübid
# "hello world" - str
# 1 - int
# 1.5 - float

#muutujad
name = "anton"
perekonnanimi = "buketov"
print(name+ " " + perekonnanimi)

# luua muutujad film,aasta,näitlejal ja näitleja 2
# tulemus: film sponge bob ilmus aastal 1999, Stephen Hillenburg
# ning peanäitlejad on spongebob ja patrik

film = "spongebob"
year = "realesed in 1999"
producer = "Stephen Hillenburg"
actorl = "spongebob"
actorl2 = "patrik"
print(" film " + film + " year " + year + " producer " + producer + " " +" actorl "+ actorl + " " +" actor2 " + actorl2)

lemmikloom = input("sisesta oma lemmik loom: ")
print("minu lemmikloom on: " + lemmikloom)

#str() -convert text - convert arv
#int() -convert arv =  - convert text

pikkus = int(input("sisesta pikkus: "))
laius = int(input("sisesta laius"))
umbermot = 2 * (pikkus + laius)
pindala = pikkus * laius
print("ümbermööt: ", umbermot)
print("laius: ", laius)


nimi = input("what s your name?: ")
vanus = input ("how old are you?: ")
elukoht = input (" where are you live?: ")
lemmikmuusik = input ("What is your favorite music?: ")
lemmikfilm = input("what is your favorite film?: ")

print("Welcome", nimi)
print("You are", vanus)
print("You are living in", elukoht)
print("your favorite music is", lemmikmuusik)
print("your favorite film is", lemmikfilm)



