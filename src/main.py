from tkinter import *
from tkinter import ttk, messagebox, colorchooser, filedialog
from screen import set_screen # import the screen resizing function
from func import *
from discord_webhook import DiscordEmbed
from requests.exceptions import MissingSchema

title = 'Pretenda-bot © | Discord'

BG = '#36393f'
root = Tk()
root.title(title)
set_screen(root, width_ofset=.6)
root.iconbitmap('assets/icon.ico')
root.resizable(False, False)
root.config()

clr = None


def set_color():
    global clr
    color = colorchooser.askcolor()
    if color[1] is not None:
        clr = color[1]
        message.config(bg=color[1])

def clear_color():
    global clr
    clr = None
    message.config(bg='white')

def send_message():
    link = web_hook_urls.get()
    if ',' in link:
            link = link.replace('\n', '').replace(' ', '').split(',')
    hook = Hook(link)
    global clr
    name_ = author.get()
    
    if clr is not None:
        msg = message.get(1.0, END)
        embed = DiscordEmbed(description=msg, color=clr.replace('#', ''))
        try:
            hook.send_embed(embed=embed, username=name_)
            messagebox.showinfo('Sucess', 'Message sent!')
        except MissingSchema:
            messagebox.showerror('Error', 'Invalid WebHook URL')
    else:
        msg = message.get(1.0, END)
        try:
            hook.send_msg(msg, username=name_)
            messagebox.showinfo('Sucess', 'Message sent!')
        except MissingSchema:
            messagebox.showerror('Error', 'Invalid WebHook URL')
    

title_label = ttk.Label(root, text=title.split('|')[0], font=('Arial', 30))
small_label = ttk.Label(root, text='- Become a Discord bot', font=('Arial', 12))
web_hook_urls = ttk.Entry(root, width=80, font=('Cascadia Code', 10))
web_hook_urls_lbl = ttk.Label(root, text='Webhook URLs (separated by commas):', font=('Arial', 10))
message_lbl = ttk.Label(root, text='Message:', font=('Arial', 10))
message = Text(root, height=5, font=('Cascadia Code', 10))
color_lbl = ttk.Label(root, text='Color:', font=('Arial', 10))
color = ttk.Button(root, text='Choose color', command=set_color, width=20)
send_btn = ttk.Button(root, text='Send', command=send_message, width=20)
author_lbl = ttk.Label(root, text='Username:', font=('Arial', 10))
author = ttk.Entry(root, width=80, font=('Cascadia Code', 10))
clr_btn = ttk.Button(root, text='Clear color', command=clear_color, width=20)


web_hook_urls_lbl.grid(row=2, column=0, padx=0, pady=10, sticky=W)
title_label.grid(row=0, column=0, columnspan=2, sticky=W+E, padx=300)
small_label.grid(row=1, column=0, columnspan=2, sticky=W+E, padx=300)
web_hook_urls.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
message_lbl.grid(row=3, column=0, padx=0, pady=10, sticky=E)
message.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
color_lbl.grid(row=4, column=0, padx=0, pady=10, sticky=E)
color.grid(row=4, column=0, columnspan=100, padx=5, )
send_btn.grid(row=7, column=0, columnspan=100, padx=5, pady=5)
author_lbl.grid(row=5, column=0, padx=0, pady=10, sticky=E)
author.grid(row=5, column=1, columnspan=1, padx=5, pady=9)
clr_btn.grid(row=4, column=1, columnspan=1, padx=5, pady=6)



if __name__ == '__main__':
    root.mainloop()
