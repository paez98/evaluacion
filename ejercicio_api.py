import requests


def obtener_tareas_completadas(rangos_id):
    tareas_completadas = []
    for tarea_id in range(rangos_id[0], rangos_id[1] + 1):
        url = f"https://jsonplaceholder.typicode.com/todos/{tarea_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            tarea = response.json()

            if tarea.get('completed'):
                titulo = tarea.get('title')
                id_obtenido = tarea.get('id')
                if titulo:
                    tareas_completadas.append(
                        {'id': id_obtenido, 'title': titulo})
                else:
                    print(
                        f"La tarea {tarea_id} esta completada pero no tiene titulo.")

        except requests.exceptions.RequestException as e:
            print(f"Error al procesar la tarea {tarea_id}: {e}")
        except Exception as e:
            print(
                f"Ocurrió un error inesperado al procesar la tarea {tarea_id}: {e}")

    return tareas_completadas


tarea_inicial = int(input("Ingrese el ID de la primera tarea: "))
tarea_final = int(input("Ingrese el ID de la ultima tarea: "))
rango_de_tareas = (tarea_inicial, tarea_final)

titulos_tareas = obtener_tareas_completadas(rango_de_tareas)

if titulos_tareas:
    print(f"Tareas completadas:{len(titulos_tareas)}")
    for i in titulos_tareas:
        print(f"Tarea ID: {i['id']}, Titulo: {i['title']}")
else:
    print("No se encontraron tareas completadas en el rango especificado.")
