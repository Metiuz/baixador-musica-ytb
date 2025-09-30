import os
import platform
import shutil


def get_ffmpeg_path():
    """
    Detecta automaticamente o caminho do ffmpeg/ffprobe
    - No Linux/macOS: assume que está no PATH (/usr/bin/ffmpeg etc.)
    - No Windows: tenta procurar ffmpeg.exe/ffprobe.exe na pasta do projeto
    """
    system = platform.system()

    if system in ["Linux", "Darwin"]:  # Linux ou macOS
        if shutil.which("ffmpeg") and shutil.which("ffprobe"):
            return None  # None = deixa yt-dlp usar o ffmpeg do PATH
        else:
            raise FileNotFoundError("ffmpeg não encontrado no PATH. Instale com 'sudo pacman -S ffmpeg'.")

    elif system == "Windows":
        # espera encontrar ffmpeg.exe na mesma pasta do script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ffmpeg_exe = os.path.join(base_dir, "ffmpeg.exe")
        ffprobe_exe = os.path.join(base_dir, "ffprobe.exe")

        if os.path.exists(ffmpeg_exe) and os.path.exists(ffprobe_exe):
            return base_dir  # pasta local onde estão ffmpeg.exe e ffprobe.exe
        else:
            raise FileNotFoundError("ffmpeg.exe/ffprobe.exe não encontrados na pasta do projeto. "
                                    "Baixe em https://www.gyan.dev/ffmpeg/builds/ e coloque ao lado do script.")

    else:
        raise OSError(f"Sistema operacional {system} não suportado automaticamente.")


