import json

with open('C:/Users/Nicolas/Documents/Code/esp32/Firebase/datos.json', 'r') as datosJson:
    datos = datosJson.read()

objeto = json.loads(datos)

print(json.dumps(objeto, indent=4))

