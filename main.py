import tweepy
import csv
import time
from datetime import datetime

api_key = 'cYxnTUtY7jc7jvBKKMJ0urpJG'
api_secret = 'x2dTIvaH7rPdjFv9DNhgETmbtq8VMqmJLbnQhjkJ37i2STSram'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGxCZAEAAAAAP4ycP%2BCNA5SSRkztaCNH7mQRQVQ%3DM7mOCjj3jf0cT6ubFYxErCpFaljtbXHhOxbgVHNundMyl1lORv'
acces_token = '1491564956646612993-4LVd9NBDc4aKZ3GjaqN5HZwgpjxEQj'
acces_token_secret = 'h5nmk2BWCbIqxztubU4o2yKCPKlHEpqS5eEiGJdY4IRDS'
# Nos autenticamos en Twitter

auth = tweepy.OAuthHandler("cYxnTUtY7jc7jvBKKMJ0urpJG", "x2dTIvaH7rPdjFv9DNhgETmbtq8VMqmJLbnQhjkJ37i2STSram")
auth.set_access_token("1491564956646612993-4LVd9NBDc4aKZ3GjaqN5HZwgpjxEQj", "h5nmk2BWCbIqxztubU4o2yKCPKlHEpqS5eEiGJdY4IRDS")

# Creamos un objeto de la librería

api = tweepy.API(auth)

#creamos una funcion para tuitear

def Tuitear(message):
    api.update_status(status=message)

#Tuitear('Hola mundo!')




import time
from datetime import datetime

nombre_archivo = 'roman_.csv'
separador = ','

while True:

    with open(nombre_archivo, encoding="utf-8") as archivo:
        next(archivo)
        goles = []
        for linea in archivo:

            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            fecha = columnas[0]
            hora = columnas [1]
            equipo = columnas[2]
            rival = columnas[3]
            minuto = columnas[4]
            parcial = columnas[5]
            fecha_ref = columnas[6]
            goles.append({
                "fecha" : fecha,
                "hora" : hora,
                "equipo" : equipo,
                "rival" : rival,
                "minuto" : minuto,
                "parcial" : parcial,
                "fecha_ref" : fecha_ref,
            })
    
    for elementos in goles:
        hoy = datetime.today()
        hora_hoy = time 
        if elementos['fecha_ref'] == hoy.strftime('%Y-%m-%d') and elementos['hora'] == hoy.strftime('%H:%M:%S'):
            tuit = f"{elementos['fecha']}---{elementos['equipo']} vs {elementos['rival']}---\nGol de Juan Roman Riquelme a los {elementos['minuto']} minutos, pone el partido {elementos['parcial']}"
            Tuitear(tuit)
        else:
        
            print('no match')




