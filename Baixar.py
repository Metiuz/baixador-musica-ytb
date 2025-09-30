from yt_dlp import YoutubeDL
import os
from getPathFile import get_ffmpeg_path 


diretorio = './media/mp3'

def Baixar(url, diretorio=diretorio):
    os.makedirs(diretorio, exist_ok=True)

    ffmpeg_path = get_ffmpeg_path()

    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{diretorio}/%(title)s.%(ext)s',
        'restrictfilenames': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if ffmpeg_path:  # só define explicitamente no Windows
        options['ffmpeg_location'] = ffmpeg_path

    with YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict.get('title', 'arquivo_sem_titulo')

