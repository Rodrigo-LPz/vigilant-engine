/**
 *
 * @author Rodrigo
 */
package com.mycompany.recuperacionexamen_ut2;


// Importa de la biblioteca/librería el paquete "Connection".
import java.sql.Connection;
// Importa de la biblioteca/librería el paquete "DriverManager".
import java.sql.DriverManager;
// Importa de la biblioteca/librería el paquete "PreparedStatement".
import java.sql.PreparedStatement;
// Importa de la biblioteca/librería el paquete "ResultSet".
import java.sql.ResultSet;
// Importa de la biblioteca/librería el paquete "SQLException".
import java.sql.SQLException;
// Importa de la biblioteca/librería el paquete "Statement".
import java.sql.Statement;
// Importa de la biblioteca/librería el paquete "JOptionPane".
import javax.swing.JOptionPane;

// Crea la clase 'main', principal, del programa.
public class RecuperacionExamen_UT2{
    // Configuración previa.
        // Variable (Atributo) de carácter privado para crear la conexión con la DB dado una dirección, "URL"; un usuario, "USER"; y una contraseña "PASSWORD".
    private Connection connection;
    
        // Configuración MySQL.
    private static final String URL = "jdbc:mysql://localhost:3306/";
    private static final String DB_NAME = "HOSPITAL";
    private static final String URL_ROOT = URL + DB_NAME;
    private static final String USER = "root";
    private static final String PASSWORD = "root";
    
    String sql;
    
    // Crea el método 'main', principal, del programa. Su función será ir llamando/inicializando los distintos métodos que contenga la clase "RecuperacionExamen_UT2".
    public static void main(String[] args){
        RecuperacionExamen_UT2 hospital = new RecuperacionExamen_UT2();
        
        hospital.Conexion();
        
        // -------------------- Apartado 1 --------------------
        hospital.MostrarDatos();
        
        // -------------------- Apartado 2 --------------------
        hospital.mostrarCitasPorMedicos(DB_NAME);
        
        // -------------------- Apartado 3 --------------------
        hospital.insertarMedico(DB_NAME, DB_NAME, USER, URL, 0, 0, 0, 0, 0, 0);
        
        // -------------------- Apartado 4 --------------------
        hospital.eliminarMedico(DB_NAME);
        
        // -------------------- Apartado 5 --------------------
        
        
        // -------------------- Apartado 6 --------------------
        
    }
    
