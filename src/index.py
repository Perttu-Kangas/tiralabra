from tkinter import Tk, ttk, constants, Canvas
from enum import Enum


#
# Ei vielä ole juurikaan dokumentointia, koska tulen vielä refaktoiroimaan
# tämän kokonaan erillisiin luokkiin. Tässä on lähinnä pohja, millä testasin
# piirtotyökalua.


class GridType(Enum):
    """Enum, joka määrittelee """
    NONE = "white"
    WALL = "black"
    START = "blue"
    END = "green"
    VISITED = "gray"


width = 500
height = 200

grid_size = 25
# GRID[y][x] = GridType enum
grid_rows = int(width / grid_size)
grid_cols = int(height / grid_size)
GRID = [[GridType.NONE] * grid_rows] * grid_cols

print(len(GRID), len(GRID[0]))
print(GRID[0])

current_type = GridType.WALL
start_pos = None
end_pos = None


def wall():
    global current_type
    current_type = GridType.WALL


def start():
    global current_type
    current_type = GridType.START


def end():
    global current_type
    current_type = GridType.END


window = Tk()
window.title("Tiralabra")
window.resizable(False, False)
window.geometry(f"{width}x{height}")

frame = ttk.Frame(master=window)
wall_button = ttk.Button(
    master=frame,
    text="Seinä",
    command=wall
)
start_button = ttk.Button(
    master=frame,
    text="Alku",
    command=start
)
end_button = ttk.Button(
    master=frame,
    text="Loppu",
    command=end
)

wall_button.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
start_button.grid(row=0, column=1, sticky=constants.EW, padx=10, pady=10)
end_button.grid(row=0, column=2, sticky=constants.EW, padx=10, pady=10)

frame.pack()


def draw(event):
    global current_type, start_pos, end_pos
    x, y = (event.x // grid_size) * grid_size, (event.y // grid_size) * grid_size - grid_size
    list_x, list_y = int(x / grid_size), int(y / grid_size)

    if current_type == GridType.START:
        if start_pos:
            GRID[start_pos[1]][start_pos[0]] = GridType.NONE
        start_pos = [list_x, list_y]
    elif current_type == GridType.END:
        if end_pos:
            GRID[end_pos[1]][end_pos[0]] = GridType.NONE
        end_pos = [list_x, list_y]

    GRID[list_y][list_x] = current_type

    canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill=str(current_type.value))

    print(GRID[0])


canvas = Canvas(window, width=width, height=height, background=GridType.NONE.value)
canvas.pack(expand=1, fill="both")
canvas.bind("<B1-Motion>", draw)

window.mainloop()
