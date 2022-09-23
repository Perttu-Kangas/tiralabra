from tkinter import Tk

from services.ui_logic import UILogic
from ui.main_view import MainView


class UI:
    def __init__(self, root: Tk, ui_logic: UILogic):
        self.root = root
        self.current_view = None
        self.hidden = False
        self.ui_logic = ui_logic

    def start(self):
        """Kutsutaan, kun sovellus käynnistyy.
        Avaa ensiksi päänäkymän.
        """
        self.show_main_view()

    def hide_current_view(self):
        """Tuhoaa tämän hetkisen ikkunan
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_main_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa päänäkymän
        """
        self.hide_current_view()
        self.current_view = MainView(self.root,
                                     self.ui_logic)
        self.current_view.pack()
