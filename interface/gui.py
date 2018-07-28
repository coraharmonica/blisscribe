#!/usr/bin/env python3
import tkinter as tk


class BlissApp(tk.Frame):

    def __init__(self, master=None, translator=None):
        tk.Frame.__init__(self, master)
        self.translator = translator
        self.grid()
        self.intro_screen()

    def intro_screen(self):
        self.translate_button = tk.Button(self, text='Translate', command=self.translate_screen)
        self.translate_button.grid(column=3, row=4)
        self.learn_button = tk.Button(self, text='Learn', command=self.learn_screen)
        self.learn_button.grid(column=3, row=5)
        #self.quit_button = tk.Button(self, text='Q', command=self.quit)
        #self.quit_button.grid(column=5, row=0)

    def translate_screen(self):
        print("Translating!")
        self.translate_button.grid_forget()
        #self.quit()
        return

    def learn_screen(self):
        print("Learning!")
        self.translate_button.grid_forget()
        self.learn_button.grid_forget()
        #self.quit()
        return


app = BlissApp()
app.master.title("Blisscribe")
app.mainloop()
