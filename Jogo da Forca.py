from Graphics import graphics as gf
from Codigos import visual as vis

import random as rd

win = gf.GraphWin( "Jogo da Forca" , 720,380)

def main(win):
    win.setBackground("#f4f4e8")

    FORCA = vis.forca()
    for item in FORCA:
        item.draw(win)
    FORCA[-1].undraw()

    BONECO = vis.boneco()
    for item in BONECO:
        item.draw(win) 

    ROSTO = vis.rosto_vivo()
    for item in ROSTO:
        item.draw(win)

    MENU = vis.menu("INICIAL")
    for item in MENU:
        item.draw(win)

    SETA = vis.seta("INCIAL")
    for item in SETA:
        item.draw(win)

    escolha = 0

    done_menu = False
    while not done_menu:
        key = win.getKey()

        if key == "Return" and escolha == 0:
            for item in BONECO:
                item.undraw()
            for item in MENU:
                item.undraw()
            for item in SETA:
                item.undraw()
            for item in ROSTO:
                item.undraw()

            FORCA[-1].draw(win)
            done_menu = True
            jogo(win, FORCA)
            

        if key == "Down" and escolha == 0:
            for item in SETA:
                item.move(0, 47)
            escolha += 1

        if key == "Up" and escolha == 1:
            for item in SETA:
                item.move(0, -47)
            escolha -= 1

        if key == "Return" and escolha == 1:
            done_menu = True
            win.close()

def jogo(win, FORCA):
    #Chamo a função que me retorna uma dica/palavra aleatória:
    ESCOLHA = palavraChoice()

    DICA = ESCOLHA[0]

    DICAVISUAL = vis.dicas(DICA)
    for item in DICAVISUAL:
        item.draw(win)

    PALAVRA = ESCOLHA[1]

    TRACOS = vis.tracos()
    for item in TRACOS:
        item.draw(win)

    BONECO = vis.boneco()
    ERRO = 0

    ACERTOS = []
    ERROS = []
    LETRAS_CHECADAS = []

    done = False
    while not done:

        letra = win.getKey()
        letra = letra.upper()

        if letra not in PALAVRA:
            ERRO += 1

            if ERRO == 1:
                FORCA[-1].undraw()

                BONECO[0].draw(win)
                BONECO[1].draw(win)

                ROSTO = vis.rosto_vivo()
                for item in ROSTO:
                    item.draw(win)

                ERROS = vis.tentativas(letra, 6, ERROS)
                ERROS[0].draw(win)


            if ERRO == 2:
                BONECO[2].draw(win)

                ERROS = vis.tentativas(letra, 8, ERROS)
                ERROS[1].draw(win)

            if ERRO == 3:
                BONECO[3].draw(win)

                ERROS = vis.tentativas(letra, 10, ERROS)
                ERROS[2].draw(win)

            if ERRO == 4:
                BONECO[4].draw(win)

                ERROS = vis.tentativas(letra, 12, ERROS)
                ERROS[3].draw(win)

            if ERRO == 5:
                BONECO[5].draw(win)

                ERROS = vis.tentativas(letra, 14, ERROS)
                ERROS[4].draw(win)

            if ERRO == 6:
                BONECO[6].draw(win)

                ERROS = vis.tentativas(letra, 16, ERROS)
                ERROS[5].draw(win)

                for item in DICAVISUAL:
                    item.undraw()

                for item in TRACOS:
                    item.undraw()

                for item in ERROS:
                    item.undraw()
                
                for item in ACERTOS:
                    item.undraw()

                for item in BONECO:
                    item.undraw()

                for item in FORCA:
                    item.undraw()

                for item in ROSTO:
                    item.undraw()

                done = True
                derrota(win, PALAVRA)

        contador = 0
        if letra not in LETRAS_CHECADAS and letra in PALAVRA:
                while contador < len(PALAVRA):
                    if letra == PALAVRA[contador]:
                        ACERTO = vis.acertos(contador, PALAVRA, ACERTOS)
                        contador += 1

                        if contador < 5 and letra == PALAVRA[contador]:
                            contador -= 1

                        for item in ACERTO:
                            item.undraw()
                            item.draw(win)

                    contador += 1

        LETRAS_CHECADAS.append(str(letra))

        if len(ACERTOS) == 6:
            for item in DICAVISUAL:
                item.undraw()

            for item in TRACOS:
                item.undraw()

            for item in ERROS:
                item.undraw()
            
            for item in ACERTOS:
                item.undraw()

            for item in BONECO:
                item.undraw()

            for item in FORCA:
                item.undraw()

            done = True
            vitoria(win)




def vitoria(win):
    IMAGEM = gf.Image(gf.Point(330, 195), "Imagens/fundo.png")
    IMAGEM.draw(win)

    MENU = vis.menu("VITÓRIA")
    for item in MENU:
        item.draw(win)

    SETA = vis.seta("FINAL")
    for item in SETA:
        item.draw(win)

    escolha = 0

    done_menu = False
    while not done_menu:
        key = win.getKey()

        if key == "Return" and escolha == 0:
            done_menu = True
            for item in MENU:
                item.undraw()

            for item in SETA:
                item.undraw()

            IMAGEM.undraw()

            done_menu = True
            main(win)
            
        if key == "Down" and escolha == 0:
            for item in SETA:
                item.move(0, 47)
            escolha += 1

        if key == "Up" and escolha == 1:
            for item in SETA:
                item.move(0, -47)
            escolha -= 1

        if key == "Return" and escolha == 1:
            done_menu = True
            win.close()




def derrota(win, PALAVRA):
    MENU = vis.menu("DERROTA")
    for item in MENU:
        item.draw(win)     

    REVELAR_PALAVRA = vis.mostrar_palavra(PALAVRA)
    for item in REVELAR_PALAVRA:
        item.draw(win)

    SETA = vis.seta("DERROTA")
    for item in SETA:
        item.draw(win)

    FORCA = vis.forca()
    for item in FORCA:
        item.draw(win)
    FORCA[-1].undraw()

    BONECO = vis.boneco()
    for item in BONECO:
        item.draw(win)

    ROSTO = vis.rosto_morto()
    for item in ROSTO:
        item.draw(win)

    escolha = 0

    done_menu = False
    while not done_menu:
        key = win.getKey()

        if key == "Return" and escolha == 0:
            done_menu = True
            for item in MENU:
                item.undraw()

            for item in SETA:
                item.undraw()

            for item in REVELAR_PALAVRA:
                item.undraw()

            for item in SETA:
                item.undraw()

            for item in FORCA:
                item.undraw()

            for item in BONECO:
                item.undraw()

            for item in ROSTO:
                item.undraw()

            done_menu = True
            main(win)
            
        if key == "Down" and escolha == 0:
            for item in SETA:
                item.move(0, 47)
            escolha += 1

        if key == "Up" and escolha == 1:
            for item in SETA:
                item.move(0, -47)
            escolha -= 1

        if key == "Return" and escolha == 1:
            done_menu = True
            win.close()

def palavraChoice():
    arq = open("Arquivos/palavras.txt", "r", encoding="utf-8")
    conteudo = arq.read()
    arq.close()

    novo_conteudo = conteudo.split("\n")

    num = rd.randint(0, 112)

    escolha_palavra = novo_conteudo[num]
    escolha_palavra = escolha_palavra.split("-")

    palavra = escolha_palavra[1]
    dica = escolha_palavra[0]

    return([dica, palavra])





if __name__ == "__main__":
    main(win)