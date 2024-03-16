#cantidad de letras de un texto
Texto = input("Ingrese su Texto: ").lower()
print(Texto)
Letra1 = input("Digite su primera Letra: ").lower()
Letra2 = input("Digite su segunda Letra: ").lower()
Letra3 = input("Digite su tercera Letra: ").lower()

Lista1=[]
Lista1.append(Letra1)
Lista1.append(Letra2)
Lista1.append(Letra3)

contar1=Texto.count(Letra1)
print(f"La cantidad de la primera letra que digistaste en el texto es: ",contar1)

contar2=Texto.count(Letra2)
print(f"La cantidad de la Segunda letra que digistaste en el texto es: ",contar2)

contar3=Texto.count(Letra3)
print(f"La cantidad de la Tercera letra que digistaste en el texto es: ",contar3)

#cantidad de palabras en un texto
palabra = input("Ingrese su palabra: ").lower()
Lista2=[]
Lista2.append(Texto)
contar4=Texto.count(palabra)
print(f"La cantidad de palabras que digistaste en el texto es: ",contar4)

#cual es la primera letra y ultima de un texto
print(f"la primera letra del texto es: *{Texto[0]}* y la ultima letra es: *{Texto[-1]}*" )

#INVERTIR EL ORDEN DE LAS PALABRAS DE UN TEXTO 
invertir = Texto[::-1]
print(invertir)

#verficar si la palabra python se encuentra
verficar = "python" in Texto
if(verficar==True):
    print("la plabra si existe")
else:
    print("la plabra no existe")