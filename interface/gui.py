#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Canvas, Text, Entry, Label, Listbox, TOP, BOTH, END
import bliss_online.bliss_webapp.translation.blisscribe as blisscribe


class BlissApp(tk.Frame):
    WIDTH = 600
    HEIGHT = 400
    LABEL_WIDTH = 20  # 600 / 30

    def __init__(self, master=None, translator=None):
        tk.Frame.__init__(self, master, width=self.WIDTH, height=self.HEIGHT, bg='white')
        self.init_origin()
        self.translator = translator
        self.menu_container = None
        self.lookup_container = None
        self.translate_container = None
        self.bliss_label = None
        self.display_menu()

    def display_menu(self):
        self.clear_grid(keep='menu')
        colspan, rowspan = 3, 3
        self.grid(column=0, row=0, columnspan=colspan, rowspan=rowspan)

        button_w = self.WIDTH // 50
        button_h = self.HEIGHT // 200

        # (width || height) / ([# cells occupied in x || y] * 2)
        xpad = self.WIDTH // 2   # 1*2 = 2
        ypad = self.HEIGHT // 2  # 2*2 = 4

        # (xpad || ypad) - [(button_w || button_h) * ([# cells occupied in x || y] * 4)
        padx = xpad - (button_w * 4)
        pady = ypad - (button_h * 4)

        self.menu_container = tk.Frame(master=self, padx=padx, pady=pady)
        self.menu_container.grid(column=0, row=0, sticky='nsew', columnspan=colspan, rowspan=rowspan)

        self.translate_button = tk.Button(master=self.menu_container, text='translate',
                                          command=self.display_translate,
                                          width=button_w, height=button_h)
        self.translate_button.grid(column=1, row=1)

        self.learn_button = tk.Button(master=self.menu_container, text='lookup',
                                      command=self.display_lookup,
                                      width=button_w, height=button_h)
        self.learn_button.grid(column=1, row=2, pady=10)

    def display_translate(self):
        self.clear_grid(keep='translate')
        colspan, rowspan = 5, 4
        self.grid(column=0, row=0, columnspan=colspan, rowspan=rowspan)
        self.translate_container = tk.Frame(master=self)
        print("Translating!")
        self.translate_container.grid(column=0, row=0, sticky='nsew', columnspan=colspan, rowspan=rowspan)

    def display_lookup(self):
        self.clear_grid(keep='lookup')
        colspan, rowspan = 5, 4
        self.lookup_container = tk.Frame(master=self, padx=10, pady=10)
        # simple Blissymbol lookup:
        # enter a word, pos, & language
        # -> renders Blissymbol for given word, pos & language
        print("Learning!")
        self.lookup_container.grid(column=0, row=0, sticky='nsew', columnspan=colspan, rowspan=rowspan)
        self.text_box_widget(width=10, height=5, master=self.lookup_container)
        self.select_pos_widget(master=self.lookup_container)
        self.select_lang_widget(master=self.lookup_container)
        self.enter_button_widget(master=self.lookup_container)

    # SETUP
    # -----
    def init_origin(self):
        self.master.title("Blisscribe")
        x = (self.winfo_screenwidth()//2) - (self.WIDTH//2)
        y = (self.winfo_screenheight()//2) - (self.HEIGHT//2)
        self.master.geometry('{}x{}+{}+{}'.format(self.WIDTH, self.HEIGHT, x, y))
        self.master.wm_minsize(width=self.WIDTH, height=self.HEIGHT)
        self.grid(column=0, row=0, columnspan=3, rowspan=3)

    def init_translator(self, lang):
        if self.translator is None:
            self.translator = blisscribe.BlissTranslator(lang)

    # WIDGETS
    # =======
    def text_box_widget(self, **kwargs):
        master = kwargs.get('master', self)

        self.word_label = Label(master, font='arial', text=kwargs.get('label_text', 'word'),
                                width=kwargs.get('label_width', None), height=kwargs.get('height', None))
        self.word_label.grid(column=0, row=1)

        self.word_field = Text(self.word_label, '', font='arial',
                               width=kwargs.get('field_width', self.LABEL_WIDTH),
                               height=self.word_label.winfo_height())
        self.word_field.grid(column=1, row=1)

    def select_pos_widget(self, **kwargs):
        master = kwargs.get('master', self)

        label_text = kwargs.get('label_text', 'part of speech')
        self.pos_label = Label(master, font='arial', text=label_text,
                               width=kwargs.get('width', None))
        self.pos_label.grid(column=0, row=2)

        pos_names = blisscribe.POS_KEY.values()
        self.pos_field = Listbox(self.pos_label, width=self.LABEL_WIDTH, height=kwargs.get('height', 10),
                                 selectmode='multiple', exportselection=0)
        self.pos_field.pack()

        for pos in sorted(pos_names):
            self.pos_field.insert(END, pos)

        self.pos_field.grid(column=1, row=2)

    def select_lang_widget(self, **kwargs):
        master = kwargs.get('master', self)

        self.lang_label = Label(master=master, font='arial', text="language")
        self.lang_label.grid(column=0, row=3)
        langs = blisscribe.BlissTranslator.supported_langs()

        self.lang_field = Listbox(master=self.lang_label, width=len(max(langs, key=len)), height=len(langs),
                                  exportselection=0)
        self.lang_field.pack()
        for lang in sorted(langs):
            self.lang_field.insert(END, lang)
        self.lang_field.grid(column=1, row=3)

    def enter_button_widget(self, **kwargs):
        master = kwargs.get('master', self)

        self.enter_button = tk.Button(master=master, text='enter', command=self.render_blissymbol)
        self.enter_button.grid(column=2, row=4)

    def retrieve_input(self, field):
        if type(field) == Text:
            return field.get('1.0', 'end-1c')
        elif type(field) == Listbox:
            return field.curselection()

    def render_blissymbol(self):
        if self.bliss_label is not None:
            self.bliss_label.destroy()

        word = self.retrieve_input(self.word_field)
        height = self.HEIGHT // 3
        blissymbol = None

        if len(word) != 0:
            self.init_translator("English")
            poses = self.retrieve_input(self.pos_field)
            lang = self.retrieve_input(self.lang_field)

            if len(poses) == 0:
                poses = self.translator.token_pos(word, language=lang)
            else:
                pos_codes = sorted(blisscribe.POS_KEY, key=lambda k: blisscribe.POS_KEY[k])
                poses = {pos_codes[idx] for idx in poses}

            lang = sorted(blisscribe.BlissTranslator.supported_langs())[lang[0]] if len(lang) != 0 \
                else self.translator.detect_language(word)
            lang = self.translator.find_lang_code(lang)

            print()
            print("WORD:", word)
            print("POS:", poses)
            print("LANG:", lang)

            synsets = self.translator.word_synsets(word, pos=poses, lang_code=self.translator.find_lang_code(lang))
            print("SYNSETS:", synsets)
            blissymbol = self.translator.synsets_to_blissymbol(synsets)

        if blissymbol is None:
            blissymbol = self.translator.blissword_to_blissymbol("question_mark")

        print("BLISSYMBOL:\n", blissymbol)
        bliss_img = blissymbol.image(max_height=height, white_bg=True)
        fp = blissymbol.bliss_name + ".png"
        bliss_img.save(fp=fp)
        bliss_img = Image.open(fp)
        bliss_imgtk = ImageTk.PhotoImage(Image.open(fp))

        self.bliss_label = Label(self.lookup_container, image=bliss_imgtk,
                                 width=bliss_img.size[0], height=bliss_img.size[1])
        self.bliss_label.image = bliss_imgtk
        self.bliss_label.grid(column=3, row=2)

    def clear_grid(self, keep=None):
        if keep != 'menu' and self.menu_container is not None:
            self.menu_container.destroy()
        if keep != 'lookup' and self.lookup_container is not None:
            self.lookup_container.destroy()
        if keep != 'translate' and self.translate_container is not None:
            self.translate_container.destroy()


app = BlissApp()
app.mainloop()
