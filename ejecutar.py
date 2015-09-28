# -*- encoding: utf-8 -*-
import pilasengine

import escena_menu
import escena_juego

pilas = pilasengine.iniciar()


# Vinculamos las escenas
pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_juego.EscenaJuego)

# Definimos como escena inicial al menú
pilas.escenas.EscenaMenu()

pilas.ejecutar()
