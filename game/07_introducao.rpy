image chuva_animada:
    "cabana/chuva1_2.png"
    0.15
    "cabana/chuva2_2.png"
    0.15
    "cabana/chuva3_2.png" 
    0.15
    "cabana/chuva4_2.png" 
    0.15
    repeat

image fogo_animado:
    "cabana/fogo_3.1.png"
    0.15
    "cabana/fogo_3.2.png" 
    0.15
    "cabana/fogo_3.1.png"
    0.15
    "cabana/fogo_3.2.png" 
    0.15
    repeat

define piscada = Fade(0.2, 0.3, 0.2, color="#000")
define piscada2 = Fade(0.2, 0.5, 1, color="#000")

label introducao:
    # Começa no escuro total
    scene black with dissolve

    filho "..."

    filho "Frio... Molhado... Respirando... lá fora..."

    # Mostra a cabana (imagem olhando da cama para a janela, se tiver)
    show image "cabana/fundo_6.png" at escala_normal 
    # show image "cabana/pernas_5.png" at escala_normal 
    show image "cabana/armario_4.png" at escala_pessoal, galhos_retorcendo 
    show image "cabana/cama_3.png" at escala_pessoal, mover_medio_vertical_t, mover_medio_horizontal_t, quase_vivo
    # show image "cabana/mae_piscando_5.png" at escala_normal, respirando
    # show image "cabana/mae_5.png" at escala_normal, piscar, respirando   
    # show image "cabana/mae_pp_4.png" at escala_normal 
    show image "cabana/fogo_3.png" at escala_normal
    show fogo_animado at escala_normal
    show chuva_animada at escala_normal
    show image "cabana/olho_pp_1.png" at escala_normal 
    show image "cabana/janela_1.png" at escala_normal
    
    with piscada

    hide image "cabana/olho_pp_1.png"
    # hide image "cabana/mae_pp_4.png"

    with piscada2

    mae "Você acordou." 
    mae "Graças..."
    
    "Ela tenta ajeitar um pedaço de pano que te cobre, olhando para suas mãos"

    menu:
            "Perguntar: O que... aconteceu...?":
                "(Ela por um momento olha para a janela.)"
                mae "Você... você estava lá fora... na lama e na chuva... eu te achei..."
                mae "(Engole seco.) Você... não tava... bem..."

            "Perguntar: Onde... onde eu estou...?":
                mae "Em uma cabana."
                mae "Aonde exatamente... estou cuidando disso ainda."
                mae "Mas não se preocupe, assim que passa a chuva vamos para casa."
           
            "Perguntar: Quem... quem é você?":
                "Ela se enrijece por meio segundo... depois lhe dirige um sorriso fraco."
                mae "Eu... sou sua mãe. Claro... sua mãe... Não se lembra?"

            "Ficar em silêncio.":
                "Ela percebe. Baixa a cabeça. Fala quase sussurrando."
                mae "...Tudo bem... não precisa... dizer nada..."

    return

    jump janela

label janela:

    # Sorteia um número aleatório de 1 a 3
    $ criatura = renpy.random.randint(1, 3)

    if criatura == 1:
        "Você vê uma sombra esguia, com olhos vermelhos brilhando no escuro..."
        jump criatura_sombra

    elif criatura == 2:
        "Algo enorme, coberto de musgo, se move lentamente do outro lado da janela..."
        jump criatura_musgo

    else:
        "Um rosto estranho, quase humano, te observa sorrindo..."
        jump criatura_rosto

label criatura_sombra:
    "A sombra some rapidamente..."
    # continua sua história daqui
    return

label criatura_musgo:
    "O monstro de musgo parece ignorar você..."
    # continua daqui
    return

label criatura_rosto:
    "O sorriso daquele rosto não parece amigável..."
    # continua daqui
    return
