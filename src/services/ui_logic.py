from util.enums import GridType


class UILogic:

    def __init__(self):
        self.draw_rectangle = None

        self.current_type = GridType.WALL
        self.start_position = None
        self.end_position = None

        self.width = 400
        self.height = 400
        self.grid_size = 25

        grid_rows = int(self.width / self.grid_size)
        grid_cols = int(self.height / self.grid_size)

        self.GRID = [[GridType.NONE] * grid_rows] * grid_cols

    def handle_motion(self, event):
        """Käsittelee canvasin motion eventin.
        Päivittää gridin ja canvasin.

        :param event: canvasin motion event
        """
        x, y = self.normalize(event.x), self.normalize(event.y)
        if self.x_out_of_bounds(x) or self.y_out_of_bounds(y):
            return

        if self.current_type == GridType.START:
            if self.start_position:
                self.GRID[self.start_position[1]][self.start_position[0]] = GridType.NONE
                self.draw_rectangle(self.start_position[0], self.start_position[1], GridType.NONE)
            self.start_position = [x, y]
        elif self.current_type == GridType.END:
            if self.end_position:
                self.GRID[self.end_position[1]][self.end_position[0]] = GridType.NONE
                self.draw_rectangle(self.end_position[0], self.end_position[1], GridType.NONE)
            self.end_position = [x, y]

        self.GRID[y][x] = self.current_type
        self.draw_rectangle(x, y, self.current_type)

    def x_out_of_bounds(self, x):
        """Tarkastaa onko x koordinaatti rajojen ulkopuolella

        :param x: x koordinaatti
        :return: True, jos rajojen ulkopuolella
        """
        return x < 0 or x >= len(self.GRID[0])

    def y_out_of_bounds(self, y):
        """Tarkastaa onko y koordinaatti rajojen ulkopuolella

        :param y: y koordinaatti
        :return: True, jos rajojen ulkopuolella
        """
        return y < 0 or y >= len(self.GRID)

    def normalize(self, num):
        """Normalisoi annetun koordinaatin vastaamaan lähintä arvoa gridin koon perusteella

        :param num: normalisoitava koordinaatti
        :return:
        """
        return num // self.grid_size

    def set_draw_rectangle(self, draw_rectangle):
        """Asettaa ui logikaalle metodin, mitä sen pitää kutsua halutessaan piirtää canvasiin

        :param draw_rectangle: piirto metodi, args (x, y, GridType)
        """
        self.draw_rectangle = draw_rectangle

    def wall_type(self):
        """Vaihtaa nykyisen canvasissa käytetyn värin loppupisteen väriin
        """
        self.current_type = GridType.WALL

    def start_type(self):
        """Vaihtaa nykyisen canvasissa käytetyn värin alkupisteen väriin
        """
        self.current_type = GridType.START

    def end_type(self):
        """Vaihtaa nykyisen canvasissa käytetyn värin loppupisteen väriin
        """
        self.current_type = GridType.END
