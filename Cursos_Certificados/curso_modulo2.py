# Importamos la librería random para colocar las minas en posiciones aleatorias
import random

# --- 1. Crear las matrices --

# Esta matriz guarda las minas (True = hay mina, False = no hay mina)
matriz_minas = [[False for _ in range(8)] for _ in range(8)]

# Esta matriz es la que el jugador ve (al principio está vacía)
matriz_jugador = [[" " for _ in range(8)] for _ in range(8)]


# --- 2. Colocar 10 minas aleatoriamente ---

minas_colocadas = 0
while minas_colocadas < 10:
    fila = random.randint(0, 7)  # Genera un número entre 0 y 7 (porque es 8x8)
    columna = random.randint(0, 7)
    
    # Solo ponemos la mina si no había ya una en esa posición
    if not matriz_minas[fila][columna]:
        matriz_minas[fila][columna] = True
        minas_colocadas += 1


# --- 3. Función para mostrar el tablero al jugador ---

def mostrar_tablero(matriz):
    print("  " + " ".join(str(i) for i in range(8)))  # Números de las columnas arriba
    for idx, fila in enumerate(matriz):
        print(idx, " ".join(fila))  # Número de la fila y contenido de la fila


# --- 4. Función para contar minas cercanas a una casilla ---

def contar_minas_cercanas(fila, columna):
    conteo = 0
    # Revisamos todas las casillas alrededor (incluyendo diagonales)
    for i in range(max(0, fila-1), min(8, fila+2)):
        for j in range(max(0, columna-1), min(8, columna+2)):
            if matriz_minas[i][j]:
                conteo += 1
    return conteo


# --- 5. Funciones principales del juego ---

# Función para destapar una casilla
def destapar(fila, columna):
    if matriz_jugador[fila][columna] != " ":
        # Ya destapada o marcada, no hacemos nada
        print("Esa casilla ya está destapada o marcada.")
        return True

    if matriz_minas[fila][columna]:
        # Si hay una mina, el jugador pierde
        print("¡BOOM! Pisaste una mina. ¡PERDISTE!")
        return False
    else:
        # Si no hay mina, mostramos cuántas minas hay alrededor
        minas_cerca = contar_minas_cercanas(fila, columna)
        matriz_jugador[fila][columna] = str(minas_cerca)
        return True

# Función para marcar una casilla (poner una bandera)
def marcar(fila, columna):
    if matriz_jugador[fila][columna] == " ":
        matriz_jugador[fila][columna] = "⚑"
    else:
        print("No se puede marcar, ya está destapada o marcada.")

# Función para desmarcar una casilla
def desmarcar(fila, columna):
    if matriz_jugador[fila][columna] == "⚑":
        matriz_jugador[fila][columna] = " "
    else:
        print("No hay una marca en esa casilla.")


# --- 6. Función para verificar si el jugador ganó ---

def verificar_ganar():
    for i in range(8):
        for j in range(8):
            if not matriz_minas[i][j] and matriz_jugador[i][j] == " ":
                # Si hay una casilla sin mina y aún no destapada, no ganó
                return False
    return True


# --- 7. Bucle principal del juego ---

juego_terminado = False

print("¡Bienvenido al Buscaminas!")
print("Acciones posibles: destapar, marcar, desmarcar.")

while not juego_terminado:
    mostrar_tablero(matriz_jugador)  # Mostrar tablero actual
    accion = input("¿Qué quieres hacer? (destapar/marcar/desmarcar): ").lower()
    
    # Pedimos fila y columna al jugador
    try:
        fila = int(input("Fila (0-7): "))
        columna = int(input("Columna (0-7): "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    
    # Validar que la fila y columna estén dentro del rango
    if fila < 0 or fila > 7 or columna < 0 or columna > 7:
        print("Fila y columna deben estar entre 0 y 7.")
        continue

    # Dependiendo de la acción, llamamos a la función correcta
    if accion == "destapar":
        juego_terminado = not destapar(fila, columna)
    elif accion == "marcar":
        marcar(fila, columna)
    elif accion == "desmarcar":
        desmarcar(fila, columna)
    else:
        print("Acción no válida.")

    # Después de cada movimiento, verificamos si ganó
    if verificar_ganar():
        mostrar_tablero(matriz_jugador)
        print("¡Felicidades, has destapado todas las casillas sin minas! ¡GANASTE!")
        break

# Fin del juego
print("Juego terminado.")
