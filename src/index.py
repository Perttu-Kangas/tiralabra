from tkinter import Tk, ttk, constants, Canvas
from enum import Enum


class GridType(Enum):
    NONE = "white"
    WALL = "black"
    START = "blue"
    END = "green"
    VISITED = "gray"


# GRID[x][y] = GridType enum
GRID = []
grid_size = 10

width = 400
height = 400

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

    if current_type == GridType.START:
        if start_pos:
            old_x, old_y = start_pos[0], start_pos[1]
            canvas.create_rectangle(old_x, old_y, old_x + grid_size, old_y + grid_size, fill=GridType.NONE.value,
                                    outline=GridType.NONE.value)
        start_pos = [x, y]
        canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill=str(current_type.value))
    elif current_type == GridType.END:
        if end_pos:
            old_x, old_y = end_pos[0], end_pos[1]
            canvas.create_rectangle(old_x, old_y, old_x + grid_size, old_y + grid_size, fill=GridType.NONE.value,
                                    outline=GridType.NONE.value)
        end_pos = [x, y]
        canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill=str(current_type.value))
    else:
        canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill=str(current_type.value))


canvas = Canvas(window, width=width, height=height, background=GridType.NONE.value)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

window.mainloop()
