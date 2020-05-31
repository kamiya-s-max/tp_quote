import configparser as c
import tkinter as tk


class Model(object):
    def __init__(self, master):
        self.config = c.ConfigParser()
        self.config.read('config.ini')

        self.title = self.config['DISPLAY_INFO']['title']
        self.width = self.config['DISPLAY_INFO']['width']
        self.height = self.config['DISPLAY_INFO']['height']

        self.ent_choice_text = tk.StringVar()
        self.lbl_message_text = tk.StringVar()

    def hello_execute(self):
        self.lbl_message_text.set(f'Hello {self.ent_choice_text.get()}!')