import tkinter as tk
from googletrans import Translator

root = tk.Tk()
root.title("Translator")
root.geometry("200x70")

def  translator():
    word = Entry.get()
    translator = Translator(service_url=["translate.google.com"])
    translation = translator.translate(word,dest="fr")
    label1=tk.Label(root,text=f'Translated Word : {translation.text}')
    label1.grid(row=2,column=0)

    label = tk.Label(root,text="Write Here: ")
    label.grid(row=0,column=0)

    entry=tk.Entry(root)
    entry.grid(row=1,column=0)

    button=tk.Button(root,text="Go",command=translator)
    button.grid(row=1,column=1)

    root.mainloop()