import random as rd
class Escribe:

    def __init__(self, abecedario=[]):
        if len(abecedario)==0:
            self.abecedario=\
                ["a","b","c","d","e","f","g","h","i","j","k",
                 "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


    def escribir(self,numeroDePalabras=10):
        str=""
        for i in range(0,numeroDePalabras):
            str=str+self.abecedario[rd.randint(0, 25)]
        return str

    def divide_str(self,string):
        lista=[]
        for i in range(0,len(string)):
            lista.append(string[i])

        return lista

