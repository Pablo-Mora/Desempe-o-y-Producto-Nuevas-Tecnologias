import itertools  # Librería para generar IDs únicos

# Generador de IDs únicos
idProductos = itertools.count(1)


helados = []

def switch(ban):
    global helados

    if ban == 1:
        print("➕ AGREGA NUEVO HELADO ➕")
        nameProduct = input("Ingrese el nombre: ")
        description = input("Ingrese la descripción: ")
        value = input("Ingrese el valor unitario: ")

        if value.replace(".", "").isdigit():  # Permitir valores decimales
            helado = {
                'code': next(idProductos),
                'name': nameProduct,
                'description': description,
                'value': float(value)
            }
            helados.append(helado)
            print(f"✅ Producto {nameProduct} agregado correctamente con ID {helado['code']}.")
        else:
            print("⚠️ Error: El precio debe ser un número.")

    elif ban == 2:
        print("❌ ELIMINAR HELADO ❌")
        codeProduct = input("Digite el código: ")

        if codeProduct.isdigit():
            codeProduct = int(codeProduct)
            helado_encontrado = next((h for h in helados if h['code'] == codeProduct), None)

            if helado_encontrado:
                print(f"✅ Helado encontrado: {helado_encontrado['name']}")
                confirm = input("⚠️ ¿Desea eliminar el helado? (yes= 1 / no = 0): ")

                if confirm == "1":
                    helados = [h for h in helados if h['code'] != codeProduct]
                    print("✅ Producto eliminado correctamente.")
                else:
                    print("❌ Cancelado.")
            else:
                print("❌ Error: No se encontró un helado con ese ID.")
        else:
            print("❌ Error: El ID debe ser un número.")

    elif ban == 3:
        print("📖 LISTA DE HELADOS 📖")
        if len(helados) == 0:
            print("⚠️ No hay productos registrados.")
        else:
            for helado in helados:
                print(f"\nID: {helado['code']} | Nombre: {helado['name']} | Descripción: {helado['description']} | Precio: ${helado['value']:.2f}")

    elif ban == 4:
        print("🧾 EDITAR LISTA DE HELADOS 🧾")
        idEdit = input("Ingrese el ID del helado a modificar: ")

        if idEdit.isdigit():
            idEdit = int(idEdit)
            encontrado = False

            for helado in helados:
                if helado['code'] == idEdit:
                    nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
                    nueva_descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ")
                    nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

                    if nuevo_nombre:
                        helado["name"] = nuevo_nombre
                    if nueva_descripcion:
                        helado["description"] = nueva_descripcion
                    if nuevo_precio.replace(".", "").isdigit():
                        helado["value"] = float(nuevo_precio)

                    print("✅ Helado modificado correctamente.")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ Error: No se encontró un helado con ese ID.")
        else:
            print("❌ Error: El ID debe ser un número.")

    elif ban == 5:
        print("👋 Hasta luego, vuelva pronto!")
        return False

    else:
        print("⚠️ Opción no válida, vuelva a intentar.")
    return True 


while True:
    print("\n------ Menú de Opciones ------")
    print("1. Nuevo helado")
    print("2. Eliminar helado")
    print("3. Lista de helados")
    print("4. Editar lista de helados")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        ban = int(opcion)
        if not switch(ban):
            break
    else:
        print("❌ Error: Debe ingresar un número válido.")
