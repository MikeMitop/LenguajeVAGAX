from librerias.grafvag import GRAFVAG

def graficar_funciones_trigonometricas():
  
    print("GENERANDO GRÁFICAS TRIGONOMÉTRICAS CON GRAFVAG")
    

    # El motor ahora se encarga de todo de forma interna
    print("[*] Renderizando Seno...")
    GRAFVAG.plot_funcion("seno", nombre_archivo="grafica_seno.ppm")

    print("[*] Renderizando Coseno...")
    GRAFVAG.plot_funcion("coseno", nombre_archivo="grafica_coseno.ppm")

    print("[*] Renderizando Tangente...")
    GRAFVAG.plot_funcion("tangente", nombre_archivo="grafica_tangente.ppm")
    


if __name__ == "__main__":
    graficar_funciones_trigonometricas()