class Persona:
    """Clase base que representa a una persona con información básica.
    
    Esta clase maneja la información personal básica y permite a las personas
    'pensar' ideas, manteniendo un contador de pensamientos y la última idea.
    """
    
    def __init__(self, nombre, apellido, dni):
        """Inicializa una nueva persona.
        
        Args:
            nombre (str): El nombre de la persona.
            apellido (str): El apellido de la persona.
            dni (str): El documento nacional de identidad.
            
        Raises:
            ValueError: Si algún parámetro está vacío o es None.
        """
        if not nombre or not apellido or not dni:
            raise ValueError("Nombre, apellido y DNI son obligatorios")
        
        if not isinstance(dni, str) or len(dni) < 7:
            raise ValueError("DNI debe ser una cadena de al menos 7 caracteres")
            
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"
    
    def __repr__(self):
        """Representación en cadena de la persona.
        
        Returns:
            str: Descripción completa de la persona incluyendo su última idea.
        """
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    
    def pensar(self, idea):
        """Permite a la persona pensar una nueva idea.
        
        Incrementa el contador de pensamientos y actualiza la última idea.
        
        Args:
            idea (str): La nueva idea que piensa la persona.
            
        Raises:
            ValueError: Si la idea está vacía o es None.
        """
        if not idea:
            raise ValueError("La idea no puede estar vacía")
            
        self.pensamientos += 1
        self.ultima_idea = idea