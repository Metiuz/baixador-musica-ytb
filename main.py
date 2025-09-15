import customtkinter
from Baixar import Baixar

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Baixador MP3")


        self.url_input = customtkinter.CTkEntry(self, placeholder_text="URL", width=400)
        self.url_input.grid(column=0, row=0, padx=(20,5), pady=20, sticky="E")

        self.button_baixar = customtkinter.CTkButton(self, text="Baixar", command=lambda: Baixar(self.url_input.get()))
        self.button_baixar.grid(column=1, row=0, padx=(5,10), pady=20, sticky="W")


app = App()
app.mainloop()