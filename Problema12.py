# Diccionario de extensiones y tipos MIME
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

nombreArchivo = input("Ingrese el nombre del archivo: ")

# Obteniendo la extensión del archivo
_, extension = nombreArchivo.rsplit('.', 1) if '.' in nombreArchivo else (nombreArchivo, '')

# Convirtiendo la extensión a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
extension = extension.lower()

# Obteniendo el tipo MIME correspondiente o 'application/octet-stream' si no se encuentra
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

print(f"Salida Esperada: {tipo_mime}")