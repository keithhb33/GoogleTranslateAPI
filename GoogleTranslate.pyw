from googletrans import Translator
import tkinter as tk
from tkinter import *
import sys
import os

root = tk.Tk()


def get_box_1_lang(args=None):
    translator = Translator()
    box_1_get = box_1.get()
    translations = translator.translate([box_1_get], dest=variable_2.get())
    for translation in translations:
        translation_text = str(translation.text)
        print(translation.origin, ' -> ', translation.text)
    final_label = Label(root, text=translation_text)
    final_label.pack()


def get_box_2_lang(args=None):
    box_1_lang_get = variable_1.get()
    box_2_lang_get = variable_2.get()
    print(box_1_lang_get)
    print(box_2_lang_get)


def sys_exit(args=None):
    os.execl(sys.executable, sys.executable, *sys.argv)


translate_label = Label(root, text="Google Translate", font=("Courier", 44))
translate_label.pack()

Languages = ["English", "Spanish", "French"]

variable_1 = StringVar(root)
variable_1.set(Languages[0])  # default value

variable_2 = StringVar(root)
variable_2.set(Languages[1])  # default value

box_1_lang = OptionMenu(root, variable_1, *Languages, command=get_box_1_lang)
box_1_lang.pack()
box_1 = Entry(root)
box_1.focus()
box_1.bind('<Return>', get_box_1_lang)
box_1.pack()

box_2_lang = OptionMenu(root, variable_2, *Languages, command=get_box_2_lang)
box_2_lang.pack()

restart = Button(root, text="Clear Translations")
restart.bind('<Button-1>', sys_exit)
restart.pack()

root.mainloop()
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개
