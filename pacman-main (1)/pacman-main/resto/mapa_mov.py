import pyxel

# Inicialización de Pyxel al principio del programa
pyxel.init(340, 170, title="Pacman", fps=60)

class Pacman:
    def __init__(self, map_instance):
        pyxel.load("pacman.pyxres")  # Suponiendo que contiene el sprite de Pac-Man
        self.x = 17
        self.y = 17
        self.velocidad = 2
        self.direccion = "derecha"
        self.base = 1
        self.sprite_size = 16  # Tamaño del sprite de Pac-Man
        self.map = map_instance  # Pasar la instancia del mapa a Pacman
        pyxel.run(self.update, self.draw)

    # Actualiza las posiciones de Pac-Man con las teclas
    def update(self):
        next_x, next_y = self.x, self.y
        # Mover hacia la izquierda
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            next_x -= self.velocidad
            self.direccion = "izquierda"
            self.base = -1
        # Mover hacia la derecha
        elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            next_x += self.velocidad
            self.direccion = "derecha"
            self.base = 1
        # Mover hacia arriba
        elif pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            next_y -= self.velocidad
            self.direccion = "arriba"
        # Mover hacia abajo
        elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            next_y += self.velocidad
            self.direccion = "abajo"
        # Comprobar colisión antes de actualizar la posición
        if self.check_collision(next_x, next_y):
            self.x, self.y = next_x, next_y

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 0, self.base * 16, 17, 0)

    def check_collision(self, new_x, new_y):
        # Calcular las coordenadas de la celda en la matriz del mapa
        left = new_x // self.map.cell_size
        right = (new_x + self.sprite_size - 1) // self.map.cell_size
        top = new_y // self.map.cell_size
        bottom = (new_y + self.sprite_size - 1) // self.map.cell_size

        # Verificar si alguna esquina de Pacman está dentro de un muro
        return not (
            self.map.mapa[top][left] == 1 or
            self.map.mapa[top][right] == 1 or
            self.map.mapa[bottom][left] == 1 or
            self.map.mapa[bottom][right] == 1
        )


class Map:
    def __init__(self):
        self.width = 340
        self.height = 270
        self.cell_size = 17
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def draw(self):
        for y, row in enumerate(self.mapa):
            for x, cell in enumerate(row):
                screen_x = x * self.cell_size
                screen_y = y * self.cell_size
                if cell == 1:  # Dibujar paredes
                    pyxel.blt(screen_x, screen_y, 1, 0, 0, 17, 17, 0)
                elif cell == 2:  # Dibujar puntos
                    pyxel.circ(screen_x + self.cell_size // 2, screen_y + self.cell_size // 2, 2, 7)


mapita = Map()
Pacman(mapita)