import io_handler
import analyzer
import pyfiglet
from matplotlib import pylab
import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)

def main():
    print(pyfiglet.figlet_format("GenShell"))

    opcion_carga = input("¿Cargar archivo FASTA? (s/n): ").lower()
    if opcion_carga == 's':
        ruta = input("Ingresa la ruta: ")
        record = io_handler.obtener_desde_archivo(ruta)
    else:
        record = io_handler.obtener_manual()
    
    while True:
        print(f"\n--- Secuencia actual: {record.id} ---")
        print("1. GC | 2. Complemento | 3. Transcripción | 4. Traducción | 5. Inversa | 6.Grafico GC | 7. Salir")
        
        eleccion = input("Opción: ")
        
        if eleccion == '1':
            print(f"Resultado GC: {analyzer.procesar_gc(record)}")
        elif eleccion == '2':
            print(f"Complemento: {analyzer.procesar_complemento(record)}")
        elif eleccion == '3':
            print(f"Transcripción: {analyzer.procesar_transcripcion(record)}")
        elif eleccion == '4':
            print(f"Traducción: {analyzer.procesar_traduccion(record)}")
        elif eleccion == '5':
            print(f"Secuencia Inversa: {analyzer.procesar_inversa(record)}")
        elif eleccion == '6':
            print("Generando grafica GC...")
            analyzer.grafica_gc(record)
        elif eleccion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()