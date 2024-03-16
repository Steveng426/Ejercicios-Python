#cantidad de letras de un texto
Texto = input("Ingrese su Texto: ").lower()
print(Texto)
Letra1 = input("Digite su primera Letra: ").lower() #.lower sirve para que todo el texto pase a minusculas
Letra2 = input("Digite su segunda Letra: ").lower() #para mayusculas se utiliza .upper()
Letra3 = input("Digite su tercera Letra: ").lower()

Lista1=[] #creo una lista
Lista1.append(Letra1) #con .append() agrego elementos a una lista
Lista1.append(Letra2)
Lista1.append(Letra3)

contar1=Texto.count(Letra1) #.count sirve para contar
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
print(f"la primera letra del texto es: *{Texto[0]}* y la ultima letra es: *{Texto[-1]}*" ) #[0] es la posicion inicial y [-1] para la posicion final

#INVERTIR EL ORDEN DE LAS PALABRAS DE UN TEXTO 
invertir = Texto[::-1] #para invertir las palabas utilizamos [::-1]
print(invertir)

#verficar si la palabra python se encuentra
clave= input("Digite su palabra a buscar:").lower()
verficar = clave in Texto #verficar si una palabra existe en un texto
if(verficar==True):
    print(f"la plabra {clave} si existe")
else:
    print(f"la plabra {clave} no existe")