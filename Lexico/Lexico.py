import re
from Gram import gramatica
from tkinter import StringVar, ttk

import tkinter
import pandas as pd
window = tkinter.Tk()
pd.set_option("display.max_rows", None, "display.max_columns", None)
window.title("Analizador Lexico")
window.geometry("850x350")
window.configure(background='#D7FF90')
s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="#A1AEFD")
table = ttk.Treeview(window, columns=(
"#1", "#2", "#3"),show='headings') 
table.heading("#1", text="token") 
table.heading("#2", text="valor")
table.heading("#3", text="incidencias")
table.column("#1", width=100)  
table.column("#2", width=150)
table.column("#3", width=100)
table.place(x=450, y=40, height=290)
table.tag_configure('odd', background='#A1DCFD')
table.tag_configure('even', background='#A1FDF0')
def ObtenerCadena():
    table.delete(*table.get_children())
    x= entry.get()
    evaluateLexer(x)
def evaluateLexer(input):
    for i in range(len(gram.reserved)):
        result = re.findall(r""+gram.reserved[i]+"\\b",input)
        # subCadenaIn = input[:result.start()]
        # subCadenaFin = input[result.end():]
        # input = subCadenaIn+subCadenaFin
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('odd'))
        else:
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('even'))
    for i in range(len(gram.simbols)):
        result = re.findall(gram.simbols[i],input)
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i+7],result,len(result)),tags=('even'))
        else:
            table.insert('','end',values=(gram.tokens[i+7],result,len(result)),tags=('odd'))
    divided = input.split()
    ids=[]
    print(f"^{gram.id}")
    for i in range(len(divided)):
        expression = re.compile(f"(\({{1}}{gram.id}\){{1}})|{gram.id}")
        result2 = re.fullmatch(expression, divided[i])
        parentesis = divided[i]
        if(result2!=None):
            if(parentesis[0]=="("):
                substring=parentesis[1:-1]
                ids.append(substring)
            else:
                ids.append(divided[i])
    table.insert('','end',values=("IDS",ids,len(ids)),tags=('odd'))
    denegated = []
    chain=""
    for i in range(len(gram.simbols2)):
        result = re.findall(gram.simbols2[i],input)
        # subCadenaIn = input[:result.start()]
        # subCadenaFin = input[result.end():]
        # input = subCadenaIn+subCadenaFin
        if(len(result)>0):
            for j in range(len(result)):
                chain=chain+result[j]+", "
    print(chain)
    textTitle.set(chain)
        

if __name__ == "__main__":
    gram = gramatica()
    entry = ttk.Entry(window)

    entry.config(width=50)
    # Posicionarla en la ventana.
    entry.place(x=120, y=50)
    textTitle=StringVar()
    texto2 = tkinter.Label(window,text="TOKENS IRRECONOCIDOS:",font=12,background='#D7FF90').place(x=60,y=130) 
    texto1 = tkinter.Label(window,text="",font=12,textvariable= textTitle,background='#D7FF90').place(x=60,y=160) 
    T = tkinter.Text(window, height = 10, width = 52)
    boton = tkinter.Button(text="verificar tokens", command=ObtenerCadena)
    boton.place(x=150, y=90)
    window.mainloop()

