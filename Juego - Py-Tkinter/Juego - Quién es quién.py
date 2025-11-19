import tkinter as tk            # Importa de la biblioteca/librería el paquete "Tkinter" (biblioteca gráfica).
from PIL import Image, ImageTk  # Biblioteca para manejar imágenes (para que Tkinter pueda trabajar con imágenes).
import random                   # Importa de la biblioteca/librería el paquete "random" (para selección aleatoria).
import os                       # Importa de la biblioteca/librería el paquete "os" (para manejar rutas de archivos).


# ======================================== RUTAS DE IMÁGENES ========================================
    # Aquí se definen las rutas de las imágenes de los personajes.
ruta_base = os.path.dirname(os.path.abspath(__file__))          # Obtiene la ruta base del archivo actual.


# ======================================== PERSONAJES ========================================
    # Lista para guardar/almacenar los personajes.
personajes = [
    {
        "nombre": "Mariano Rajoy",
        "genero": "Hombre",
        "nacionalidad": "Española",
        "pelo": "Castaño oscuro",
        "ojos": "Marrones",
        "gafas": True,
        "sombrero": False,
        "barba": True,
        "bigote": False,
        "imagen": "Rajoy.png"
    },
    {
        "nombre": "Pedro Sánchez",
        "genero": "Hombre",
        "nacionalidad": "Española",
        "pelo": "Castaño oscuro",
        "ojos": "Marrones oscuros",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Sánchez.png"
    },
    {
        "nombre": "Lionel Andrés Messi",
        "genero": "Hombre",
        "nacionalidad": "Argentina",
        "pelo": "Castaño claro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Messi.png"
    },
    {
        "nombre": "Cristiano Ronaldo",
        "genero": "Hombre",
        "nacionalidad": "Portuguesa",
        "pelo": "Negro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Cristiano.png"
    },
    {
        "nombre": "Adolf Hitler",
        "genero": "Hombre",
        "nacionalidad": "Alemana",
        "pelo": "Negro",
        "ojos": "Azules",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": True,
        "imagen": "Hitler.png"
    },
    {
        "nombre": "Francisco Franco",
        "genero": "Hombre",
        "nacionalidad": "Española",
        "pelo": "Castaño oscuro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": True,
        "imagen": "Franco.png"
    },
    {
        "nombre": "Benito Mussolini",
        "genero": "Hombre",
        "nacionalidad": "Italiana",
        "pelo": False,
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Mussolini.png"
    },
    {
        "nombre": "Mortadelo",
        "genero": "Hombre",
        "nacionalidad": "Española",
        "pelo": False,
        "ojos": "Negros",
        "gafas": True,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Mortadelo.png"
    },
    {
        "nombre": "Filemon",
        "genero": "Hombre",
        "nacionalidad": "Española",
        "pelo": "Negro",
        "ojos": "Negros",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Filemon.png"
    },
    {
        "nombre": "Marie Curie",
        "genero": "Mujer",
        "nacionalidad": "Polaca",
        "pelo": "Castaño oscuro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Curie.png"
    },
    {
        "nombre": "Albert Einstein",
        "genero": "Hombre",
        "nacionalidad": "Alemana",
        "pelo": "Blanco",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": True,
        "imagen": "Einstein.png"
    },
    {
        "nombre": "Giorgia Meloni",
        "genero": "Mujer",
        "nacionalidad": "Italiana",
        "pelo": "Rubio",
        "ojos": "Azul verdosos",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Meloni.png"
    },
    {
        "nombre": "Yayoi Kusama",
        "genero": "Mujer",
        "nacionalidad": "Japonesa",
        "pelo": "Rojo",
        "ojos": "Marrones",
        "gafas": True,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Kusama.png"
    },
    {
        "nombre": "Diego Armando Maradona",
        "genero": "Hombre",
        "nacionalidad": "Argentina",
        "pelo": "Negro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Maradona.png"
    },
    {
        "nombre": "Luis Figo",
        "genero": "Hombre",
        "nacionalidad": "Portuguesa",
        "pelo": "Castaño oscuro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Figo.png"
    },
    {
        "nombre": "Shizuka Minamoto",
        "genero": "Mujer",
        "nacionalidad": "Japonesa",
        "pelo": "Negro",
        "ojos": "Negros",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Shizuka.png"
    },
    {
        "nombre": "Frida Kahlo",
        "genero": "Mujer",
        "nacionalidad": "Mexicana",
        "pelo": "Negro",
        "ojos": "Marrones",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Kahlo.png"
    },
    {
        "nombre": "Sara Garcia Alonso",
        "genero": "Mujer",
        "nacionalidad": "Española",
        "pelo": "Rojo",
        "ojos": "Avellana",
        "gafas": False,
        "sombrero": False,
        "barba": False,
        "bigote": False,
        "imagen": "Sara.png"
    },
]

    # Lista para guardar/almacenar las preguntas cerradas del juego.
