a = int(input("1e valeur : "))
b = int(input("2e valeur : "))
c = int(input("3e valeur : "))
d = int(input("4e valeur : "))
e = int(input("5e valeur : "))

# listeNombre = []
#listeNombre.append(int(input("..."))) x 5

listeNombre = [a, b, c, d, e]

numeroDordre = int(input("Position du nombre dont vous voulez déterminer l'accroissement : "))
index1 = numeroDordre - 1
print(listeNombre[index1])

index2 = index1 + 1
tauxAccroissement = ((listeNombre[index2] - listeNombre[index1])/listeNombre[index1] * 100)
tauxAccroissement = round(tauxAccroissement, 2)

#print(f"1e valeur : {listeNombre[index1]}")
#print(f"2e valeur : {listeNombre[index2]} ({tauxAccroissement} %)")

print(f"""1e valeur : {listeNombre[index1]}
2e valeur : {listeNombre[index2]} 
Taux d'accroissement : ({tauxAccroissement} %)""")
