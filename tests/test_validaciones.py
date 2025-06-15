import unittest
from src.persona import Persona
from src.profesor import Profesor
from src.alumno import Alumno

class TestValidaciones(unittest.TestCase):
    """Pruebas adicionales para casos límite y validaciones."""
    
    def test_persona_datos_vacios(self):
        """Prueba que se lance excepción con datos vacíos."""
        with self.assertRaises(ValueError):
            Persona("", "Pérez", "12345678")
        
        with self.assertRaises(ValueError):
            Persona("Juan", "", "12345678")
        
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", "")
    
    def test_persona_datos_none(self):
        """Prueba que se lance excepción con datos None."""
        with self.assertRaises(ValueError):
            Persona(None, "Pérez", "12345678")
        
        with self.assertRaises(ValueError):
            Persona("Juan", None, "12345678")
        
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", None)
    
    def test_dni_formato_invalido(self):
        """Prueba validación de formato de DNI."""
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", "123")  # DNI muy corto
        
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", 12345678)  # DNI no es string
    
    def test_pensar_idea_vacia(self):
        """Prueba que no se pueda pensar una idea vacía."""
        persona = Persona("Juan", "Pérez", "12345678")
        
        with self.assertRaises(ValueError):
            persona.pensar("")
        
        with self.assertRaises(ValueError):
            persona.pensar(None)
    
    def test_profesor_sueldo_invalido(self):
        """Prueba validación de sueldo del profesor."""
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", 0)  # Sueldo 0
        
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", -1000)  # Sueldo negativo
        
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", "50000")  # Sueldo no numérico
    
    def test_alumno_legajo_vacio(self):
        """Prueba validación de legajo del alumno."""
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "12345678", "")
        
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "12345678", None)
    
    def test_herencia_metodo_pensar(self):
        """Prueba que las clases hijas heredan el método pensar."""
        profesor = Profesor("Ana", "García", "87654321", 60000)
        alumno = Alumno("Carlos", "López", "11223344", "B456")
        
        profesor.pensar("Cómo enseñar mejor")
        alumno.pensar("Necesito estudiar más")
        
        self.assertEqual(profesor.pensamientos, 1)
        self.assertEqual(profesor.ultima_idea, "Cómo enseñar mejor")
        
        self.assertEqual(alumno.pensamientos, 1)
        self.assertEqual(alumno.ultima_idea, "Necesito estudiar más")
    
    def test_multiples_pensamientos(self):
        """Prueba el contador de múltiples pensamientos."""
        persona = Persona("María", "Rodríguez", "99887766")
        
        persona.pensar("Primera idea")
        persona.pensar("Segunda idea")
        persona.pensar("Tercera idea")
        
        self.assertEqual(persona.pensamientos, 3)
        self.assertEqual(persona.ultima_idea, "Tercera idea")