categoriaPreguntas = {
    "Género": [
        ("¿Es hombre?", ("genero", "Hombre")),
        ("¿Es mujer?", ("genero", "Mujer")),
    ],
    "Pelo": [
        ("¿Tiene el pelo castaño oscuro?", ("pelo", "Castaño oscuro")),
        ("¿Tiene el pelo castaño claro?", ("pelo", "Castaño claro")),
        ("¿Tiene el pelo negro?", ("pelo", "Negro")),
        ("¿Tiene pelo?", "pelo"), # Para calvos.
        ("¿Tiene el pelo blanco?", ("pelo", "Blanco")),
        ("¿Tiene el pelo rubio?", ("pelo", "Rubio")),
        ("¿Tiene el pelo rojo?", ("pelo", "Rojo")),
    ],
    "Ojos": [
        ("¿Sus ojos son marrones?", ("ojos", "Marrones")),
        ("¿Sus ojos son marrones oscuros?", ("ojos", "Marrones oscuros")),
        ("¿Sus ojos son azules?", ("ojos", "Azules")),
        ("¿Sus ojos son azul verdosos?", ("ojos", "Azul verdosos")),
        ("¿Sus ojos son avellana?", ("ojos", "Avellana")),
    ],
    "Nacionalidad": [
        ("¿Es de nacionalidad española?", ("nacionalidad", "Española")),
        ("¿Es de nacionalidad argentina?", ("nacionalidad", "Argentina")),
        ("¿Es de nacionalidad portuguesa?", ("nacionalidad", "Portuguesa")),
        ("¿Es de nacionalidad alemana?", ("nacionalidad", "Alemana")),
        ("¿Es de nacionalidad italiana?", ("nacionalidad", "Italiana")),
        ("¿Es de nacionalidad polaca?", ("nacionalidad", "Polaca")),
        ("¿Es de nacionalidad japonesa?", ("nacionalidad", "Japonesa")),
        ("¿Es de nacionalidad mexicana?", ("nacionalidad", "Mexicana")),
    ],
    "Accesorios": [
        ("¿Tiene gafas?", "gafas"),
        ("¿Tiene sombrero?", "sombrero"),
    ],
    "Vello facial": [
        ("¿Tiene barba?", "barba"),
        ("¿Tiene bigote?", "bigote"),
    ]
}


# ======================================== CLASE PRINCIPAL DEL JUEGO ========================================
    # Aquí se define la clase principal del juego. Su función es gestionar la lógica y la interfaz del juego.
