import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Marcos
apellido:nuñez
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el valor contenido en la caja de texto (txtSueldo), 
transformarlo a número y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        op_sueldo_txt = self.txt_sueldo.get()
        num = float (op_sueldo_txt)
        porcentaje = num * 0.15
        result = num + porcentaje
        alert(title = "Sueldo", message= f"El incremento de {num} es: {result}")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()