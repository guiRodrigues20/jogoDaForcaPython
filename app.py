import random

# Passo 1: Escolher uma Palavra Aleatória
def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    return random.choice(palavras)

# Passo 2: Criar a Função de Exibir a Forca
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

# Passo 3: Iniciar o Jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(" ".join(palavra_oculta))
    
    # Passo 4: Loop Principal do Jogo
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
        
        # Passo 5: Verificação de Vitória e Derrota
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        
        if tentativas == 6:
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break
    
    # Passo 6: Finalização do Jogo
    print("Obrigado por jogar!")

# Executa o jogo
jogar()