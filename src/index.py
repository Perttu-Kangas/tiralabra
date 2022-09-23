from tkinter import Tk

from services.ui_logic import UILogic
from ui.ui import UI

window = Tk()
window.title("Tiralabra")
window.resizable(False, False)
ui_logic = UILogic()
window.geometry(f"{ui_logic.width}x{ui_logic.height + (ui_logic.grid_size * 2)}")
ui = UI(window, ui_logic)
ui.start()
window.mainloop()
