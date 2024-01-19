# Agenda de Contacto
Este programa nos sirve para almacenar datos que pedimos que son nombre, correo, numero celular, telefono fijo, usuario de github.
Que hace

podría gestionar información de contactos, como nombres, teléfono celular, teléfono fijo, correos electrónicos y usuario de github. Podría permitir la adición, modificación y eliminación de contactos, además de buscar y mostrar la lista de contactos.
Como se usa 

primero debes crear una instancia de la clase. Aquí hay un ejemplo simple de cómo podrías hacerlo:

class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        self.contactos[nombre] = {'telefono': telefono, 'correo': correo}

    def mostrar_contactos(self):
        for nombre, info in self.contactos.items():
            print(f'{nombre}: Teléfono - {info["telefono"]}, Correo - {info["correo"]}')

# Crear una instancia de la clase AgendaContactos
mi_agenda = AgendaContactos()

# Agregar contactos
mi_agenda.agregar_contacto('Juan', '123-456-7890', 'juan@email.com')
mi_agenda.agregar_contacto('Maria', '987-654-3210', 'maria@email.com')

# Mostrar la lista de contactos
mi_agenda.mostrar_contactos()