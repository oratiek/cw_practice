import os
import sys
import random
import tkinter as tk
from datetime import datetime


# StringVarで文字を変更する時の注意
# 同じ領域に上書きしているだけなのでサイズが小さいものを重ねると前の表示が残ってしまう。2回目で消えるっぽい。スペースで上書きしても良いかもしれない

# モールス符号を表示するオプションをつけたい

class AlphabetGenerator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("500x500")
        master.title("CW PRACTICE")

        self.display = tk.StringVar(master, "S")
        self.label = tk.Label(self.master, textvariable=self.display, font=("Serif",250))
        self.label.place(x=160,y=100)

        # generator working state
        self.working_state = tk.StringVar(master, "Stopped")
        self.working_state_label = tk.Label(master, textvariable=self.working_state)
        self.working_state_label.place(x=0, y=0)

        self.generator_working = False

        self.alphabets = [chr(i).upper() for i in range(97,97+26)]
        self.current_index = 0
        self.interval = 1000 # millisec

        master.after(self.interval, self.show)

        # add space key control
        master.bind("<Key-space>", self.control_generator)
        master.bind("<Key-r>", self.control_generator)

    def control_generator(self, event): # event need to be specified as args, even if you dont use it.
        if event.keycode == ord("r"): # restart
            self.shuffle()
            self.current_index = 0
        else:
            if self.generator_working:
                self.generator_working = False
                self.working_state.set("Stopped")
            else:
                self.generator_working = True
                self.shuffle()
                self.working_state.set("Working")

    def shuffle(self):
        random.shuffle(self.alphabets)

    def show(self):
        if self.generator_working:
            if self.current_index == 25:
                self.current_index = 0
            self.display.set(self.alphabets[self.current_index])
            self.current_index += 1

        self.master.after(self.interval, self.show)

if __name__ == "__main__":
    win = tk.Tk()
    generator = AlphabetGenerator(master=win)
    generator.mainloop()

