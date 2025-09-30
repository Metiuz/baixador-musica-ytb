# baixador-musica-ytb
!!! PROJETO EM DESENVOLVIMENTO !!!

 Baixador de música do youtube feito com custom tkinter e yt_dlp.

 Este projeto utiliza o yt-dlp
 para baixar músicas, e ele depende do FFmpeg
 para converter os arquivos de áudio.
É necessário ter o ffmpeg e o ffprobe disponíveis no PATH do sistema.

## Windows

Baixe uma versão compilada do FFmpeg:
 (https://www.gyan.dev/ffmpeg/builds/)

Extraia o .zip.

Copie os arquivos ffmpeg.exe e ffprobe.exe para a pasta do projeto (ao lado do script principal)
ou adicione o caminho deles à variável de ambiente PATH.

Teste no terminal (PowerShell ou CMD):

```ruby
ffmpeg -version
```

## Linux
* Arch Linux / Manjaro
```ruby
sudo pacman -S ffmpeg
```

### Ubuntu / Debian / Linux Mint
```ruby
sudo apt update
sudo apt install ffmpeg
```

### Fedora
```ruby
sudo dnf install ffmpeg ffmpeg-devel
```

### openSUSE
```ruby
sudo zypper install ffmpeg
```


Teste no terminal:

```ruby
ffmpeg -version
```

## macOS
### Homebrew (recomendado)

Se tiver o Homebrew instalado:

```ruby
brew install ffmpeg
```

### Binário manual

Baixe um binário pronto:
 (https://evermeet.cx/ffmpeg/)

Mova para /usr/local/bin:

```ruby
sudo mv ffmpeg /usr/local/bin/
sudo mv ffprobe /usr/local/bin/
chmod +x /usr/local/bin/ffmpeg /usr/local/bin/ffprobe
```


Teste no terminal:

```ruby
ffmpeg -version
```