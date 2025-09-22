import customtkinter
from Baixar import Baixar

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Baixador MP3")

        #====== ROW 0 ======
        self.url_input = customtkinter.CTkEntry(self, placeholder_text="URL", width=400)
        self.url_input.grid(column=0, row=0, padx=(25,5), pady=10, sticky="E")

        self.button_baixar = customtkinter.CTkButton(self, text="Baixar", command=self.baixar)
        self.button_baixar.grid(column=1, row=0, padx=(5,25), pady=10, sticky="W")

        #====== ROW 1 ======
        self.labelhist = customtkinter.CTkLabel(self, text="Histórico")
        self.labelhist.grid(column=0, row=1, padx=25, pady=(0,0), columnspan=2)

        #====== ROW 2 ======
        self.historico = []
        self.texthistorico = customtkinter.CTkTextbox(self, width=550, height=300)
        self.texthistorico.grid(column=0, row=2, padx=25, pady=0, columnspan=2)

    # FUNÇÕES
    def render_hist(self, historico:list):
        self.texthistorico.delete("1.0", "end")
        for item in reversed(historico):
            self.texthistorico.insert("end", f"{item}\n")
    
    def baixar(self):
        url = self.url_input.get()
        if not url:
            return

        titulo = Baixar(url)   # recebe o título
        if titulo:             # só adiciona se não for None
            self.historico.append(titulo)
            self.render_hist(self.historico)
            self.update()


app = App()

if __name__ == "__main__":
    app.mainloop()