import tkinter as tk

# Función para agregar datos
def agregar():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)

# Función para limpiar datos
def limpiar():
    seleccionado = lista.curselection()
    if seleccionado:
        lista.delete(seleccionado)
    else:
        lista.delete(0, tk.END)  # Limpia toda la lista si no hay selección

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("300x250")

# Etiqueta y campo de texto
tk.Label(ventana, text="Ingrese información:").pack(pady=5)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botones
tk.Button(ventana, text="Agregar", command=agregar).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=35, height=8)
lista.pack(pady=10)

ventana.mainloop()
