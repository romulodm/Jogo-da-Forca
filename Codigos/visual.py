from Graphics import graphics as gf

def forca():
    FORCA = []

    forca_um = gf.Rectangle(gf.Point(75, 280), gf.Point(85, 80))
    forca_um.setFill("#362617") #cor marrom árvore
    forca_um.setOutline("#362617")
    FORCA.append(forca_um)

    forca_dois = gf.Rectangle(gf.Point(75, 80), gf.Point(180, 90))
    forca_dois.setFill("#362617")
    forca_dois.setOutline("#362617")
    FORCA.append(forca_dois)

    forca_tres = gf.Rectangle(gf.Point(175, 80), gf.Point(185, 140))
    forca_tres.setFill("#362617")
    forca_tres.setOutline("#362617")
    FORCA.append(forca_tres)

    forca_quatro = gf.Rectangle(gf.Point(70, 280), gf.Point(90, 300))
    forca_quatro.setFill("#362617")
    forca_quatro.setOutline("#362617")
    FORCA.append(forca_quatro)

    corda_cima = gf.Line(gf.Point(177, 142), gf.Point(183, 142))
    corda_cima.setOutline("burlywood4")
    corda_cima.setWidth(2)
    FORCA.append(corda_cima)

    corda = gf.Line(gf.Point(180, 142), gf.Point(180, 160))
    corda.setOutline("burlywood4")
    corda.setWidth(2)
    FORCA.append(corda)

    corda_pescoco = gf.Oval(gf.Point(175, 161), gf.Point(185, 190))
    corda_pescoco.setOutline("burlywood4")
    corda_pescoco.setWidth(3)
    FORCA.append(corda_pescoco)

    return(FORCA)


def rosto_vivo():
    ROSTO_VIVO = []
    olho_dir = gf.Circle(gf.Point(173, 175), 3)
    olho_dir.setWidth(1)
    ROSTO_VIVO.append(olho_dir)
    olho_esq = gf.Circle(gf.Point(187, 175), 3)
    olho_esq.setWidth(1)
    ROSTO_VIVO.append(olho_esq)
    olho_di = gf.Point(173, 175)
    ROSTO_VIVO.append(olho_di)
    olho_es = gf.Point(187, 175)
    ROSTO_VIVO.append(olho_es)
    boca = gf.Line(gf.Point(176, 190), gf.Point(184, 190))
    boca.setWidth(2)
    ROSTO_VIVO.append(boca)

    return(ROSTO_VIVO)

def rosto_morto():
    ROSTO_MORTO = []
    olho_di = gf.Text(gf.Point(173, 175),f"x")
    ROSTO_MORTO.append(olho_di)
    olho_es = gf.Text(gf.Point(187, 175), f"x")
    ROSTO_MORTO.append(olho_es)
    boca = gf.Text(gf.Point(180, 190), f"o")
    ROSTO_MORTO.append(boca)

    return(ROSTO_MORTO)


def boneco():
    BONECO = []

    outra_corda = gf.Line(gf.Point(176, 204), gf.Point(185, 204))
    outra_corda.setOutline("burlywood4")
    outra_corda.setWidth(4)
    BONECO.append(outra_corda)

    cabeca = gf.Circle(gf.Point(180, 181), 20)
    cabeca.setWidth(3)
    BONECO.append(cabeca)

    corpo = gf.Line(gf.Point(180, 205), gf.Point(180, 250))
    corpo.setWidth(3)
    BONECO.append(corpo)

    braco1 = gf.Line(gf.Point(180, 210), gf.Point(200, 235))
    braco1.setWidth(2)
    BONECO.append(braco1)

    braco2 = gf.Line(gf.Point(180, 210), gf.Point(160, 235))
    braco2.setWidth(2)
    BONECO.append(braco2)

    perna1 = gf.Line(gf.Point(180, 248), gf.Point(200, 278))
    perna1.setWidth(3)
    BONECO.append(perna1)

    perna2 = gf.Line(gf.Point(180, 248), gf.Point(160, 278))
    perna2.setWidth(3)
    BONECO.append(perna2)

    return(BONECO)


