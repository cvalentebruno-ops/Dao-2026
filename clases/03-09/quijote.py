import re
from collections import Counter

ruta_libro = "./quijote.txt"
ruta_diccionario = "./words_alpha.txt"

# --- LECTURA Y PROCESAMIENTO ---

# Leer el libro y contar frecuencias
with open(ruta_libro, 'r', encoding='utf-8') as f:
    texto_libro = f.read().lower()
    lista_palabras = re.findall(r'\b[a-záéíóúüñ]+\b', texto_libro)
    
    # Contamos cuántas veces aparece cada palabra en todo el texto
    conteo_palabras = Counter(lista_palabras)
    
    # Filtramos SOLO las que tienen frecuencia exacta de 1
    palabras_una_sola_vez = set(palabra for palabra, cantidad in conteo_palabras.items() if cantidad == 1)

# Leer el diccionario
with open(ruta_diccionario, 'r', encoding='utf-8') as f:
    texto_diccionario = f.read().lower()
    palabras_diccionario = set(re.findall(r'\b[a-z]+\b', texto_diccionario))

# --- RESOLUCIÓN DE LOS 4 PUNTOS ---

# 1. Cantidad de palabras que aparecen 1 única vez en el libro
cant_una_vez = len(palabras_una_sola_vez)

# 2. Cantidad de palabras del diccionario
cant_diccionario = len(palabras_diccionario)

# 3. Cantidad de palabras (de las que aparecen 1 vez) que no existen en el diccionario
palabras_no_encontradas = palabras_una_sola_vez - palabras_diccionario
cant_no_encontradas = len(palabras_no_encontradas)

# 4. Listado ordenado de las palabras que no existen
listado_ordenado = sorted(palabras_no_encontradas)


# --- IMPRESIÓN DE RESULTADOS ---
print(f"1. Cantidad de palabras que aparecen solo 1 vez en el libro:", cant_una_vez)
print(f"2. Cantidad de palabras del diccionario: {cant_diccionario}")
print(f"3. Cantidad de estas palabras que NO están en el diccionario: {cant_no_encontradas}")

print("\n4. Listado ordenado (primeras 50):")
print(listado_ordenado[:50])

# Guardar el listado completo en un txt
with open('palabras_no_encontradas.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(listado_ordenado))
print("\nEl listado completo se guardó en 'palabras_no_encontradas.txt'")