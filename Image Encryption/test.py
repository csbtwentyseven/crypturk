import sifrelemeSade
from sifrelemeSade import *

with open("sakir.jpg","r+b") as resim:
    veri = ["seefa","bcf","cdf"]
    sakir = open("sakir.jpg", "r")
    necati = open("necati.jpg","w")

    necati.write(sifrelemeSade.encrypt(sakir.read()))

with open("necati.jpg","a") as resimyaz:
    pass
