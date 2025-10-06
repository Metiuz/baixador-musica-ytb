import customtkinter
import threading
from Baixar import Baixar

stop_event = threading.Event() #flag de controle global

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Baixador MP3")

        #====== ROW 0 ======
        self.url_input = customtkinter.CTkEntry(self, placeholder_text="URL", width=400)
        self.url_input.grid(column=0, row=0, padx=(25,5), pady=10, sticky="E")

        self.button_baixar = customtkinter.CTkButton(self, text="Baixar", command=self.iniciar_download)
        self.button_baixar.grid(column=1, row=0, padx=(5,25), pady=10, sticky="W")

        #====== ROW 1 ======
        self.output_label = customtkinter.CTkLabel(self, text="", width=400, wraplength=400, justify="left")
        self.output_label.grid(column=0, row=1, padx=(25, 5), pady=(0,0))

        self.button_parar = customtkinter.CTkButton(self, text="Parar", command=self.parar_download)
        self.button_parar.grid(column=1, row=1, padx=(5,25), pady=10, sticky="W")

        #====== ROW 2 ======
        self.historico = []
        self.texthistorico = customtkinter.CTkTextbox(self, width=550, height=300)
        self.texthistorico.grid(column=0, row=2, padx=25, pady=0, columnspan=2)

    # FUNÇÕES
    def render_hist(self, historico:list):
        self.texthistorico.delete("1.0", "end")
        for item in reversed(historico):
            self.texthistorico.insert("end", f"{item}\n")
    
    def baixarSalvarHistorico(self, url:str, output_label: customtkinter.CTkLabel):
        try:
            titulo = Baixar(url, self.progresso_hook)   # recebe o título
            if titulo:             # só adiciona se não for None
                self.historico.append(titulo)
                self.render_hist(self.historico)
            output_label.after(0, lambda: output_label.configure(text="✅ Download concluído!"))
        except Exception as e:
            output_label.after(0, lambda e=e: output_label.configure(text=f"Erro: {e}"))
        

    def iniciar_download(self):
        url = self.url_input.get()
        if not url:
            return
        self.button_baixar.configure(state="disabled")
        self.output_label.configure(text="Baixando...")
        stop_event.clear() # garante que a flag está desligada
        thread = threading.Thread(target=self.baixarSalvarHistorico, args=(url, self.output_label))
        thread.start()
        app.after(1000, self.checar_thread, thread)

    def checar_thread(self, thread:threading.Thread):
        if thread.is_alive():
            app.after(500, self.checar_thread, thread)
        else:
            self.button_baixar.configure(state="normal")

    def progresso_hook(self, d):
        if stop_event.is_set():
            raise Exception("⛔ Download interrompido pelo usuário.")

    def parar_download(self):
        stop_event.set() # ativa o evento de parada



app = App()

if __name__ == "__main__":
    app.mainloop()