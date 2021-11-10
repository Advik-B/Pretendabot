from tkinter import *
from tkinter import ttk, messagebox, colorchooser
from screen import set_screen # import the screen resizing function
from func import *

title = 'Pretenda-bot © | Discord'

root = Tk()
root.title(title)
set_screen(root)
root.iconbitmap('assets/icon.ico')
root.resizable(False, False)

title_label = ttk.Label(root, text=title.split('|')[0].replace('©', ''), font=('Arial', 30))
small_label = ttk.Label(root, text='Become a Discord bot', font=('Arial', 12))
web_hook_urls = ttk.Entry(root, width=80, font=('Cascadia Code', 10))
web_hook_urls_lbl = ttk.Label(root, text='Webhook URLs (separated by commas):', font=('Arial', 10))


web_hook_urls_lbl.grid(row=2, column=0, padx=10, pady=10, sticky=W)
title_label.grid(row=0, column=0, columnspan=2, sticky=W+E, padx=250)
small_label.grid(row=1, column=0, columnspan=2, sticky=W+E, padx=251)
web_hook_urls.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


if __name__ == '__main__':
    root.mainloop()