def tracos():
    TRACOS = []
    traco1 = gf.Line(gf.Point(220, 300), gf.Point(260, 300))
    traco1.setWidth(2)
    TRACOS.append(traco1)
    traco2 = gf.Line(gf.Point(300, 300), gf.Point(340, 300))
    traco2.setWidth(2)
    TRACOS.append(traco2)
    traco3 = gf.Line(gf.Point(380, 300), gf.Point(420, 300))
    traco3.setWidth(2)
    TRACOS.append(traco3)
    traco4 = gf.Line(gf.Point(460, 300), gf.Point(500, 300))
    traco4.setWidth(2)
    TRACOS.append(traco4)
    traco5 = gf.Line(gf.Point(540, 300), gf.Point(580, 300))
    traco5.setWidth(2)
    TRACOS.append(traco5)
    traco6 = gf.Line(gf.Point(620, 300), gf.Point(660, 300))
    traco6.setWidth(2)
    TRACOS.append(traco6)

    return(TRACOS)

def tentativas(LETRA, POSICAO, ERROS):
    letra = LETRA.upper()

    erro = gf.Text(gf.Point(POSICAO*40, 340),f"{letra}")
    erro.setSize(26)
    erro.setOutline("red")
    erro.setFace("helvetica")
    ERROS.append(erro)

    return(ERROS)

