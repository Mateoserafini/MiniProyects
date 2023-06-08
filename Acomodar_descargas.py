import os, shutil

carpetaDescargas = r'C:\Users\Mateo\Downloads'
carpetaImagenes = r'E:\Archivos\Imagenes'
carpetaComprimidos = r'E:\Archivos\Comprimidos'
carpetaDocumentos = r'E:\Archivos\Documentos' 
carpetaMusicaAudios = r'E:\Archivos\Musica o Audios'
carpetaPdf = r'E:\Archivos\PDFs' 
carpertaVideos = r'E:\Archivos\Videos'
carpertaOtros = r'E:\Archivos\Otros'

if not os.path.exists(carpetaImagenes):
    os.mkdir(carpetaImagenes)

if not os.path.exists(carpetaComprimidos):
    os.mkdir(carpetaComprimidos)

if not os.path.exists(carpetaDocumentos):
    os.mkdir(carpetaDocumentos)

if not os.path.exists(carpetaMusicaAudios):
    os.mkdir(carpetaMusicaAudios)

if not os.path.exists(carpetaPdf):
    os.mkdir(carpetaPdf)

if not os.path.exists(carpertaVideos):
    os.mkdir(carpertaVideos)

if not os.path.exists(carpertaOtros):
    os.mkdir(carpertaOtros)

for filename in os.listdir(carpetaDescargas):
    name, extension = os.path.splitext(filename)
    if extension in ['.jpg', '.jpeg', '.png','.JPG','.JPEG']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpetaImagenes, filename))
    elif extension in ['.rar', '.zip', '.7z']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpetaComprimidos, filename))
    elif extension in ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpetaDocumentos, filename))
    elif extension in ['.mp3', '.wav', '.ogg']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpetaMusicaAudios, filename))
    elif extension in ['.pdf']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpetaPdf, filename))
    elif extension in ['.mp4', '.mov', '.avi','.MOV']:
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpertaVideos, filename))
    else: 
        shutil.move(os.path.join(carpetaDescargas, filename), os.path.join(carpertaOtros, filename))




            

