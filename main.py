import customtkinter
import threading
from Baixar import Baixar



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Baixador MP3")

        self.stop_event = threading.Event() #flag de controle global
        self.download_thread = None

        #====== ROW 0 ======
        self.url_input = customtkinter.CTkEntry(self, placeholder_text="URL", width=400)
        self.url_input.grid(column=0, row=0, padx=(25,5), pady=5, sticky="E")

        self.button_baixar = customtkinter.CTkButton(self, text="Baixar", command=self.iniciar_download)
        self.button_baixar.grid(column=1, row=0, padx=(5,25), pady=5, sticky="W")

        #====== ROW 1 ======
        self.output_label = customtkinter.CTkLabel(self, text="", width=400, wraplength=400, justify="left")
        self.output_label.grid(column=0, row=1, padx=(25, 5), pady=(0,0))

        self.button_parar = customtkinter.CTkButton(self, text="Parar", command=self.parar_download)
        self.button_parar.grid(column=1, row=1, padx=(5,25), pady=5, sticky="W")

        #====== ROW 2 ======
        self.progress_bar = customtkinter.CTkProgressBar(self, width=300)
        self.progress_bar.set(0)
        self.progress_bar.grid(column=0, row=2, padx=25, pady=5, columnspan=2)

        #====== ROW 3 ======
        self.historico = []
        self.texthistorico = customtkinter.CTkTextbox(self, width=550, height=280)
        self.texthistorico.grid(column=0, row=3, padx=25, pady=0, columnspan=2)
        self.texthistorico.configure(state="disabled")

        # Captura o evento de fechamento da janela
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

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
            self.progress_bar.after(0, lambda: self.progress_bar.set(1.0))
        except Exception as e:
            output_label.after(0, lambda e=e: output_label.configure(text=f"{e}"))
        

    def iniciar_download(self):
        url = self.url_input.get()
        if not url:
            return
        self.button_baixar.configure(state="disabled")
        self.output_label.configure(text="Baixando...")
        self.stop_event.clear() # garante que a flag está desligada
        self.progress_bar.set(0)
        self.download_thread = threading.Thread(target=self.baixarSalvarHistorico, args=(url, self.output_label))
        self.download_thread.start()
        app.after(1000, self.checar_thread, self.download_thread)

    def checar_thread(self, thread:threading.Thread):
        if self.download_thread.is_alive():
            app.after(500, self.checar_thread, thread)
        else:
            self.button_baixar.configure(state="normal")

    def progresso_hook(self, d):
        if self.stop_event.is_set():
            raise Exception("⛔ Download interrompido pelo usuário.")
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)

            if total:
                progresso = downloaded / total
                # Atualiza a barra e o texto de forma segura (thread-safe)
                self.progress_bar.after(0, lambda p=progresso: self.progress_bar.set(p))
                percent_str = d.get('_percent_str', '')
                self.output_label.after(0, lambda p=percent_str: self.output_label.configure(text=f"Baixando... {p}"))

        elif d['status'] == 'finished':
            self.output_label.after(0, lambda: self.output_label.configure(text="Processando..."))

    def parar_download(self):
        self.stop_event.set() # ativa o evento de parada

    def on_closing(self):
        """Chamado automaticamente ao fechar a janela."""
        self.stop_event.set()  # sinaliza interrupção

        # Espera um tempo curto para permitir encerramento limpo
        if self.download_thread and self.download_thread.is_alive():
            self.output_label.configure(text="Encerrando thread de download...")
            self.download_thread.join(timeout=2)

        # Agora fecha a janela (e termina o programa)
        self.destroy()

app = App()

if __name__ == "__main__":
    app.mainloop()