class QuienEsQuien:
    # Constructor de la clase.
    def __init__(self, root):
        self.root = root
        self.root.title("¿Quién es quién?")

        # Aquí se almacenará el personaje oculto.
        self.personaje_secreto = None

        # Lista para guardar las imágenes y evitar que Python las borre.
        self.imagenes_tk = []

        # Pantalla inicial.
        self.pantalla_inicio()

    # ==================== PANTALLA DE INICIO ====================
        # Método/Función para mostrar la pantalla de inicio.
    def pantalla_inicio(self):
        # Limpia la ventana.
        self.limpiar_ventana()

        # Título del juego.
        tk.Label(self.root, text = "¿Quién es quién?", font = ("Arial", 24)).pack(pady = 20)

        # Botón para iniciar el juego.
        tk.Button(self.root, text = "Jugar", font = ("Arial", 16), command = self.iniciar_juego).pack(pady = 15)

    # ==================== INICIO DEL JUEGO ====================
        # Método/Función para iniciar el juego.
    def iniciar_juego(self):
        # Selecciona un personaje secreto aleatoriamente.
        self.personaje_secreto = random.choice(personajes)

        # Muestra la pantalla principal del juego.
        self.pantalla_juego()

    # ==================== PANTALLA PRINCIPAL ====================
        # Método/Función para mostrar la pantalla principal del juego.
    def pantalla_juego(self):
        # Limpia la ventana.
        self.limpiar_ventana()

        # Título de la sección de preguntas.
        tk.Label(self.root, text = "Selecciona una pregunta:", font = ("Arial", 20)).pack(pady = 10)

        # ========== BOTONES DE PREGUNTAS ==========
            # Método/Función para crear los botones de preguntas.
        frame_preguntas = tk.Frame(self.root)   # Contenedor de botones de preguntas.
        frame_preguntas.pack(pady = 10)         # Contenedor de botones de preguntas.

        # Crea un botón para cada categoría de preguntas.
        for categoriaPreguntas in categoriaPreguntas.keys():
            # Crea el botón y asigna la función de respuesta.
            btn = tk.Button(frame_preguntas, text = categoriaPreguntas, font = ("Arial", 12), command = lambda c = categoriaPreguntas: self.mostrar_subpreguntas(c))  # Crea el botón.
            btn.pack(pady = 4)                                                                                                      # Muestra el botón.

        # Zona de respuesta “Sí/No”.
        self.label_respuesta = tk.Label(self.root, text = "", font = ("Arial", 22)) # Etiqueta para mostrar la respuesta.
        self.label_respuesta.pack(pady = 20)                                        # Muestra la etiqueta.

        # ========== REJILLA DE IMÁGENES DE PERSONAJES ==========
            # Método/Función para crear la rejilla de imágenes de personajes.
        frame_personajes = tk.Frame(self.root)  # Contenedor de la rejilla de personajes.
        frame_personajes.pack(pady = 10)        # Muestra el contenedor.

            # Rejilla de 4 columnas y filas automáticas.
        columnas = 4
        fila = 0
        columna = 0

        # Crea la rejilla de personajes.
        for p in personajes:
            # Carga la imagen desde el archivo.
            ruta_img = os.path.join(ruta_base, "Personajes", p["imagen"])   # Construye la ruta completa a la imagen del personaje.
            img = Image.open(ruta_img)                                      # Abre la imagen desde la ruta "Personajes/".
            img = img.resize((120, 120))                                    # Tamaño fijo.
            img = img.convert("RGBA")                                       # Convierte la imagen a formato RGBA (para transparencia).
            img_tk = ImageTk.PhotoImage(img)                                # Convierte la imagen para Tkinter (para que Tkinter la pueda tratar).

            # Guarda la referencia para evitar que Python las elimine.
            self.imagenes_tk.append(img_tk)

            # Frame individual de cada personaje.
            cont = tk.Frame(frame_personajes)                               # Crea el frame del personaje.
            cont.grid(row = fila, column = columna, padx = 10, pady = 10)   # Posiciona el frame en la rejilla.

            # Imagen del personaje.
            lbl_img = tk.Label(cont, image = img_tk)    # Crea la etiqueta de la imagen.
            lbl_img.pack()                              # Muestra la imagen.

            # Nombre debajo de la imagen.
            tk.Label(cont, text = p["nombre"], font = ("Arial", 12)).pack()

            # Controlar (columnas / filas) de la rejilla.
            columna += 1
            if columna == columnas:
                columna = 0
                fila += 1

        # Botón para adivinar el personaje.
        tk.Button(self.root, text = "Adivinar personaje", font = ("Arial", 14), command = self.pantalla_final).pack(pady = 20)

    # ==================== RESPONDER LA PREGUNTA ====================
        # Método/Función para responder la pregunta seleccionada.
    def responder(self, atributo):
        # Determina la respuesta según el atributo preguntado (atributo simple o atributo compuesto).
        if isinstance(atributo, str):
            # Atributo booleano (atributo simple).
            valor = self.personaje_secreto[atributo]    # Obtiene el valor del atributo.
            respuesta = "Sí" if valor else "No"         # Respuesta según el valor.
        else:
            # Atributo compuesto (clave, valor).
            clave, valor = atributo                                                 # Desempaqueta el atributo.
            respuesta = "Sí" if self.personaje_secreto[clave] == valor else "No"    # Respuesta según el valor.

        # Muestra la respuesta en la etiqueta correspondiente.
        self.label_respuesta.config(text=respuesta)


    # ==================== MOSTRAR SUBPREGUNTAS ====================
        # Método/Función para mostrar las subpreguntas de una categoría.
    def mostrar_subpreguntas(self, categoria):
        # Limpia la ventana para mostrar nuevas preguntas.
        self.limpiar_ventana()

        # Título.
        tk.Label(self.root, text = categoria, font = ("Arial", 20)).pack(pady = 10)

        frame = tk.Frame(self.root) # Contenedor de botones de subpreguntas.
        frame.pack(pady = 10)       # Muestra el contenedor.

        # Generar botones de subpreguntas
        for texto, atributo in categoriaPreguntas[categoria]:
            btn = tk.Button(frame, text = texto, font = ("Arial", 12), command = lambda a = atributo: self.responder(a))    # Crea el botón.
            btn.pack(pady = 4)                                                                                              # Muestra el botón.

        # Botón para volver atrás.
        tk.Button(self.root, text = "Volver", font = ("Arial", 14), command = self.pantalla_juego).pack(pady = 20)

        # Crear rejilla de imágenes de nuevo.
        self.mostrar_rejilla_personajes()

    # ==================== MOSTRAR REJILLA DE PERSONAJES ====================
        # Método/Función para mostrar la rejilla de personajes.
    def mostrar_rejilla_personajes(self):
        # Rejilla de imágenes de personajes.
        frame_personajes = tk.Frame(self.root)  # Contenedor de la rejilla de personajes.
        frame_personajes.pack(pady = 10)        # Muestra el contenedor.

        # Rejilla de 4 columnas y filas automáticas.
        columnas = 4
        fila = 0
        columna = 0

        # Crea la rejilla de personajes.
        for p in personajes:
            # Carga la imagen desde el archivo.
            ruta_img = os.path.join(ruta_base, "Personajes", p["imagen"])   # Construye la ruta completa a la imagen del personaje.
            img = Image.open(ruta_img)                                      # Abre la imagen desde la ruta "Personajes/".
            img = img.resize((120, 120))                                    # Tamaño fijo.
            img_tk = ImageTk.PhotoImage(img)                                # Convierte la imagen para Tkinter (para que Tkinter la pueda tratar).

            # Guarda la referencia para evitar que Python las elimine.
            self.imagenes_tk.append(img_tk)

            # Frame individual de cada personaje.
            cont = tk.Frame(frame_personajes)                            # Crea el frame del personaje.
            cont.grid(row=fila, column = columna, padx = 10, pady = 10)  # Posiciona el frame en la rejilla.

            # Imagen del personaje.
            tk.Label(cont, image = img_tk).pack()                           # Muestra la imagen.
            tk.Label(cont, text = p["nombre"], font = ("Arial", 12)).pack() # Nombre debajo de la imagen.

            # Controlar (columnas / filas) de la rejilla.
            columna += 1
            if columna == columnas: # Controlar cambio de fila al llenar columnas. Si se alcanza el número de columnas, pasa a la siguiente fila.
                columna = 0
                fila += 1

    # ==================== PANTALLA FINAL ====================
        # Método/Función para mostrar la pantalla final del juego.
    def pantalla_final(self):
        # Limpia la ventana.
        self.limpiar_ventana()

        # Muestra el personaje secreto.
        texto = f"¡El personaje secreto era: {self.personaje_secreto['nombre']}!"   # Texto con el nombre del personaje secreto.
        tk.Label(self.root, text = texto, font = ("Arial", 22)).pack(pady = 20)     # Muestra el texto.

        # Muestra la imagen del personaje secreto.
        ruta_img = os.path.join(ruta_base, "Personajes", self.personaje_secreto["imagen"])   # Construye la ruta completa a la imagen del personaje.
        img = Image.open(ruta_img)                                      # Abre la imagen.
        img = img.resize((200, 200))                                    # Tamaño fijo.
        img_tk = ImageTk.PhotoImage(img)                                # Convierte la imagen para Tkinter (para que Tkinter la pueda tratar).

        # Guarda la referencia para evitar que Python las elimine.
        self.imagenes_tk.append(img_tk)

        # Muestra la imagen.
        tk.Label(self.root, image = img_tk).pack(pady = 10)

        # Botón para volver al inicio.
        tk.Button(self.root, text = "Volver al inicio", font = ("Arial", 14), command = self.pantalla_inicio).pack(pady = 20)

    # ==================== LIMPIAR VENTANA ====================
        # Método/Función para limpiar la ventana en caso de reinicio o cambio de pantalla.
    def limpiar_ventana(self):
        # Elimina todos los widgets de la ventana.
        for widget in self.root.winfo_children():
            widget.destroy()


# ======================================== EJECUCIÓN DEL PROGRAMA ========================================
    # Aquí se ejecuta el programa llamando a crear la ventana principal y la instancia del juego.
root = tk.Tk()              # Crea la ventana principal.
app = QuienEsQuien(root)    # Crea una instancia de la clase del juego.
root.mainloop()             # Inicia el bucle principal de la interfaz gráfica.