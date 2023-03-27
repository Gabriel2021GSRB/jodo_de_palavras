palavra_secreta = "perfume" # se eu colocar a variavel dentro do while o mesmo zerar a str da variavel.
letras_acertadas = ""

while True:
    letra_digitada = input("Digite uma letra!")

    if len(letra_digitada) > 1: # o função len serve para capturar uma letra
        print("Digigite apenas uma letra!")
        continue

    if letra_digitada in palavra_secreta:    
        letras_acertadas += letra_digitada


    for letra_secreta in palavra_secreta: # sempre que o usuario digitar uma letra certa o sistema vai permanecer quardando a letra.
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print("*") # se o usuario errar a letra o sistema vai exibir o asterisco
            