def mostrar_cliente(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")


def agregar_cliente(lista_clientes, nombre):

    # validacion de datos de entrada
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f" Cliente agregado: {nombre.title()}")
    else:
        print(
            "Nombre invalido. El nombre debe tener una longitud mayor a 2 y menor de 50 caracteres"
        )


def modificar_cliente(lista_cliente, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50):
        print(
            "Nombre invalido. El nombre debe tener una longitud mayor a 2 y menor a 50 caracteres"
        )
        return

    if 0 <= indice < len(lista_cliente):
        original = lista_cliente[indice]
        lista_cliente[indice] = nuevo_nombre.title()
        print(
            f"El cliente {original} fue modificado con éxito, Nuevo nombre {nuevo_nombre.title()}"
        )
    else:
        print("Indice fuera de rango...")


def main():
    clientes = ["ana", "jose", "argemiro"]

    print("Clientes actules")
    mostrar_cliente(clientes)

    agregar_cliente(clientes, "emmanuel")
    print("La listas de clientes ctualizada")
    mostrar_cliente(clientes)

    modificar_cliente(clientes, 2, "x")
    print("La lista de clientes actualizada:")
    mostrar_cliente(clientes)


if __name__ == "__main__":
    main()