    // Crea el método "Conexion". Su función será conectarse a la base de datos.
    public void Conexion(){
        try{
            connection = DriverManager.getConnection(URL_ROOT, USER, PASSWORD);
            
            System.out.println("\n\n\tConexión exitosa al servidor.");
            
            System.out.println("\n\n\tConexión a la DB (base de datos) \"" + DB_NAME + "\" abierta.");
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar conectarse a la DB (base de datos): " + sqlex.getMessage(), "Error de conexión", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    // -------------------- Apartado 1 -------------------- 
        // Crea el método "MostrarDatos". Su función será mostrar toda la información, todos los datos almacenada (médicos y citas).
    public void MostrarDatos(){
        // Comprobación previa para verificar si la conexión sigue vigente.
        if (connection == null){
            JOptionPane.showMessageDialog(null, "Error inesperado la conexión se ha detenido/pausado repentinamente. La base de datos no está operativa, activa.", "Error de conexión", JOptionPane.ERROR_MESSAGE);
            return;
        }
        
        // Muestra los médicos.
            // Crea la sentencia SQL para realizar la búsqueda.
        sql = "SELECT * FROM MEDICOS";
        
        try (Statement st = connection.createStatement(); ResultSet rs = st.executeQuery(sql)){
            System.out.println("\n\n\t<==================== Lista/Tabla de MEDICOS ====================>");
            
            while (rs.next()){
                System.out.printf("%-10s %-80s %-30s %-10s %d %d %d %d %d %d\n",
                        rs.getString("COD_MEDICO"),
                        rs.getString("NOMBRE_COMPLETO"),
                        rs.getString("ESPECIALIDAD"),
                        rs.getString("TURNO"),
                        rs.getInt("CONSULTAS_DISPONIBLES_LUNES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_MARTES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_MIERCOLES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_JUEVES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_VIERNES"),
                        rs.getInt("ANOS_EXPERIENCIA")
                        );
            }
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar mostrar la lista de los datos de los médicos: " + sqlex.getMessage(), "Error de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
        
        // Muestra las citas.
            // Crea la sentencia SQL para realizar la búsqueda.
        sql = "SELECT * FROM CITAS";
        
        try (Statement st = connection.createStatement(); ResultSet rs = st.executeQuery(sql)){
            System.out.println("\n\n\t<==================== Lista/Tabla de CITAS ====================>");
            
            while (rs.next()){ System.out.println("\n\n\tNúmero de Cita: " + rs.getInt("NUM_CITA") + "\n\tCódigo del médico: " + rs.getInt("COD_MEDICO") + "\n\tFecha de la Cita: " + rs.getDate("FECHA_CITA") + "\n\tHora de la Cita: " + rs.getTime("HORA_CITA") + "\n\tModalidad/Especialidad: " + rs.getString("MODALIDAD") + "\n\tUrgente: " + rs.getString("URGENTE") + "\n\tEstado: " + rs.getString("ESTADO")); }
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar mostrar la lista de los datos de las citas médicas: " + sqlex.getMessage(), "Error de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
        
        // Muestra los médicos y las citas, todo junto.
            // Crea la sentencia SQL para realizar la búsqueda.
        sql = """
                SELECT m.COD_MEDICO, m.NOMBRE_COMPLETO, m.ESPECIALIDAD, m.TURNO, m.CONSULTAS_DISPONIBLES_LUNES, m.CONSULTAS_DISPONIBLES_MARTES, m.CONSULTAS_DISPONIBLES_MIERCOLES, m.CONSULTAS_DISPONIBLES_JUEVES, m.CONSULTAS_DISPONIBLES_VIERNES, m.ANOS_EXPERIENCIA, c.Número de Cita, c.COD_MEDICO, c.FECHA_CITA, c.HORA_CITA, c.MODALIDAD, c.URGENTE, c.ESTADO
                FROM MEDICOS m
                LEFT JOIN CITAS c ON m.COD_MEDICO = c.COD_MEDICO
                ORDER BY m.COD_MEDICO, c.NUM_CITA
              """;
        
        try (Statement st = connection.createStatement(); ResultSet rs = st.executeQuery(sql)){
            System.out.println("\n\n\t<==================== Lista/Tabla de MEDICOS con sus respectivas CITAS ====================>");
            
            while (rs.next()){
                System.out.printf("Código del Médico: %-10s | Nombre Completo: %-80s | Especialidad: %-30s | Turno: %-10s | Consultas Disponibles los Lunes: %d | Consultas Disponibles los Martes: %d | Consultas Disponibles los Miércoles: %d | Consultas Disponibles los Jueves: %d | Consultas Disponibles los Viernes: %d | Años de Experiencia: %d | Número de Cita: %d | Fecha de la Cita: %-16s | Hora de la Cita: %-16s | Modalidad/Especialidad: %-15s | Urgente: %-2s | Estado: %-15s",
                        rs.getString("COD_MEDICO"),
                        rs.getString("NOMBRE_COMPLETO"),
                        rs.getString("ESPECIALIDAD"),
                        rs.getString("TURNO"),
                        rs.getInt("CONSULTAS_DISPONIBLES_LUNES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_MARTES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_MIERCOLES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_JUEVES"),
                        rs.getInt("CONSULTAS_DISPONIBLES_VIERNES"),
                        rs.getInt("ANOS_EXPERIENCIA"),
                        rs.getInt("NUM_CITA"),
                        rs.getDate("FECHA_CITA"),
                        rs.getTime("HORA_CITA"),
                        rs.getString("MODALIDAD"),
                        rs.getString("URGENTE"),
                        rs.getString("ESTADO")
                        );
            }
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar mostrar la lista de los datos de los médicos junto a sus respectivas citas médicas: " + sqlex.getMessage(), "Error de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    // -------------------- Apartado 2 -------------------- 
        // Crea el método "mostrarCitasPorMedicos". Su función será mostrar toda la información, todos los datos almacenada (médicos y citas), pero listando las citas en función del parámetro médico.
    public void mostrarCitasPorMedicos(String codMedico){
        // Comprobación previa para verificar si la conexión sigue vigente.
        if (connection == null){
            JOptionPane.showMessageDialog(null, "Error inesperado la conexión se ha detenido/pausado repentinamente. La base de datos no está operativa, activa.", "Error de conexión", JOptionPane.ERROR_MESSAGE);
            return;
        }
        
        // Muestra los médicos.
            // Crea la sentencia SQL para realizar la búsqueda.
        sql = "SELECT * FROM CITAS WHERE COD_MEDICO = ?";
        
        try (PreparedStatement pst = connection.prepareStatement(sql)){
            pst.setString(1, codMedico);
            ResultSet rs = pst.executeQuery();
            
            System.out.println("\n\n\tCitas con el médico '" + codMedico + "':");
            
            // Declara una variable booleana inicializada en valor "false" para comprobar si hay o no citas declaradas en/para un vuelo.
            boolean hayCitas = false;
            
            while (rs.next()){
                hayCitas = true;
                
                System.out.printf("Número de la Cita: %d | Fecha de la Cita: %-16s | Hora de la Cita: %-16s | Modalidad/Especialidad: %-15s | Urgente: %-2s | Estado: %-15s");
            }
            
            if (!hayCitas) System.out.println("\n\n\tNo hay citas pendientes (registradas) para dicho médico, para el médico con código {" + codMedico + "}.");
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar mostrar la lista de los datos de las citas respecto al parámetro 'código de un médico (COD_MEDICO)': " + sqlex.getMessage(), "Error de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    // -------------------- Apartado 3 -------------------- 
        // Crea el método "insertarMedico". Su función será la de añadir un nuevo registro a la tabla "MEDICOS", es decir, añadir un nuevo médico.
    public void insertarMedico(String codMedico, String nombreCompleto, String especialidad, String turno, int consultasDisponiblesLunes, int consultasDisponiblesMartes, int consultasDisponiblesMiercoles, int consultasDisponiblesJueves, int consultasDisponiblesViernes, int anosExperiencia){
        // Comprobación previa para verificar si la conexión sigue vigente.
        if (connection == null){
            JOptionPane.showMessageDialog(null, "Error inesperado la conexión se ha detenido/pausado repentinamente. La base de datos no está operativa, activa.", "Error de conexión", JOptionPane.ERROR_MESSAGE);
            return;
        }
        
        // Muestra los médicos.
            // Crea la sentencia SQL para realizar la inserción.
        sql = "INSERT INTO VUELOS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
        int rows;
        
        try (PreparedStatement pst = connection.prepareStatement(sql)){
            pst.setString(1, codMedico);
            pst.setString(2, nombreCompleto);
            pst.setString(3, especialidad);
            pst.setString(4, turno);
            pst.setInt(5, consultasDisponiblesLunes);
            pst.setInt(6, consultasDisponiblesMartes);
            pst.setInt(7, consultasDisponiblesMiercoles);
            pst.setInt(8, consultasDisponiblesJueves);
            pst.setInt(9, consultasDisponiblesViernes);
            pst.setInt(10, anosExperiencia);
            
            rows = pst.executeUpdate();
            
            System.out.println("\n\n\tEl nuevo médico ha sido insertado/registrado en la tabla \"MEDICOS\" correctamente.\n\t\tSe han añadido un total de {" + rows + "} filas nuevas en el registro.");
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar insertar/registrar un nuevo médico a la lista de la tabla \"MEDICOS\": " + sqlex.getMessage(), "Error de inserción de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    // -------------------- Apartado 4 -------------------- 
        // Crea el método "eliminarMedico". Su función será la de eliminar/borrar el nuevo médico registrado/insertado a la tabla "MEDICOS".
    public void eliminarMedico(String codMedico){
        // Comprobación previa para verificar si la conexión sigue vigente.
        if (connection == null){
            JOptionPane.showMessageDialog(null, "Error inesperado la conexión se ha detenido/pausado repentinamente. La base de datos no está operativa, activa.", "Error de conexión", JOptionPane.ERROR_MESSAGE);
            return;
        }
        
        // Muestra los médicos.
            // Crea la sentencia SQL para realizar la eliminación.
        sql = "DELETE FROM MEDICOS WHERE COD_MEDICO = ?";
        int rows;
        
        try (PreparedStatement pst = connection.prepareStatement(sql)){
            pst.setString(1, codMedico);
            
            rows = pst.executeUpdate();
            
            System.out.println("\n\n\tEl nuevo médico ha sido eliminado/borrado de la tabla \"MEDICOS\" correctamente.\n\t\tSe han eliminado un total de {" + rows + "} filas del nuevo registro, del nuevo medico.");
        } catch (SQLException sqlex){
            System.getLogger(RecuperacionExamen_UT2.class.getName()).log(System.Logger.Level.ERROR, (String) null, sqlex);
            JOptionPane.showMessageDialog(null, "Error inesperado al intentar borrar/eliminar el nuevo médico de la lista de la tabla \"MEDICOS\": " + sqlex.getMessage(), "Error de eliminación de sentencia 'SQL'", JOptionPane.ERROR_MESSAGE);
        }
    }
}
