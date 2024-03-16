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
print(f"La cantidad de la primera letra que digistaste es: ",contar1)

contar2=Texto.count(Letra2)
print(f"La cantidad de la Segunda letra que digistaste es: ",contar2)

contar3=Texto.count(Letra3)
print(f"La cantidad de la Tercera letra que digistaste es: ",contar3)