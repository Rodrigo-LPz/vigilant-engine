/**
 *
 * @authors Rodrigo y Matías
 */
package Hilos_y_Servicios___Multihilo_Runnable_Control;


// Importa de la biblioteca/librería el paquete "JOptionPane".
import javax.swing.JOptionPane;

/*
    Problema/Ejercicio 3 (con Runnable Controlado, con 'Control'):
        Controlar la ejecución de los hilos: usar "sleep()", "join()" y "setPriority()". Con esto se puede controlar el orden, la pausa y la prioridad con la que se ejecutan los hilos.
*/

// Crea la clase principal del programa.
public class MostrarHiloRunnableControl{
    public static void main(String[] args){

        // Creamos dos hilos conectados a la clase "HiloMensaje", con 'Runnable' implementado
            // A cada hilo le pasamos un nombre diferente.
        Thread hilo1 = new Thread(new HiloMensaje("Hilo 1"));
        Thread hilo2 = new Thread(new HiloMensaje("Hilo 2"));
        
        // Cambiamos la prioridad de cada hilo. Cuanto mayor sea el número, más atención le da el procesador a ese hilo.
            // La prioridad es un valor del 1 al 10 (MIN_PRIORITY = 1, MAX_PRIORITY = 10).
        hilo1.setPriority(Thread.MIN_PRIORITY);
        hilo2.setPriority(Thread.MAX_PRIORITY);
        
        // Llama/Iniciliza los dos hilos llamando al método "run()" de "HiloMensaje".
        hilo1.start();
        hilo2.start();
        
        try{
            // Hacemos uso del método de control "join()". Con él, le decimos al programa principal (main) que espere a que estos hilos terminen su ejecución antes de continuar.
            hilo1.join();
            hilo2.join();
        } catch (InterruptedException iex){
            // Captura de excepción para el caso de si algún hilo es interrumpido mientras esperamos, mostramos un mensaje.
            JOptionPane.showMessageDialog(null, "Error de ejecución", "Error inesperado en la ejecución de los hilos. Un hilo fue interrumpido: " + iex.getMessage(), JOptionPane.ERROR_MESSAGE);
        }
        
        System.out.println("\nTodos los hilos han terminado.");
    }
}

// Crea la clase "HiloMensaje" ésta implementa "Runnable", una forma alternativa de crear hilos en Java, sin necesidad de heredar de la clase "Thread".
class HiloMensaje implements Runnable{
    // Declara una variable de cadena privada con la que guardar el nombre del hilo (para saber cuál escribe cada mensaje).
    private String nombre;

    // Crea el constructor (recibe el nombre del hilo cuando se crea).
    public HiloMensaje(String nombre){
        this.nombre = nombre;
    }

    // Sobrescribe/Redefine el método "run()" de la clase "HiloMostrarCero".
    @Override
    // Crea el método "run", contiene el código que el hilo ejecutará cuando lo iniciemos con "start()".
    public void run(){
        // Bucle "for" con el que mostrar varios mesnajes 10 veces.
        for (int i = 1; i <= 10; i++){
            // Muestra un mensaje con el nombre del hilo y el número de mensaje.
            System.out.println(nombre + "\t-\tmensaje: " + i);

            try{
            // Hacemos uso del método de control "sleep()". Con él, le decimos al programa principal (main) que se detenga el hilo durante medio segundo (500 milisegundos).
                // Esto sirve para simular una tarea que tarda un poco en completarse.
                Thread.sleep(500);
            } catch (InterruptedException iex){
                // Captura de excepción para el caso de si algún hilo es interrumpido durante la pausa mientras esperamos, mostramos un mensaje.
                JOptionPane.showMessageDialog(null, "Error de ejecución", "Error inesperado durante la espera de ejecución de los hilos. Un hilo {" + nombre + "} fue interrumpido: " + iex.getMessage(), JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}