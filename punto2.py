frutas = []

# Ingreso de 10 frutas
for i in range(10):
    print(f"Ingrese la fruta {i+1}:")
    nombre = input("Nombre de la fruta: ")
    precio = float(input("Precio de la fruta: "))
    
    frutas.append({"nombre": nombre, "precio": precio})

# Algoritmo de ordenamiento (Bubble short)
for i in range(len(frutas) - 1):
    for j in range(len(frutas) - 1 - i):
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:  # Si el precio es menor, intercambia
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]

print("\n📌 Lista de frutas ordenadas por precio (Mayor a Menor):")
print("=" * 40)
print("{:<15} {:<10}".format("Fruta", "Precio"))
print("=" * 40)

for fruta in frutas:
    print("{:<15} ${:<10.2f}".format(fruta["nombre"], fruta["precio"]))
