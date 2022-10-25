from tkinter import ttk, constants, Canvas, StringVar

from services.ui_logic import UILogic
from util.enums import GridType


class MainView:

    def __init__(self, root, ui_logic: UILogic):
        self.root = root
        self.ui_logic = ui_logic
        self.frame = None
        self.time_var = None
        self.visits_var = None
        self.distance_var = None
        self.canvas = None

        self.initialize()

    def pack(self):
        """Avaa näkymän"""
        self.frame.pack()
        self.canvas.pack()

    def destroy(self):
        """Tuhoaa näkymän"""
        self.frame.destroy()
        self.canvas.destroy()

    def initialize(self):
        """Alustaa näkymän"""
        self.frame = ttk.Frame(master=self.root)

        idastar_button = ttk.Button(
            master=self.frame,
            text="IDA*",
            command=self.ui_logic.start_idastar
        )
        dijkstra_button = ttk.Button(
            master=self.frame,
            text="Dijkstra",
            command=self.ui_logic.start_dijkstra
        )
        reset_button = ttk.Button(
            master=self.frame,
            text="Tyhjennä",
            command=self.ui_logic.reset_grid
        )

        wall_button = ttk.Button(
            master=self.frame,
            text="Seinä",
            command=self.ui_logic.wall_type
        )
        start_button = ttk.Button(
            master=self.frame,
            text="Alku",
            command=self.ui_logic.start_type
        )
        end_button = ttk.Button(
            master=self.frame,
            text="Loppu",
            command=self.ui_logic.end_type
        )

        self.time_var = StringVar()
        self.time_var.set("Aika: 0ms")
        time_label = ttk.Label(master=self.frame, textvariable=self.time_var)

        self.visits_var = StringVar()
        self.visits_var.set("Vierailtu: 0")
        visits_label = ttk.Label(master=self.frame, textvariable=self.visits_var)

        self.distance_var = StringVar()
        self.distance_var.set("Pituus: 0")
        distance_label = ttk.Label(master=self.frame, textvariable=self.distance_var)

        idastar_button.grid(
            row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        dijkstra_button.grid(
            row=0, column=1, sticky=constants.EW, padx=10, pady=10)
        reset_button.grid(
            row=0, column=2, sticky=constants.EW, padx=10, pady=10)

        wall_button.grid(row=1, column=0, sticky=constants.EW,
                         padx=10, pady=10)
        start_button.grid(
            row=1, column=1, sticky=constants.EW, padx=10, pady=10)
        end_button.grid(row=1, column=2, sticky=constants.EW, padx=10, pady=10)

        time_label.grid(row=2, column=0, sticky=constants.EW, padx=10, pady=10)
        visits_label.grid(row=2, column=1, sticky=constants.EW, padx=10, pady=10)
        distance_label.grid(row=2, column=2, sticky=constants.EW, padx=10, pady=10)

        self.canvas = Canvas(self.root, width=self.ui_logic.width, height=self.ui_logic.height,
                             background=str(GridType.NONE.value))

        self.ui_logic.draw_rectangle = self.draw_rectangle
        self.ui_logic.update_stats = self.update_stats

        self.canvas.bind("<B1-Motion>", self.ui_logic.handle_motion)
        self.canvas.bind("<Button-1>", self.ui_logic.handle_motion)

    def draw_rectangle(self, x, y, grid_type):
        """Piirtää suorakulmion annettuihin koordinaatteihin.
        x, y koordinaatit muutetaan canvasiin sopiviksi.

        :param x: x koordinaatti
        :param y: y koordinaatti
        :param grid_type: uusi väri
        """
        canvas_x, canvas_y = self.to_canvas(x), self.to_canvas(y)
        self.canvas.create_rectangle(canvas_x, canvas_y,
                                     canvas_x + self.ui_logic.grid_size,
                                     canvas_y + self.ui_logic.grid_size,
                                     fill=str(grid_type.value))
        self.canvas.update_idletasks()

    def update_stats(self, time, visits, distance):
        """Päivittää näkymän statistiikka variablet

        :param time: uusi aika millisekunteissa
        :param visits: vierailujen määrä
        :param distance: reitin pituus
        """
        self.time_var.set(f"Aika: {time}ms")
        self.visits_var.set(f"Vierailtu: {visits}")
        self.distance_var.set(f"Pituus: {distance}")

    def to_canvas(self, num):
        """Muuttaa annetun koordinaatin canvasiin sopivaksi

        :param num: koordinaatti
        """
        return int(num * self.ui_logic.grid_size)
