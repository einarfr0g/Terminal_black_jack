import random
import time
import art  # Módulo externo que contiene un logo.

# Baraja de cartas simulada para Blackjack. El 11 representa un As.
card_deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def hit(card_hand):
    """
    Añade una carta aleatoria de la baraja a la mano dada.
    """
    new_card = random.choice(card_deck)
    card_hand.append(new_card)

def cumsum(li):
    """
    Retorna la suma acumulada de los valores en la lista.
    """
    sum = 0 
    for x in li:
        sum  += x
    return sum

def less_than_21(card_hand):
    """
    Verifica si la suma de la mano es menor o igual a 21.
    """
    result = False
    sum = cumsum(card_hand)
    if sum <= 21 :
        result = True
    else :
        result = False
    return result

def initial_hit(user_hand, crupier_hand):
    """
    Reparte dos cartas a cada jugador (usuario y crupier) al inicio del juego.
    """
    hit(user_hand)
    hit(user_hand)
    hit(crupier_hand)
    hit(crupier_hand)

def si_o_no_loop():
    """
    Bucle que solicita al usuario que responda 'si' o 'no' hasta que lo haga correctamente.
    """
    terminado = False
    respuesta = ""
    while not terminado: 
        respuesta = input("escribe 'si' o 'no':").lower()
        if respuesta == "si" or respuesta == "no":
            terminado = True
        else: 
            print("respuesta no válida, intenta de nuevo")
    return respuesta

def cambiar_once_a_1(user_hand):
    """
    Cambia los valores de As (11) a 1 para evitar pasarse de 21.
    """
    for i in range(len(user_hand)):
        if user_hand[i] == 11:
            user_hand[i] = 1

def quieres_hittear_loop(user_hand, crupier_hand):
    """
    Bucle que pregunta al jugador si quiere pedir otra carta hasta que diga que no
    o hasta que se pase de 21 (después de ajustar los As).
    """
    terminado = False 
    while not terminado:
        print("La mano del crupier es: [" + str(crupier_hand[0]) + ", ■ ]")
        print("Tu mano es: " + str(user_hand))
        print("¿Quieres otra carta?")
        respuesta = si_o_no_loop()
        if respuesta == "si":
            hit(user_hand)
        else:
            terminado = True

        if cumsum(user_hand) > 21:
            cambiar_once_a_1(user_hand)
            if cumsum(user_hand) > 21:
                terminado = True

def juego_del_crupier_loop(user_hand, crupier_hand):
    """
    Lógica del turno del crupier. Este sigue tomando cartas hasta superar al jugador o pasarse de 21.
    """
    print("----------JUEGO DEL CRUPIER----------")
    time.sleep(0.7)
    print("La mano del crupier es: " + str(crupier_hand))
    print("Tu mano es : " + str(user_hand))
    print("--------------------")

    if cumsum(user_hand) <= cumsum(crupier_hand):
        return

    terminado = False
    while not terminado:
        hit(crupier_hand)
        time.sleep(0.7)
        print("La mano del crupier es: " + str(crupier_hand))
        print("Tu mano es : " + str(user_hand))
        print("--------------------")
        if cumsum(crupier_hand) > 21 or cumsum(crupier_hand) >= cumsum(user_hand):
            if cumsum(crupier_hand):
                cambiar_once_a_1(crupier_hand)
                if cumsum(crupier_hand) > 21:
                    terminado = True
            elif cumsum(crupier_hand) >= cumsum(user_hand):
                terminado = True

def perdiste_de_antemano(user_hand):
    """
    Retorna True si el jugador se pasó de 21.
    """
    return cumsum(user_hand) > 21

def quien_gano(user_hand, crupier_hand):
    """
    Determina el resultado del juego:
    - 0: Empate
    - 1: Gana el jugador
    - 2: Gana el crupier
    """
    resultado = -1
    user_hand_sum = cumsum(user_hand)
    crupier_hand_sum = cumsum(crupier_hand)

    if crupier_hand_sum > 21:
        resultado = 1
    elif crupier_hand_sum == user_hand_sum:
        if len(crupier_hand) <= len(user_hand):
            resultado = 0  # Empate
        else:
            resultado = 1  # Gana jugador (menos cartas)
    elif crupier_hand_sum > user_hand_sum:
        resultado = 2  # Gana crupier
    else:
        resultado = 1  # Gana jugador
    return resultado

def print_resultado(resultado):
    """
    Imprime en consola el resultado final del juego.
    """
    if resultado == 0:
        print("-----ES UN EMPATE-----")
    elif resultado == 1:
        print("-----GANASTE-----")
    else:
        print("-----PERDISTE LOOSER-----")

def black_jack_game():
    """
    Función principal del juego de Blackjack. Controla la lógica completa de múltiples partidas.
    """
    terminado = False
    print(art.logo)  # Imprime el logo (debe estar en art.py)
    print("¿quieres jugar?")
    jugar = si_o_no_loop()

    if jugar != "si":
        print("adios")
        return

    while not terminado:
        user_hand = []
        crupier_hand = []
        initial_hit(user_hand, crupier_hand)
        quieres_hittear_loop(user_hand, crupier_hand)

        if less_than_21(user_hand):
            juego_del_crupier_loop(user_hand, crupier_hand)
            print_resultado(quien_gano(user_hand, crupier_hand))
        else:
            print("La mano del crupier es: " + str(crupier_hand))
            print("Tu mano es : " + str(user_hand))
            print_resultado(2)

        print("¿quieres seguir jugando?")
        jugar = si_o_no_loop()
        if jugar != "si":
            terminado = True
        print("----------")

    print("adios")

# Ejecutar el juego
black_jack_game()

