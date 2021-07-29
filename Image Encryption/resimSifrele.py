import sifrelemeSade
def clear():
    clearIMG = open("sakir.jpg","w")
    clearIMG.write("")

def openIMG():
    with open("sakir.png","rb") as imgwbe:
        return str(imgwbe.read())

def cryptIMG():
    print(openIMG())
    sifre = sifrelemeSade.encrypt(openIMG())
    imgwbe = open("sakir.png", "w")
    imgwbe.write(sifre)

cryptIMG()