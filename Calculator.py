import tkinter as tk

expresion = ""
expresionAnterior = ""
resultadoMostrar = False
parentesis = 0

def ultimo_numero(expr):
    i = len(expr) - 1

    while i >= 0 and expr[i] == " ":
        i -= 1

    if i >= 0 and expr[i] in "+-*/":
        i -= 1

    fin = i

    while i >= 0 and (expr[i].isdigit() or expr[i] == "."):
        i -= 1

    inicio = i + 1

    return expr[inicio:fin + 1], inicio, fin


def preparacion(expr):
    resultado = ""
    i = 0

    while i < len(expr):

        if expr[i].isdigit():
            inicio = i

            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                i += 1

            numero = expr[inicio:i]

            if i < len(expr) and expr[i] == "%":

                base, ini, fin = ultimo_numero(resultado)

                resultado = (
                    resultado[:ini]
                    + "(" + base + "*" + numero + "/100)"
                )

                i += 1

            else:
                resultado += numero

        elif expr[i] in "+-*/":
            resultado += expr[i]
            i += 1

        elif expr[i] in "()":
            resultado += expr[i]
            i += 1

        else:
            i += 1

    return resultado
            

def button_pressed(valor):
    global expresion, resultadoMostrar, expresionAnterior, parentesis

    # 1. DEL
    if valor == "Del":
        if resultadoMostrar:
            expresion = expresionAnterior[:-1]
        else:
            expresion = expresion[:-1]

        texto_variable.set(expresion)
        resultadoMostrar = False
        return

    # 2. SI VIENE DE RESULTADO
    if resultadoMostrar:
        if valor in "+-*/.":
            resultadoMostrar = False
        else:
            expresion = ""

        resultadoMostrar = False

    # 3. AC
    if valor == "AC":
        expresion = ""
        texto_variable.set(expresion)
        resultadoMostrar = False
        return

    # 4. ()
    if valor == "()":
        if expresion == "" or expresion[-1] in "+-*/(":
            valor = "("
        #SOLO CERRAMOS SI HAY MAS -> (, QUE -> )
        elif expresion.count("(") > expresion.count(")"):
            valor = ")"
        else:
            valor = "(" 

            
    # 5. añadir
    expresion += str(valor)

    # 6. evitar operadores al inicio
    if expresion and expresion[0] in "+-*/.":
        expresion = ""

    texto_variable.set(expresion)

def calcular(expresion):
    expresion = preparacion(expresion)
    resultado = eval(expresion)
    
    if resultado == int(resultado):
        resultado = int(resultado)
    return resultado

def equal_presed():
    global expresion, resultadoMostrar, expresionAnterior
    if expresion == "":
        return
    try:
        expresionAnterior = expresion  
        resultado = calcular(str(expresion))
        expresion = str(resultado)
        resultadoMostrar = True
        texto_variable.set(resultado)
 
    except Exception:
        expresion = ""
        texto_variable.set("Error")


NewWindow = tk.Tk()

NewWindow.title("Calculator")
#NewWindow.iconphoto(False, tk.PhotoImage(file="calculadora.png"))
NewWindow.geometry("400x600")
NewWindow.minsize(400,300)
NewWindow.maxsize(1200,800)
NewWindow.configure(background='white')

for i in range(4):
    NewWindow.grid_columnconfigure(i, weight=1)

for i in range(6):
    NewWindow.grid_rowconfigure(i, weight=1)

texto_variable = tk.StringVar()
entry = tk.Entry(NewWindow, textvariable=texto_variable, font=('Helvetica', 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right', 
    highlightthickness=2, highlightbackground="#1E3A8A", highlightcolor="#9B59B6",)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=6, padx=6)

botones = [
    ("AC", 1, 0), ("()", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("Del", 5, 2)
]

for i in range(len(botones)):
    
    valor = botones[i][0]

    if valor in "*+-/":
        color = "#9B59B6"
        fg = 'white'
    elif valor in "C.":
        color = "#1E3A8A"
        fg = 'white'
    else:
        color = "lightblue"
        fg = "black"

    boton = tk.Button(NewWindow, text=botones[i][0], font=('Helvetica', 20, 'bold'), command= lambda valor = botones[i][0]  : button_pressed(valor), 
        background=color, fg=fg, highlightthickness=3, highlightbackground="#cccccc")
    boton.grid(row=botones[i][1], column=botones[i][2], sticky="nsew", padx=3, pady=3) #sticky=nsew se expande en todas las direcciones, padx y pady espacio entre botones
    #sticky → cuánto del espacio ocupa el botón: n = arriba, s = abajo, e = derecha, w = izquierda. El grid reparte el espacio según weight

botonEqual = tk.Button(NewWindow, text="=", font=('Helvetica', 20, "bold"), command=equal_presed, background="#BDECB6", fg='black', highlightthickness=3, highlightbackground="#cccccc")
botonEqual.grid(row=5, column=3, sticky="nsew", padx=3, pady=3, )

NewWindow.mainloop()