import customtkinter as ctk

app = ctk.CTk()
app.title("Hola Mundo")

label = ctk.CTkLabel(app, text="Hola Mundo")
label.pack()

boton = ctk.CTkButton(app, text="Hola Mundo")
boton.pack()
app.mainloop()