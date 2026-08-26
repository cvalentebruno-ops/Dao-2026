paises = {
    "AR": "Argentina",
    "BR": "Brasil",
    "CO": "Colombia"
}

donde = input("De donde sos: ")
while donde != "":
    if donde in paises:
        print(paises[donde])
    else:
        print("No conozco ese pais")

    donde = input("De donde sos: ")