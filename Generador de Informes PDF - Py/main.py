# Interfaz gráfica de usuario (GUI) en "Tkinter" para poder visualizar los datos de la aplicación de tablas interactivas y exportarlos mediante botones.
import tkinter as tk                    # Importa la biblioteca Tkinter y la renombra como 'tk'.
import pandas as pd                     # Importa la biblioteca "Pandas" para manejar datos en estructuras de DataFrame. (Un "DataFrame" es una estructura de datos bidimensional parecida a una hoja de cálculo o tabla, con filas y columnas, donde cada columna puede contener diferentes tipos de datos (números, texto, etc.) y cada fila representa una observación)
import ctypes                           # Importa la biblioteca "ctypes" para interactuar con bibliotecas de bajo nivel y funciones del sistema operativo.

from tkinter import ttk, messagebox     # El paquete "messagebox" crea ventanas emergentes, similar a "JOptionPane".
from db_connection import connection    # Importa la función de conexión "connection" a la base de datos desde el módulo/archivo "db_connection.py".



#Función/Método para consultar datos de la base de datos y devolverlos en un DataFrame de "Pandas".
def consultarDatos(host, database, user, password):
    try:
        # Establece la conexión a la base de datos.
        conn = connection(host, database, user, password)
        
        # Si la conexión es exitosa, realiza la consulta.
        if conn is not None:
            # Consulta SQL para obtener los datos de las tablas deseadas ("MEDICOS" y "CITAS") de la tabla ("HOSPITAL").
            querySQL = """
                            SELECT m.COD_MEDICO, m.NOMBRE_COMPLETO, m.ESPECIALIDAD, m.TURNO, m.CONSULTAS_DISPONIBLES_LUNES, m.CONSULTAS_DISPONIBLES_MARTES, m.CONSULTAS_DISPONIBLES_MIERCOLES, m.CONSULTAS_DISPONIBLES_JUEVES, m.CONSULTAS_DISPONIBLES_VIERNES, m.ANOS_EXPERIENCIA, c.NUM_CITA, c.COD_MEDICO, c.FECHA_CITA, c.HORA_CITA, c.MODALIDAD, c.URGENTE, c.ESTADO
                            FROM MEDICOS m
                            LEFT JOIN CITAS c ON m.COD_MEDICO = c.COD_MEDICO
                            ORDER BY m.COD_MEDICO, c.NUM_CITA
                       """
            
            # Utiliza "Pandas" para ejecutar la consulta y cargar los datos en un "DataFrame".
            df = pd.read_sql(querySQL, conn)
            
            # Una vez terminada la conexión y su posterior consulta cierra la conexión a la base de datos.
            conn.close()

            # Devuelve el "DataFrame" con los datos consultados, obtenidos de la consulta.
            #return df
            
            # Limpia la tabla antes de insertar nuevos datos para que estos no se dupliquen al volver a cargar.
            for item in tree.get_children():
                tree.delete(item)
            
            # Inserta los datos del" DataFrame" en el "Treeview".
                # Por cada fila del "DataFrame", ésta se convierte en lista ("list(now)") y después se inserta en la tabla visual "Treeview".
            for _, row in df.iterrows():
                #tree.insert("", "end", values = list(row))
                tree.insert("", "end", values = [str(item) for item in row])  # Para evitar errores de tipo (de valores) convertimos cada elemento de la fila a cadena, a "String", antes de insertarlo.
        else:
            raise Exception("\n\n\tNo se pudo establecer la conexión a la base de datos.")
    except Exception as ex:
        # Si ocurre un error durante el proceso de ejecución de la consulta, capturamos la excepción y mostramos un mensaje de error.
        #print(f"\n\n\tError inesperado al intentar conectarse a la base de datos '" + {db_name} + "': {er}")
        #raise Exception(f"\n\n\tError inesperado al intentar conectarse a la base de datos '" + {db_name} + "': {er}")
        #messagebox.showerror("Error de ejecución", f"Error inesperado al intentar ejecutar la consulta de datos de las tablas a la base de datos: {e}.")
        ctypes.windll.user32.MessageBoxW(0, f"Error inesperado al intentar ejecutar la consulta de datos de las tablas a la base de datos: {ex}", "Error de ejecución", 0x10)
        return None # Devuelve "None" si hubo un error durante la ejecución de la consulta.

# Función/Método para exportar los datos a un archivo PDF.
def export_data_to_pdf(host, database, user, password):
    try:
        from export_pdf import export_data_to_pdf           # Importa la función "export_data_to_pdf" desde el módulo/archivo "export_pdf.py".
        export_data_to_pdf(host, database, user, password)  # Llama a la función para exportar los datos a PDF.
    except Exception as ex:
        ctypes.windll.user32.MessageBoxW(0, f"Error inesperado al intentar exportar los datos a PDF: {ex}", "Error de exportación", 0x10)
        return None # Devuelve "None" si hubo un error durante la exportación de datos a PDF.


# Configuración de la ventana principal de la aplicación.
    # Crea la ventana principal.
