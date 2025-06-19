# Ejemplo de una Lista
frutas = ["manzana", "banana", "cereza", "manzana"]
print("Lista de frutas:", frutas)
print("Primera fruta (índice 0):", frutas[0])
frutas.append("naranja")  # Agrego un elemento
print("Lista de frutas modificada:", frutas)

print("-" * 20)

# Ejemplo de un Diccionario
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "ingeniera"
}
print("Diccionario de persona:", persona)
print("Nombre de la persona:", persona["nombre"])
persona["edad"] = 31  # Modifico el valor de una clave
persona["estado_civil"] = "soltera"  # Agrego un nuevo par clave-valor
print("Diccionario de persona modificado:", persona)
