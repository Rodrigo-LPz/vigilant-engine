# Exportación de los datos a PDF utilizando "ReportLab" y "MySQL Connector/MySQL Python".
    # Módulo para exportar datos de la base de datos MySQL a un archivo PDF.
from reportlab.lib.pagesizes import A4  # Importa el tamaño de página A4.
from reportlab.pdfgen import canvas     # Importa la clase "canvas" para crear el PDF.
from db_connection import connection    # Importa la función de conexión a la base de datos desde el módulo "db_connection".

# Función/Método para exportar los datos a un archivo PDF.
def export_data_to_pdf(host, database, user, password):
    # Establece la conexión a la base de datos.
    conn = connection(host, database, user, password)

    # Crea un cursor para ejecutar consultas SQL.
    curSQL = conn.cursor()

    # Ejecuta una consulta SQL para obtener los datos de ambas tabla "MEDICOS" y "CITAS".
    curSQL.execute("""
                    SELECT m.COD_MEDICO, m.NOMBRE_COMPLETO, m.ESPECIALIDAD, m.TURNO, m.CONSULTAS_DISPONIBLES_LUNES, m.CONSULTAS_DISPONIBLES_MARTES, m.CONSULTAS_DISPONIBLES_MIERCOLES, m.CONSULTAS_DISPONIBLES_JUEVES, m.CONSULTAS_DISPONIBLES_VIERNES, m.ANOS_EXPERIENCIA, c.NUM_CITA, c.COD_MEDICO, c.FECHA_CITA, c.HORA_CITA, c.MODALIDAD, c.URGENTE, c.ESTADO
                    FROM MEDICOS m
                    LEFT JOIN CITAS c ON m.COD_MEDICO = c.COD_MEDICO
                    ORDER BY m.COD_MEDICO, c.NUM_CITA
                   """)
    
    # Obtiene todos los datos resultantes de la consulta.
    datos = curSQL.fetchall()

    # Una vez terminada la conexión y su posterior consulta de ejecución cierra la conexión a la base de datos.
    conn.close()

    # Crea un archivo PDF.
        # Crea un objeto "canvas" para el PDF con: 
            # Nombre del archivo PDF.
            # Tamaño de página definido (A4).
            # Establece la fuente y el tamaño de letra
            # Título del informe en el PDF.
    pdf_file = "informe_medicos_citas.pdf"
    c = canvas.Canvas(pdf_file, pagesize = A4)
    c.setFont("Helvetica", 14)
    c.drawString(200, 800, "Informe de Médicos y Citas")

    # Define las posiciones iniciales para escribir los datos en el PDF.
    x = 50   # Posición horizontal inicial para escribir los datos.
    y = 750  # Posición vertical inicial para escribir los datos.

    # ========== Formato 1 ==========
    # Escribe los datos en el PDF.
    #for row in datos:
    #    texto = ", ".join(str(item) for item in row)    # Para evitar errores de tipo (de valores) convierte cada elemento de la fila a cadena, a "String", y cada elemento de la cadena separado por comas, antes de insertarlo.
    #    c.drawString(x, y, texto)                       # Escribe la cadena en la posición (x, y) del PDF.
    #    y -= 20                                         # Mueve la posición vertical hacia abajo para la siguiente fila.

    #    # Si la posición vertical llega al final de la página, crea una nueva página.
    #    if y < 50:
    #        c.showPage()      # Crea una nueva página en el PDF.
    #        c.setFont("Helvetica", 12)  # Restablece la fuente y el tamaño de letra.
    #        y = 750           # Reinicia la posición vertical para la nueva página.

    # ========== Formato 2 ==========
    # Escribe los datos en el PDF.
    for row in datos:
        cod_medico, nombre, especialidad, turno, lun, mar, mie, jue, vie, exp, num_cita, cod_medico_cita, fecha, hora, modalidad, urgente, estado = row

        tab = " " * 7

        rows = [
            f"{tab}{tab}Código del Médico: {cod_medico}" + f"{tab}Número de Cita: {num_cita}",
            "",
            "MÉDICO:",
            f"{tab}Médico: {cod_medico}",
            f"{tab}Nombre: {nombre}",
            f"{tab}Especialidad: {especialidad}",
            f"{tab}Turno: {turno}",
            f"{tab}Consultas Semanales Disponibles (L-V): {lun}, {mar}, {mie}, {jue}, {vie}",
            f"{tab}Años de experiencia: {exp}",
            "",
            "CITA:",
            f"{tab}Fecha: {fecha}",
            f"{tab}Hora: {hora}",
            f"{tab}Modalidad: {modalidad}",
            f"{tab}Urgente: {urgente}",
            f"{tab}Estado: {estado}",
            "-" * 100,
            "",
            "",
            "",
            ""
        ]

        for row in rows:
            c.drawString(x, y, row)                       # Escribe la cadena en la posición (x, y) del PDF.
            y -= 18                                         # Mueve la posición vertical hacia abajo para la siguiente fila.

            # Si la posición vertical llega al final de la página, crea una nueva página.
            if y < 60:
                c.showPage()      # Crea una nueva página en el PDF.
                c.setFont("Helvetica", 14)  # Restablece la fuente y el tamaño de letra.
                y = 800           # Reinicia la posición vertical para la nueva página.

    # Guarda el archivo PDF.
    c.save()
    print(f"\n\n\tLos datos han sido exportados exitosamente a {pdf_file}")