root_windows = tk.Tk()                      # Crea la ventana principal (el contenedor de toda la app).
root_windows.title("Gestor de Informes")    # Título de la ventana.
root_windows.geometry("750x450")            # Define el tamaño de la ventana (ancho x alto).
root_windows.configure(bg = "#2C3E50")    # Cambia el color de fondo de la ventana principal
#root_windows.resizable(False, False)       # Evita que el usuario cambie el tamaño de la ventana (ancho, alto).

# Frame para colocar los botones lado a lado.
frame_botones = tk.Frame(root_windows, bg = "#2C3E50")  # Crea un marco (frame) para contener los botones.
frame_botones.pack(fill = 'x', padx = 20, pady = 15)                             # Empaqueta/Muestra el marco (frame) con un margen vertical (arriba/abajo) de tamaño 15.

# Crea y configura widgets (etiquetas, botones, etc.).
button_cargar = tk.Button(frame_botones, text = "🔄️\nCargar Datos", font = ("Arial", 20), command = lambda:consultarDatos("localhost", "HOSPITAL", "root", "root"))  # Botón que usa el/interactua con el usuario. Llama a la función "consultarDatos".
button_cargar.pack(side = "left", fill = "x", expand = True, padx = (0, 20))                                                                                                                 # Empaqueta/Muestra el botón "consultarDatos" estirado horizontalmente (a lo ancho). Añadiendo un margen horizontal (izquierda/derecha) con tamaño 50 y un margen vertical (arriba/abajo) con tamaño 15.

button_exportar = tk.Button(frame_botones, text = "⏬\nExportar Datos", font = ("Arial", 20), command = lambda:export_data_to_pdf("localhost", "HOSPITAL", "root", "root"))  # Botón que usa el/interactua con el usuario. Llama a la función "consultarDatos".
button_exportar.pack(side = "left")                                                                                # Empaqueta/Muestra el botón "consultarDatos" estirado horizontalmente (a lo ancho). Añadiendo un margen horizontal (izquierda/derecha) con tamaño 50 y un margen vertical (arriba/abajo) con tamaño 15.

# Crea un marco (frame) para contener la tabla y las barras de desplazamiento.
table_frame = ttk.Frame(root_windows, padding = (10, 10, 10, 10))       # Margen interno (izq, sup, der, inf).
table_frame.pack(fill = "both", expand = True, padx = 20, pady = 10)    # "padx" y "pady" crean el margen externo (borde) azul.

# Empaqueta/Muestra el "Treeview" dentro del marco (frame).
scrollbar_x = ttk.Scrollbar(table_frame, orient = "horizontal")
scrollbar_x.pack(side = "bottom", fill = "x")

# Crea el "Treeview" para mostrar los datos en forma de tabla.
tree = ttk.Treeview(table_frame)   # Crea el widget "Treeview" dentro de la ventana principal.
tree["columns"] = ("COD_MEDICO", "NOMBRE_COMPLETO", "ESPECIALIDAD", "TURNO", "CONSULTAS_DISPONIBLES_LUNES", "CONSULTAS_DISPONIBLES_MARTES", "CONSULTAS_DISPONIBLES_MIERCOLES", "CONSULTAS_DISPONIBLES_JUEVES", "CONSULTAS_DISPONIBLES_VIERNES", "ANOS_EXPERIENCIA", "NUM_CITA", "FECHA_CITA", "HORA_CITA", "MODALIDAD", "URGENTE", "ESTADO")    # Define las columnas del "Treeview".

# Configura los encabezados de las columnas.
for col in tree["columns"]:
    tree.heading(col, text = col, anchor = "w")                     # Configura los encabezados de las columnas.
    tree.column(col, width = 150, minwidth = 50, stretch = tk.YES)  # Configura el ancho de las columnas.

# La columna 'fantasma' que crea el espacio a la izquierda es la columna "#0" (el identificador de fila). Eliminamos ese espacio:
tree.column("#0", width = 0, stretch = tk.NO)   # Ancho 0, no redimensionable.
tree.heading("#0", text = "")                   # Columna vacía para el identificador del ítem. Sin encabezado.

# Para que la primera columna visible ("COD_MEDICO") se vea bien alineada a la izquierda y sin espacio extra.
tree.column("COD_MEDICO", anchor = "w", width = 80, minwidth = 60, stretch = tk.NO)

# Vincula/Añade el scrollbar horizontal al "Treeview".
tree.pack(fill = "both", expand = True, side = "left")    # Empaqueta/Muestra el "Treeview" para que ocupe todo el espacio disponible en la ventana principal.
scrollbar_x.pack(side = "bottom", fill = "x")           # Empaqueta/Muestra la barra horizontal en el lado derecho.
scrollbar_x.config(command = tree.xview)              # Configura la barra horizontal para controlar la vista del "Treeview".
tree.config(xscrollcommand = scrollbar_x.set)           # Configura el "Treeview" para usar la barra horizontal.

# Inicia el bucle principal de la aplicación (se llama a la ventana).
root_windows.mainloop() # Inicia el bucle principal que mantiene la ventana abierta y responde a eventos.