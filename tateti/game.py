from jugadores import JugadorHumano,JugadorAleatorio,Jugador
import time


class Tateti:
    def __init__(self) :
        self.tablero = [' ' for i in range(9)] # hace el tablero
        self.controlarVictoria = None
    
    def printTablero(self):
        for fila in [self.tablero[ i*3 : (i+1) *3 ] for i in range(3)]:
            print(' | ' + ' | '.join(fila)+ ' |' )
    @staticmethod

    def printNumerosTablero():#indica que numero es cada caja
        numeroTablero= [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for fila in numeroTablero:
            print('| ' + ' | '.join(fila) + ' |')
    
    def movimientosDisponibles(self):
        return [i for i, espacio in enumerate(self.tablero) if espacio == ' ' ]

    def ganador(self, casilla, opcion):

        fila_ind = casilla // 3
        fila = self.tablero[fila_ind*3:(fila_ind+1)*3]
      
        if all([espacio == opcion for espacio in fila]):
            return True

        col_ind = casilla % 3
        column = [self.tablero[col_ind+i*3] for i in range(3)]
     
        if all([espacio == opcion for espacio in column]):
            return True
            
        if casilla % 2 == 0:
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]]
          
            if all([espacio == opcion for espacio in diagonal1]):
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]]
            
            if all([espacio == opcion for espacio in diagonal2]):
                return True
        return False


    def casillasVacias(self):
        return ' ' in self.tablero

    def numeroCasillasVacias(self):
        return self.tablero.count(' ')
    
    def hacerMovimiento(self, casilla, opcion):
        if self.tablero[casilla] == ' ':
            self.tablero[casilla] = opcion

            if self.ganador(casilla, opcion):
                self.controlarVictoria = opcion

            return True
        return False


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.printNumerosTablero()

    opcion = 'X'

    while game.casillasVacias():
        if opcion == 'O':
            casilla = o_player.movimiento(game)
        else:
            
            casilla = x_player.movimiento(game)
            
        
        if game.hacerMovimiento(casilla, opcion):

            if print_game:

                print(opcion + f' se coloca en  {casilla}')
                game.printTablero()
                print('')
            
            if game.controlarVictoria:
                if print_game:
                    print(opcion + ' victoria!')
                return opcion 
            
            opcion = 'O' if opcion == 'X' else 'X' 
        time.sleep(0.8)

    if print_game:
        print('es un empate!')

if __name__ == '__main__':
    x_player = JugadorHumano('X')
    o_player = JugadorAleatorio('O')
    t = Tateti()
    play(t, x_player, o_player, print_game=True)
