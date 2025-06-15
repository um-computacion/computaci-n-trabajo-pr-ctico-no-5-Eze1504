"""
Ejemplo de uso del sistema de gestión de personas.

Este archivo demuestra cómo utilizar las clases Persona, Profesor y Alumno
implementadas en el sistema.
"""

from src.persona import Persona
from src.profesor import Profesor
from src.alumno import Alumno

def main():
    """Función principal que demuestra el uso del sistema."""
    print("=== Sistema de Gestión de Personas ===\n")
    
    # Crear una persona común
    print("1. Creando una persona común:")
    persona = Persona("Juan", "Pérez", "12345678")
    print(f"   {persona}")
    
    # Hacer que la persona piense
    print("\n2. La persona piensa algo:")
    persona.pensar("¿Qué haré hoy?")
    print(f"   {persona}")
    print(f"   Pensamientos totales: {persona.pensamientos}")
    
    # Crear un profesor
    print("\n3. Creando un profesor:")
    profesor = Profesor("Ana", "García", "87654321", 75000.50)
    print(f"   {profesor}")
    
    # El profesor también puede pensar
    print("\n4. El profesor piensa sobre su clase:")
    profesor.pensar("Cómo puedo explicar mejor este tema")
    print(f"   Última idea del profesor: {profesor.ultima_idea}")
    print(f"   Pensamientos del profesor: {profesor.pensamientos}")
    
    # Crear un alumno
    print("\n5. Creando un alumno:")
    alumno = Alumno("Carlos", "López", "11223344", "EST2024001")
    print(f"   {alumno}")
    
    # El alumno piensa sobre sus estudios
    print("\n6. El alumno reflexiona:")
    alumno.pensar("Necesito estudiar más para el examen")
    alumno.pensar("¿Cuándo será la próxima clase?")
    print(f"   Última idea del alumno: {alumno.ultima_idea}")
    print(f"   Pensamientos del alumno: {alumno.pensamientos}")
    
    # Demostrar polimorfismo
    print("\n7. Demostración de polimorfismo:")
    personas = [persona, profesor, alumno]
    
    for i, p in enumerate(personas, 1):
        print(f"   Persona {i}: {p}")
    
    print("\n8. Todas las personas piensan:")
    for p in personas:
        p.pensar("¡Qué buen día!")
        print(f"   {p.nombre} ahora tiene {p.pensamientos} pensamientos")
    
    print("\n=== Fin del ejemplo ===")

if __name__ == "__main__":
    main()