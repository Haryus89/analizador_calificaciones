def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones."""
    if len(calificaciones) == 0:
        return 0
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio