import random


def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    return random.choice(palavras)


def exibir_forca(tentativas):
    estagios = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(estagios[tentativas])


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(" ".join(palavra_oculta))
    
    
    while True:
        letra = input("\nDigite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(" ".join(palavra_oculta))
        else:
            tentativas += 1
            exibir_forca(tentativas)
            print(" ".join(palavra_oculta))
        
       
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        
        if tentativas == 6:
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break
    
  
    print("Obrigado por jogar!")


jogar()
