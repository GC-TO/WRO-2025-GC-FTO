materias = [
    "Tech IB",          # Informatica Bl - N
    "Bio IB",           # Biologia Bl - NM
    "Fisica",           # CCNN Fisica
    "Edfis",            # Educacion Fisica
    "Eng HL",           # English A IB - HL
    "Sociales",         # Estudios Sociales
    "Hist HL",          # History IB - HL
    "Esp NS",           # Espanola Bl - NS
    "Mat APL",          # Matematica Bl: APL
    "Mono",             # Monografia Bl (EX)
    "Religion",         # Religion
    "SAS",              # SA.S.
    "TOK"               # Teoria del Conocimiento
]

notas = []
print("=== Calculo de Promedio ===")
for m in materias:
    nota = float(input(m + ": "))
    notas.append(nota)

n = len(notas)
promedio = sum(notas) / n
print("\nPromedio actual:", round(promedio, 2))

meta = 8.5
diferencia = meta - promedio

if diferencia <= 0:
    print("Ya tienes 8.5 o mas. Bien hecho!")
else:
    print("\nPara llegar a 8.5, podrias subir una materia:")
    mejor_materia = ""
    menor_subida = 11  # mayor que 10 para comparar

    for i in range(n):
        subida = (meta * n - (sum(notas) - notas[i]))
        if subida <= 10:
            print("- Subiendo", materias[i], "a", round(subida, 2))
            if subida < menor_subida:
                menor_subida = subida
                mejor_materia = materias[i]
        else:
            print("- Subiendo", materias[i], "no es posible (pasa de 10)")

    if mejor_materia != "":
        print("\nLa mejor opcion es subir", mejor_materia, "a", round(menor_subida, 2))

