# %% [markdown]
# # Agenda de Contactos

# %% [markdown]
# ## Este programa realiza lo siguente:
# -almacena un contacto que debera contener nombre completo, telefon fijo, telefono movil, correo electronico y ususario de github

# %%
class Contacto: # Definicion de la clase Contacto con atributos como nombre telefono fijo telefono movil correo y GitHub.
    def __init__(self, nombre, telefono_fijo, telefono_movil, correo, github):
        self.nombre= nombre
        self.telefono_fijo= telefono_fijo
        self.telefono_movil= telefono_movil
        self.correo= correo
        self.github= github

class AgendaContactos:  # Definicion de la clase AgendaContactos con una lista para almacenar contactos
    def __init__(self): 
        self.Contactos= []
    
    def agrega_contactos(self, Contactos):  # Metodo para agragra un contacto a la lista
        self.Contactos.append(Contactos)

    def mostrar_contactos(self):    # Metado para mostrar la lista de contactos
        for Contactos in self.Contactos:
            print(f"nombre: {Contactos.nombre}")
            print(f"telefono fijo: {Contactos.telefono_fijo}")
            print(f"telefono movil: {Contactos.telefono_movil}")
            print(f"correo electronico: {Contactos.correo}")
            print(f"usuario github: {Contactos.github}")
            print("")
    
    def buscar_por_GitHUb(self, username):  # Metodo para buscar un contacto por el nombre
        for Contacto in self.Contactos:
            if Contacto.nombre == username:
                print("Usuaruio  encontrado:")
                print(f"nombre: {Contacto.nombre}")
                print(f"telefono fijo: {Contacto.telefono_fijo}")
                print(f"telefono movil: {Contacto.telefono_movil}")
                print(f"correo electronico: {Contacto.correo}")
                print(f"usuario github: {Contacto.github}")
                return
            print("Usuario no encontrdo.")


# %%
agenda= AgendaContactos()   # Creacion de una instancia de la clase AgendaContactos
#Creacion de dos instancias de la clase Contacto y agregar a la AGENDA
Contacto1= Contacto("Juan Perez", "5050395820", "5590567459","juan28@gmail.com", "juanGitHub")
Contacto2= Contacto("Maria Lopez", "6890659094", "5625145360","mari8@gmail.com", "mariaGitHub")

agenda.agrega_contactos(Contacto1)
agenda.agrega_contactos(Contacto2)

# %%
print("lista de contactos:")
# Mostrar la lista de contactos en la agenda
agenda.mostrar_contactos()

# %%
username_buscar = "Maria Lopez"
# Solicitar al usuario que ingrese su nombre para buscar
print(f"\n Buscando usuario GitHUb '{username_buscar}':")
#Buscar el usuario por su nombre en la agenda y la mostrar la informacion si se encuentra
agenda.buscar_por_GitHUb(username_buscar)


