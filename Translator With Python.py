import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

language_data = lt.languages()
language_names = [lang['name'] for lang in language_data]
language_code = {lang['name']: lang['code'] for lang in language_data}

app = tk.Tk()
app.geometry('700x400')
app.title("Translator")
app.config(bg="white")

app_name = tk.Label(app, text="Welcome", font="arial 15 bold", bg="white")
app_name.place(x=290, y=0)
#-----------------------------------
#input
input_lable = tk.Label(app,
                       text="Enter Text",
                       font="arial 13 bold",
                       bg="white")
input_lable.place(x=95, y=45)

input_text = tk.Text(app, font="arial 10", height=11, width=30)
input_text.place(x=25, y=100)

input_lang = ttk.Combobox(app, width=19, values=language_names)
input_lang.place(x=65, y=75)
input_lang.set("Choose Input Language")
#-------------------------------------
#output
output_lable = tk.Label(app,
                        text="Enter Text",
                        font="arial 13 bold",
                        bg="white")
output_lable.place(x=490, y=45)

output_text = tk.Text(app, font="arial 10", height=11, width=30)
output_text.place(x=410, y=100)

output_lang = ttk.Combobox(app, width=19, values=language_names)
output_lang.place(x=460, y=75)
output_lang.set("Choose output Language")

#-------------------------------------


#translate button
def Translate():
  try:
    translated_text = lt.translate(input_text.get("1.0", tk.END),
                                   language_code[input_lang.get()],
                                   language_code[output_lang.get()])
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)
  except KeyError as e:
    output_text.insert(tk.END, e)


trans_btn = tk.Button(app,
                      text="Translate",
                      font="arial 10 bold",
                      command=Translate,
                      width=8)
trans_btn.place(x=305, y=180)

#-------------------------------------


#clear button
def Clear():
  input_text.delete("1.0", tk.END)
  output_text.delete("1.0", tk.END)


clear_btn = tk.Button(app,
                      text="Clear",
                      font="arial 10 bold",
                      command=Clear,
                      width=8)
clear_btn.place(x=305, y=220)

app.mainloop()
