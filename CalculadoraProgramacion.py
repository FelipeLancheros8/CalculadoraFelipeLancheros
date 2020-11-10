import tkinter as tk
from tkinter import ttk
from tkinter import *


def init_window():
    window = Tk()
    window.title("Calculadora")
    window.geometry("700x500")

    label = Label(window,text="Calculadora Basica",font=("Arial Black",30))
    label.grid(column=0,row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)



    entrada1.grid(column=1,row=1)
    entrada2.grid(column=1,row=2)



    label_entrada1 = tk.Label(window,text="Ingrese el primer digito:",font=("Berlin Sans FB",15))
    label_entrada1.grid(column=0,row=1)

    label_entrada2 = Label(window,text="Ingrese el segundo digito:",font=("Berlin Sans FB",15))
    label_entrada2.grid(column=0,row=2)

    label_operador = Label(window,text="Escoja el operador:",font=("Berlin Sans FB",15))
    label_operador.grid(column=0,row=3)

    label_bg = Label(window,text="Modo de brillo:",font=("Berlin Sans FB",15))
    label_bg.grid(column=0,row=6)

    combo_operadores= ttk.Combobox(window)
    combo_operadores["Valores"] = ["+","-","*","/","pow"]

    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)
    combo_operadores.config(width="5")

    label_resultado = Label(window,text="Resultado: ",font=("Berlin Sans FB",15))
    label_resultado.grid(column=0,row=4)


    def calcular(num1, num2, operador):
        resultado = 0
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = round(num1 / num2, 2)
        elif operador == "pow":
            resultado = num1 ** num2

        return resultado

    def click_calular(label, num1, num2, operador):
        valor1 = float(num1)
        valor2 = float(num2)

        res = calcular(valor1, valor2, operador)
        label.configure(text="El resultado es: " + str(res))

    boton = Button(window,command = lambda:click_calular(label_resultado,entrada1.get(),entrada2.get(),combo_operadores.get()), text="Calcular",font=("Berlin Sans FB",15))
    boton.grid(column = 1, row= 4)


    def negro():
        window.config(background="black")
    modo1 = Button(window, text='Modo nocturno', value=1,command= lambda:negro())
    def blanco():
        window.config(background="white")
    modo2 = Button(window, text='Modo claro', value=1,command= lambda:blanco())

    modo1.grid(column=1, row=6)
    modo2.grid(column=2, row=6)

    label1 = Label(window, text="Esta aplicacion esta hecha con el proposito de enseñar", font=("Arial Black", 7))
    label1.grid(column=0, row=9)

    def funcion():
        label1.configure(text="Agradecimientos a:" + "\n" + "La profesora Stephanie Torres," + "\n" + "mis compañeros de equipo y" + "\n" + "al sujeto indio que me enseño" + "\n" + " como descargar Tkinter, Pycharm" + "\n" + "y cambiar el fondo de la app")

    boton2 = Button(text="Creditos", command=funcion)
    boton2.grid(column=1, row= 8)

    window.mainloop()
def main():
    init_window()

main ()