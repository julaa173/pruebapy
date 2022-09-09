import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

def saludar():
	global saludos
	if saludos == 5 or entrada.get() == "":
		messagebox.showerror(title="Error", message="Error intente nuevanente.")
		# ~ if entrada.get() == "":
			# ~ messagebox.showwarning(title="Alerta", message="Por favor ingrese un nombre")
	else:
		etiqueta.config(text="¡Hola, " + entrada.get() + "!")
		saludos += 1
		lista.insert(tk.END, entrada.get())
		entrada.delete(0, tk.END)
			


saludos = 0

ventana_principal = tk.Tk()
ventana_principal.title("Ejercicio Intregrador")
ventana_principal.config(width=350, height=300)

entrada = ttk.Entry()
entrada.place(x=10, y=20, width=220)

boton = ttk.Button(text="¡Saludar!", command=saludar)
boton.place(x=240, y=20)

etiqueta = ttk.Label()
etiqueta.place(x=10, y=50)

lista = tk.Listbox()
lista.place(x=10, y=80, width=300)

ventana_principal.mainloop()