def acertos(NUM, PALAVRA, ACERTOS):

    if NUM == 0:
        acerto = gf.Text(gf.Point(240, 280),f"{PALAVRA[0]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)
    if NUM == 1:
        acerto = gf.Text(gf.Point(320, 280),f"{PALAVRA[1]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)
    if NUM == 2:
        acerto = gf.Text(gf.Point(400, 280),f"{PALAVRA[2]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)
    if NUM == 3:
        acerto = gf.Text(gf.Point(480, 280),f"{PALAVRA[3]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)
    if NUM == 4:
        acerto = gf.Text(gf.Point(560, 280),f"{PALAVRA[4]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)
    if NUM == 5:
        acerto = gf.Text(gf.Point(640, 280),f"{PALAVRA[5]}")
        acerto.setSize(26)
        acerto.setOutline("green")
        acerto.setFace("helvetica")
        ACERTOS.append(acerto)

    return(ACERTOS)


def menu(modo):
    MENU = []

    caixa_sombra = gf.Rectangle(gf.Point(288,83), gf.Point(608, 313))
    caixa_sombra.setWidth(4)
    caixa_sombra.setOutline("#787878")
    MENU.append(caixa_sombra)

    caixa = gf.Rectangle(gf.Point(285,80), gf.Point(605, 310))
    caixa.setWidth(4)
    caixa.setFill("white")
    MENU.append(caixa)

    if modo == "DERROTA":
        titulo_sombra = gf.Text(gf.Point(442,122),"VOCÊ PERDEU!")
        titulo_sombra.setSize(25)
        titulo_sombra.setOutline("#000000")
        titulo_sombra.setFace("helvetica")
        MENU.append(titulo_sombra)
        titulo = gf.Text(gf.Point(440, 120),"VOCÊ PERDEU!")
        titulo.setSize(25)
        titulo.setOutline("burlywood4")
        titulo.setFace("helvetica")
        MENU.append(titulo)
        jogar_sombra = gf.Text(gf.Point(442, 240),"JOGAR NOVAMENTE\n\nSAIR")
        jogar_sombra.setSize(15)
        jogar_sombra.setOutline("#a1a1a1")
        jogar_sombra.setFace("helvetica")
        MENU.append(jogar_sombra)
        jogar = gf.Text(gf.Point(440, 238),"JOGAR NOVAMENTE\n\nSAIR")
        jogar.setSize(15)
        jogar.setOutline("black")
        jogar.setFace("helvetica")
        MENU.append(jogar)

    if modo == "INICIAL":
        titulo_sombra = gf.Text(gf.Point(442,122),"JOGO DA FORCA")
        titulo_sombra.setSize(25)
        titulo_sombra.setOutline("#000000")
        titulo_sombra.setFace("helvetica")
        MENU.append(titulo_sombra)#
        titulo = gf.Text(gf.Point(440, 120),"JOGO DA FORCA")
        titulo.setSize(25)
        titulo.setOutline("burlywood4")
        titulo.setFace("helvetica")
        MENU.append(titulo)
        jogar_sombra = gf.Text(gf.Point(442, 240),"JOGAR\n\nSAIR")
        jogar_sombra.setSize(15)
        jogar_sombra.setOutline("#a1a1a1")
        jogar_sombra.setFace("helvetica")
        MENU.append(jogar_sombra)
        jogar = gf.Text(gf.Point(440, 238),"JOGAR\n\nSAIR")
        jogar.setSize(15)
        jogar.setOutline("black")
        jogar.setFace("helvetica")
        MENU.append(jogar)

    if modo == "VITÓRIA":
        titulo_sombra = gf.Text(gf.Point(442,122),"VOCÊ GANHOU!!!")
        titulo_sombra.setSize(25)
        titulo_sombra.setOutline("#000000")
        titulo_sombra.setFace("helvetica")
        MENU.append(titulo_sombra)
        titulo = gf.Text(gf.Point(440, 120),"VOCÊ GANHOU!!!")
        titulo.setSize(25)
        titulo.setOutline("burlywood4")
        titulo.setFace("helvetica")
        MENU.append(titulo)
        jogar_sombra = gf.Text(gf.Point(442, 240),"JOGAR NOVAMENTE\n\nSAIR")
        jogar_sombra.setSize(15)
        jogar_sombra.setOutline("#a1a1a1")
        jogar_sombra.setFace("helvetica")
        MENU.append(jogar_sombra)
        jogar = gf.Text(gf.Point(440, 238),"JOGAR NOVAMENTE\n\nSAIR")
        jogar.setSize(15)
        jogar.setOutline("black")
        jogar.setFace("helvetica")
        MENU.append(jogar)

    return(MENU)

def dicas(palavra):
    DICA = []
    dica_sombra = gf.Text(gf.Point(442,42),f"{palavra}")
    dica_sombra.setSize(25)
    dica_sombra.setOutline("#000000")
    dica_sombra.setFace("helvetica")
    DICA.append(dica_sombra)
    dica = gf.Text(gf.Point(440, 40),f"{palavra}")
    dica.setSize(25)
    dica.setOutline("burlywood4")
    dica.setFace("helvetica")
    DICA.append(dica)

    return(DICA)

def mostrar_palavra(palavra):
    REVELAR_PALAVRA = []
    palavra_sombra = gf.Text(gf.Point(440.6,160.6),f"A PALAVRA ERA: {palavra}")
    palavra_sombra.setSize(9)
    palavra_sombra.setOutline("#a1a1a1")
    palavra_sombra.setFace("helvetica")
    REVELAR_PALAVRA.append(palavra_sombra)#
    palavra = gf.Text(gf.Point(440, 160),f"A PALAVRA ERA: {palavra}")
    palavra.setSize(9)
    palavra.setOutline("black")
    palavra.setFace("helvetica")
    REVELAR_PALAVRA.append(palavra)#
    sublinhado_sombra = gf.Line(gf.Point(345.6, 172.6), gf.Point(535.6, 172.6))
    sublinhado_sombra.setOutline("#a1a1a1")
    sublinhado_sombra.setWidth(3)
    REVELAR_PALAVRA.append(sublinhado_sombra)#
    sublinhado = gf.Line(gf.Point(345, 172), gf.Point(535, 172))
    sublinhado.setOutline("#556B2F")
    sublinhado.setWidth(3)
    REVELAR_PALAVRA.append(sublinhado)#

    return(REVELAR_PALAVRA)

def seta(modo):
    SETA = []
    if modo == "INICIAL":
        seta = gf.Polygon(gf.Point(380,210),gf.Point(380,220), gf.Point(385,215))
        seta.setFill("black")
        seta.setOutline("black")
        SETA.append(seta)
        linha_seta = gf.Line(gf.Point(375, 215), gf.Point(380, 215))
        linha_seta.setFill("burlywood4")
        linha_seta.setOutline("black")
        linha_seta.setWidth(3)
        SETA.append(linha_seta)
    else:
        seta = gf.Polygon(gf.Point(320,210),gf.Point(320,220), gf.Point(325,215))
        seta.setFill("black")
        seta.setOutline("black")
        SETA.append(seta)
        linha_seta = gf.Line(gf.Point(315, 215), gf.Point(320, 215))
        linha_seta.setFill("burlywood4")
        linha_seta.setOutline("black")
        linha_seta.setWidth(3)
        SETA.append(linha_seta)

    return(SETA)