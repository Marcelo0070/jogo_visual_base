screen atualizar_mouse_loop():
    timer 0.01 action Function(atualizar_mouse) repeat True

label before_main_menu:
    show screen atualizar_mouse_loop
    return
    
screen main_menu():
    tag menu
    use parallax_abertura

    frame:
        xalign 0.0
        yalign 0.65
        xoffset 50
        ysize 600
        background None
        has vbox
        spacing 15


        textbutton "Novo Jogo":
            action Start()
            text_style "botao_menu_custom_text"
            background None

        if existe_save_real():
            textbutton "Continuar":
                action Continue()
                text_style "botao_menu_custom_text"
                background None

        textbutton "Carregar Jogo":
            action ShowMenu("load")
            text_style "botao_menu_custom_text"
            background None

        textbutton "Preferências":
            action ShowMenu("preferences")
            text_style "botao_menu_custom_text"
            background None

        textbutton "Galeria":
            action ShowMenu("gallery")
            text_style "botao_menu_custom_text"
            background None

        textbutton "Sair":
            action Quit(confirm=True)
            text_style "botao_menu_custom_text"
            background None

label start:
    $ _preferences.fullscreen = True
    jump introducao
    return

style botao_menu_custom_text is default:
    size 38
    color "#ffffff"
    hover_color "#efff13"
    insensitive_color "#fff45e"
    outlines [(1.2, "#000000", 0, 0)]
    bold True

# Transforms de movimento horizontal (parallax) com velocidades diferentes

transform escala_normal:
    zoom 0.9
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5

transform escala_pessoal:
    zoom 0.75
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5
    
transform tremor_diagonal:
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0 zoom 1.00
    linear 0.6 xoffset 1.2 yoffset -1.2 zoom 1.01
    linear 0.6 xoffset -1.2 yoffset 1.2 zoom 0.99
    repeat

transform tremor_lateral:
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5
    xoffset 0
    linear 0.6 xoffset -2
    linear 0.6 xoffset 0
    repeat

transform galhos_retorcendo:
    anchor (0.5, 0.0)  
    xalign 0.5 yalign 0.5
    rotate 0
    easein 2.5 rotate 0.3
    easeout 2.5 rotate -0.3
    repeat

transform quase_vivo:
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5
    zoom 1.00
    linear 2.5 zoom 1.005
    linear 2.5 zoom 1.000
    repeat

transform folhear_suave:
    anchor (0.5, 0.5)
    xalign 0.5 yalign 0.5
    xzoom 1.0 yzoom 1.0
    linear 2.0 xzoom 1.015 yzoom 0.985
    linear 2.0 xzoom 1.0 yzoom 1.0
    repeat

transform piscar:
    alpha 1.0
    pause 4.5
    linear 0.05 alpha 0.0
    pause 0.2
    linear 0.05 alpha 1.0
    repeat

transform respirando:
    zoom 1.0
    linear 3.0 zoom 1.007
    linear 3.0 zoom 1.0
    repeat

transform mover_fraco_horizontal_t:
    function mover_fraco_horizontal

transform mover_fraco_vertical_t:
    function mover_fraco_vertical

transform mover_medio_horizontal_t:
    function mover_medio_horizontal

transform mover_medio_vertical_t:
    function mover_medio_vertical

transform mover_forte_horizontal_t:
    function mover_forte_horizontal

transform mover_forte_vertical_t:
    function mover_forte_vertical

screen parallax_abertura():

    # Fundo fixo
    add "abertura/abertura_6.png" at escala_normal
    add "abertura/abertura_6.png" at escala_normal, tremor_diagonal alpha 0.22

    # Camadas intermediárias (movimento leve)
    add "abertura/abertura_5.png" at escala_normal
    add "abertura/abertura_5.png" at escala_normal, tremor_lateral alpha 0.35

    add "abertura/abertura_4.png" at escala_normal, mover_fraco_vertical_t, mover_fraco_horizontal_t
    add "abertura/abertura_4.png" at escala_normal, mover_fraco_vertical_t, mover_fraco_horizontal_t, galhos_retorcendo alpha 0.75

    # Personagem próximo (movimento médio)
    add "abertura/abertura_3_piscada.png" at escala_pessoal, respirando
    add "abertura/abertura_3.png" at escala_pessoal, piscar, respirando

    # Camadas mais próximas (movimento mais forte)
    add "abertura/abertura_2.png" at escala_normal, mover_medio_vertical_t, mover_medio_horizontal_t, quase_vivo alpha 1.0

    # Elementos fixos (sem parallax)
    add "abertura/abertura_1,2.png" at escala_normal

    # Camada mais próxima (movimento mais forte)
    add "abertura/abertura_1.png" at escala_normal, mover_forte_horizontal_t, mover_forte_vertical_t
    add "abertura/abertura_1.png" at escala_normal, folhear_suave alpha 1.0
