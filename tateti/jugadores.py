
import random

class Jugador:
    def __init__(self, opcion):##opcion es X u O
        self.opcion = opcion
    
    def movimiento(self,game):##permite mover al jugador
        pass


class JugadorAleatorio(Jugador):
    def __init__(self, opcion):
        super().__init__(opcion)
    
    def movimiento(self, game):
        casilla = random.choice(game.movimientosDisponibles())
        return casilla

class JugadorHumano(Jugador):
    def __init__(self, opcion):
        super().__init__(opcion)

    def movimiento(self, game):
        casillaValida = False
        val = None
        while not casillaValida:
            casilla=input(self.opcion + ' ingrese posicion  (0,8): ')  
            try:
                val = int(casilla)
                
                if val not in game.movimientosDisponibles():
                    raise ValueError
                casillaValida = True
                
            except ValueError:
                print('casilla invalida, intenta con otra')
        return val
        