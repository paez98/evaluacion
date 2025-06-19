import requests
from bs4 import BeautifulSoup


def extraer_todas_las_frases(base_url):
    todas_las_frases_y_autores = []
    numero_pagina = 1
    hay_siguiente_pagina = True

    while hay_siguiente_pagina:

        if numero_pagina == 1:
            url_actual = base_url
        else:
            url_actual = f"{base_url}page/{numero_pagina}/"

        print(f"Scrapeando página: {url_actual}")

        try:
            response = requests.get(url_actual, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            citas_divs = soup.find_all('div', class_='quote')

            if not citas_divs:
                print(
                    f"No se encontraron citas en la página {numero_pagina}. Deteniendo.")
                hay_siguiente_pagina = False
                break

            for cita_div in citas_divs:
                frase_tag = cita_div.find('span', class_='text')
                autor_tag = cita_div.find('small', class_='author')
                frase = frase_tag.get_text(strip=True) if frase_tag else "N/A"
                autor = autor_tag.get_text(strip=True) if autor_tag else "N/A"
                todas_las_frases_y_autores.append(
                    {"quote": frase, "author": autor})

            next_button = soup.find('li', class_='next')
            if next_button:
                numero_pagina += 1
            else:
                hay_siguiente_pagina = False

        except requests.exceptions.RequestException as e:
            print(
                f"Error al procesar la página {url_actual}: {e}. Deteniendo.")
            hay_siguiente_pagina = False
        except Exception as e:
            print(
                f"Ocurrió un error inesperado al procesar la página {url_actual}: {e}. Deteniendo.")
            hay_siguiente_pagina = False

    return todas_las_frases_y_autores


base_url_quotes = "https://quotes.toscrape.com/"
todas_las_frases = extraer_todas_las_frases(base_url_quotes)

if todas_las_frases:
    print(
        f"--- Se extrajeron un total de {len(todas_las_frases)} frases de todas las páginas ---")

    for i, item in enumerate(todas_las_frases):
        print(f"{i+1}. Frase: {item['quote']} - Autor: {item['author']}")
else:
    print("No se pudieron extraer frases de ninguna página.")
