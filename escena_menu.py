# -*- encoding: utf-8 -*-
import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        texto = self.pilas.actores.Texto(u"Menú principal")
        self.pilas.eventos.click_de_mouse.conectar(self._avanzar)

    def _avanzar(self, evento):
        self.pilas.escenas.EscenaJuego()
