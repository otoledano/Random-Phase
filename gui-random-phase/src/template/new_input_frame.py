import tkinter as tk

from src.api.dto.dummy_input import DummyInput
from src.service.service import Service


class NewInputFrame(tk.Frame):
    """Frame to create new input files, save them in unfinished states or create them as templates"""

    parent_element = None

    entry_input_name = None
    label_input_name = None

    label_text_field = None
    entry_text_field = None

    button_test = None

    def __init__(self, parent_element):
        super().__init__()
        self.var_input_name = tk.StringVar()
        self.var_text_field = tk.StringVar()
        self.parent_element = parent_element
        self.paint()

    def paint(self):
        self.grid(column=0, row=0, sticky="nsew")
        self.parent_element.grid_rowconfigure(0, weight=1)
        self.parent_element.grid_columnconfigure(0, weight=1)

        # Row One
        self.label_input_name = tk.Label(self)
        self.label_input_name.config(text="Input Name")
        self.label_input_name.grid(row=0, column=0, padx=(30, 0), pady=(10, 3))

        self.entry_input_name = tk.Entry(self, textvariable=self.var_input_name)
        self.entry_input_name.config(width=20)
        self.entry_input_name.grid(row=1, column=0, sticky="", padx=(30, 0), pady=(0, 0))

        # Row Two
        self.label_text_field = tk.Label(self)
        self.label_text_field.config(text="Field 1")
        self.label_text_field.grid(row=2, column=0, padx=(30, 0), pady=(10, 3))

        self.entry_text_field = tk.Entry(self, textvariable=self.var_text_field)
        self.entry_text_field.config(width=20)
        self.entry_text_field.grid(row=3, column=0, padx=(30, 0), pady=(0, 0))

        # Row Three
        self.button_test = tk.Button(self)
        self.button_test.config(text="Test Button", command=self.send_test_data)
        self.button_test.grid(row=4, column=0, padx=(30, 0), pady=(30, 0), ipadx=10, ipady=0, sticky="ew")

    def send_test_data(self):
        service = Service()
        dummy_input = DummyInput()

        dummy_input.input_name = self.var_input_name.get()
        dummy_input.dummy_text = self.var_text_field.get()

        service.create_input_and_run(dummy_input)
