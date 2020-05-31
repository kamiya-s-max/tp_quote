import tkinter as tk

from tp_quote import controller as tp_cont
from tp_quote import model as tp_model
from tp_quote import view as tp_view

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.model = tp_model.Model(master)
        self.view = tp_view.View(master, self.model)
        self.controller = tp_cont.Controller(master, self.model, self.view)
        self.view.btn_submit['command'] = self.controller.btn_submit_clicked

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()