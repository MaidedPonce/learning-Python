def palindromo():
    frase = input("Ingresa una frase:) : ")
    frase = frase.lower().replace(" ", "")
    frase_al_reves = frase[::-1]
    if frase == frase_al_reves:
        return "Es un palindromo:D"
    else:
        return "No es un palindromo unu"

if __name__ == '__main__':
    run = palindromo()
    print(run)