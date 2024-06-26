import numpy as np

def generar_carton():
    carton = np.zeros((3, 9), dtype=int)
    posiciones = np.random.choice(range(27), 15, replace=False)
    carton.flat[posiciones] = np.random.choice(range(1, 91), 15, replace=False)
    return carton

def verificar_linea(carton):
    for fila in carton:
        if np.count_nonzero(fila) == 0:
            return True
    return False

def verificar_bingo(carton):
    return np.count_nonzero(carton) == 0

def verificar_dos_lineas(carton):
    lineas_completas = 0
    for fila in carton:
        if np.count_nonzero(fila) == 0:
            lineas_completas += 1
    return lineas_completas >= 2

def simular_ronda(n_lineas, n_bingos):
    cartones = [generar_carton() for _ in range(1200)]
    bolillas = list(range(1, 91))
    np.random.shuffle(bolillas)
    
    lineas_conseguidas = 0
    bingos_conseguidos = 0
    tiempo = 0
    
    for numero in bolillas:
        tiempo += 10  # Cada número toma 10 segundos
        for carton in cartones:
            carton[carton == numero] = 0
            
            if verificar_linea(carton):
                lineas_conseguidas += 1
                # Resetear los ceros de la fila completa para evitar contarla nuevamente
                carton[carton == 0] = -1
                
            if verificar_bingo(carton):
                bingos_conseguidos += 1
                # Resetear el cartón para evitar contar el bingo nuevamente
                carton[carton == 0] = -1
        
        if lineas_conseguidas >= n_lineas and bingos_conseguidos >= n_bingos:
            return tiempo
    return tiempo

def tiempo_promedio(n_lineas, n_bingos, n_simulaciones=1000):
    tiempos = [simular_ronda(n_lineas, n_bingos) for _ in range(n_simulaciones)]
    return np.percentile(tiempos, 90)

def duracion_5_rondas(n_lineas, n_bingos, n_simulaciones=1000):
    duraciones = [sum([simular_ronda(n_lineas, n_bingos) for _ in range(5)]) for _ in range(n_simulaciones)]
    return np.percentile(duraciones, 90)

# Ajustar los parámetros deseados
n_lineas = 2
n_bingos = 1

# Ejecutar la simulación para 5 rondas
duracion_90_percentil_5_rondas = duracion_5_rondas(n_lineas, n_bingos, 1000)
print(f"La duración para conseguir {n_lineas} líneas y {n_bingos} bingos en 5 rondas consecutivas con 90% de confiabilidad es de {duracion_90_percentil_5_rondas} segundos.")