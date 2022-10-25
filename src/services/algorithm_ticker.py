from util.enums import GridType, ResultType
import time


class AlgorithmTicker:

    def __init__(self, ui_logic, grid, algorithm, step_interval=0.025):
        self.ui_logic = ui_logic
        self.grid = grid
        self.algorithm = algorithm

        # Defaults to 25ms
        self.step_interval = step_interval

        self.time_in_ns = 0
        self.visits = 0

    def instant_find(self, times):
        """Suorittaa algoritmin välittömästi.
        Poistaa käytöstä piirtämiset, ja tulostaa keskivertoja
        suorituksista.

        :param times: kuinka monta kertaa algoritmi suoritetaan
        """

        # Reset stat variables
        self.time_in_ns = 0
        self.visits = 0
        self.algorithm.add_visit = self.new_visit
        self.algorithm.draw = None

        current_time = time.time_ns()

        distance = -2
        counter = 0
        while counter < times:

            self.algorithm.init()
            while not self.algorithm.final_path:
                self.algorithm.step()

            self.time_in_ns += time.time_ns() - current_time

            if distance == -2:
                distance = self.get_distance()
            elif distance != self.get_distance():
                print("broken", distance, self.get_distance())
                break

            counter += 1

        print(f"avg: visits={self.visits / times}, time={self.time_in_ns / times * 0.000001}ms")

    def start_ticker(self):
        """Aloittaa algorithmin looppauksen annetulla askelvälillä (def: 25ms)
        Reitti piirretään automaattisesti gridille.
        """

        if self.algorithm.draw:
            # Delete everything unnecessary from grid
            self.reset_grid()

        # Reset stat variables
        self.time_in_ns = 0
        self.visits = 0
        self.algorithm.add_visit = self.new_visit
        self.algorithm.init()

        # Loop till final path is found (or not found)
        while not self.algorithm.final_path:
            current_time = time.time_ns()

            # Make the algorithm take its next step
            self.algorithm.step()

            self.time_in_ns += time.time_ns() - current_time

            # Wait some before starting next step so
            # algorithm can be visualized better
            time.sleep(self.step_interval)

        if self.algorithm.final_path == ResultType.NOT_FOUND:
            return

        if self.algorithm.draw:
            self.draw_path(self.algorithm.final_path[0], GridType.FINAL_PATH)

    def get_time_in_ms(self):
        """
        :return: algoritmin suoritusaika millisekunteina
        """
        return round(self.time_in_ns * 0.000001, 1)

    def get_distance(self):
        """
        :return: algoritmin löytämän reitin pituus
        """
        return self.algorithm.final_path[1] \
            if self.algorithm.final_path and self.algorithm.final_path != ResultType.NOT_FOUND \
            else -1

    def draw_at(self, x, y, grid_type):
        """Piirtää yksittäiseen pisteeseen gridille.

        :param x: x koordinaatti
        :param y: y koordinaatti
        :param grid_type: väri millä piirretään
        """
        self.ui_logic.draw_rectangle(x, y, grid_type)

    def draw_path(self, path, grid_type):
        """Piirtää annetun listan gridille.

        :param path: (x, y) tuple lista piirto koordinaateista
        :param grid_type: väri millä piirretään
        """
        for xy in path:
            self.ui_logic.draw_rectangle(xy[0], xy[1], grid_type)

    def reset_grid(self):
        """Piirtää gridistä kaiken muun pois paitsi aloituspisteen,
        lopetuspisteen ja seinät

        """
        for y in range(len(self.ui_logic.grid)):
            for x in range(len(self.ui_logic.grid[y])):
                self.ui_logic.draw_rectangle(x, y, self.ui_logic.grid[y][x])

    def new_visit(self):
        """Lisää yhden vierailun
        """
        self.visits += 1
