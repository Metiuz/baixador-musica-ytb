from yt_dlp import YoutubeDL
import os

diretorio = './media/mp3'

def Baixar(url: str):
    # Configurações do yt-dlp
    ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg")

    options = {
        'format': 'bestaudio/best',  # baixa só o áudio
        'outtmpl': f'{diretorio}/%(title)s.%(ext)s',  # destino do arquivo
        'restrictfilenames': True,
        'postprocessors': [{  # converte para mp3 após baixar
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # qualidade do mp3 (kbps)
        }],
        'ffmpeg_location': ffmpeg_path,  # caminho da pasta onde estão ffmpeg.exe e ffprobe.exe
    }

    # Baixar e converter
    with YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        final_path = ydl.prepare_filename(info_dict)
        final_path = os.path.splitext(final_path)[0] + ".mp3"
        titulo = info_dict.get("title", "Sem título")
    
    if os.path.exists(final_path):
        print(f"Áudio extraído e salvo como {final_path}")
        return titulo
    else:
        print("Erro: arquivo MP3 não encontrado!")
        return None

