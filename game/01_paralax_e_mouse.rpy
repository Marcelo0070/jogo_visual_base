init -2 python:
    mouse_x = 960
    mouse_y = 540

    config.mouse = {
        "default": [("gui/cursor.png", 0, 0)],
    }

    def atualizar_mouse():
        global mouse_x, mouse_y
        mx, my = renpy.get_mouse_pos()
        if mx is not None:
            mouse_x = mx
            mouse_y = my

    config.overlay_screens.append("atualizar_mouse_loop")


init -1 python:

    def mover_fraco_horizontal(trans, st, at):
        mx, _ = renpy.get_mouse_pos()
        dx = max(-15, min(15, (mx - 960) * 0.02))  
        trans.xoffset = dx
        return 0.01

    def mover_fraco_vertical(trans, st, at):
        _, my = renpy.get_mouse_pos()
        dy = max(-10, min(10, (my - 540) * 0.015))
        trans.yoffset = dy
        return 0.01

    def mover_medio_horizontal(trans, st, at):
        mx, _ = renpy.get_mouse_pos()
        dx = max(-30, min(30, (mx - 960) * 0.04))
        trans.xoffset = dx
        return 0.01

    def mover_medio_vertical(trans, st, at):
        _, my = renpy.get_mouse_pos()
        dy = max(-20, min(20, (my - 540) * 0.03))
        trans.yoffset = dy
        return 0.01

    def mover_forte_horizontal(trans, st, at):
        mx, _ = renpy.get_mouse_pos()
        dx = max(-50, min(50, (mx - 960) * 0.06))
        trans.xoffset = dx
        return 0.01

    def mover_forte_vertical(trans, st, at):
        _, my = renpy.get_mouse_pos()
        dy = max(-35, min(35, (my - 540) * 0.045))
        trans.yoffset = dy
        return 0.01

    def atualizar_mouse():
        global mouse_x, mouse_y
        mx, my = renpy.get_mouse_pos()
        if mx is not None:
            mouse_x = mx
            mouse_y = my


    config.overlay_screens.append("atualizar_mouse_loop")

init python:
    import os

    def existe_save_real():
        nomes = ["1-1.save", "1.save", "quicksave.save", "auto-1.save"]
        for nome in nomes:
            try:
                path = renpy.loadable("saves/" + nome)
                if path:
                    return True
            except:
                pass
        return False
