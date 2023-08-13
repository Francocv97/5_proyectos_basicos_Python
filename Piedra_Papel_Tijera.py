import random


def jugar ():
    usuario = input('Escoge una opción: Piedra (pi). Papel (pa). Tijeras (ti).\n').lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'
    
    if ganó_el_jugador(usuario, computadora):
        return 'Ganaste'
    
    return 'Perdiste'

def ganó_el_jugador(jugador, oponente):

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    
print(jugar())
    