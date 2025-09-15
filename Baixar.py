from yt_dlp import YoutubeDL
import os

diretorio = './media/mp3'

def Baixar(url):
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
        audio_file = f"{diretorio}/{info_dict['title']}.mp3"
    
    if os.path.exists(audio_file):
        print(f"Áudio extraído e salvo como {audio_file}")
    else:
        print("Erro: arquivo MP3 não encontrado!")

