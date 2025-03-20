.. code:: ipython3

    # Clase base 
    class Vehiculo:
        # Atributos de clase
        tipo_vehiculo = "Automóvil"
        ruedas = 4
        motor = "Gasolina"
    
        def __init__(self, marca, modelo):
            # Atributos de instancia
            self.marca = marca
            self.modelo = modelo
    
    # Clase derivada 
    class Auto(Vehiculo):
        # Atributos de instancia adicionales
        def __init__(self, marca, modelo, color, anio):
            # Heredando los atributos de la superclase
            super().__init__(marca, modelo)
            self.color = color
            self.anio = anio
    
        def mostrar_info(self):
            return f"{self.marca} {self.modelo}, Año: {self.anio}, Color: {self.color}"
    
    # Creación de una instancia de la clase Auto 
    auto1 = Auto("Chevrolet", "Corvette C6", "Negro", 2008)
    
    # Acceso a atributos heredados y de instancia
    print(f"Tipo de vehículo: {auto1.tipo_vehiculo}")
    print(f"Número de ruedas: {auto1.ruedas}")
    print(f"Motor: {auto1.motor}")
    print(auto1.mostrar_info())
    


.. parsed-literal::

    Tipo de vehículo: Automóvil
    Número de ruedas: 4
    Motor: Gasolina
    Chevrolet Corvette C6, Año: 2008, Color: Negro
    

