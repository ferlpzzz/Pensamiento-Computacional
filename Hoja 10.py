#ejercicio 1
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def mostrar_datos_medicos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
    
    def calcular_dosis(self):
        return self.peso * 0.1
    
    def generar_ficha_medica(self):
        print("FICHA MÉDICA")
        self.mostrar_datos_medicos()
        print(f"Dosis recomendada: {self.calcular_dosis()} mg")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza, vacunado):
        super().__init__(nombre, edad, peso)
        self.raza = raza
        self.vacunado = vacunado
    
    def calcular_dosis(self):
        return self.peso * 0.15
    
    def mostrar_datos_medicos(self):
        super().mostrar_datos_medicos()
        print(f"Raza: {self.raza}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color, esterilizado):
        super().__init__(nombre, edad, peso)
        self.color = color
        self.esterilizado = esterilizado
    
    def calcular_dosis(self):
        return self.peso * 0.08
    
    def mostrar_datos_medicos(self):
        super().mostrar_datos_medicos()
        print(f"Color: {self.color}")
        print(f"Esterilizado: {'Sí' if self.esterilizado else 'No'}")

class Ave(Animal):
    def __init__(self, nombre, edad, peso, tipo_ave, puede_volar):
        super().__init__(nombre, edad, peso)
        self.tipo_ave = tipo_ave
        self.puede_volar = puede_volar
    
    def calcular_dosis(self):
        return self.peso * 0.05
    
    def mostrar_datos_medicos(self):
        super().mostrar_datos_medicos()
        print(f"Tipo de ave: {self.tipo_ave}")
        print(f"Puede volar: {'Sí' if self.puede_volar else 'No'}")

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, tipo_reptil, venenoso):
        super().__init__(nombre, edad, peso)
        self.tipo_reptil = tipo_reptil
        self.venenoso = venenoso
    
    def calcular_dosis(self):
        return self.peso * 0.03
    
    def mostrar_datos_medicos(self):
        super().mostrar_datos_medicos()
        print(f"Tipo de reptil: {self.tipo_reptil}")
        print(f"Venenoso: {'Sí' if self.venenoso else 'No'}")
perro1 = Perro("Firulais", 5, 12, "Labrador", True)
perro1.generar_ficha_medica()

gato1 = Gato("Michi", 3, 4.5, "Negro", False)
gato1.generar_ficha_medica()

#ejercicio 2 
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera, semestre):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera
        self.semestre = semestre
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print("Rol: Estudiante")

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, departamento, especialidad):
        super().__init__(nombre, edad, dni)
        self.departamento = departamento
        self.especialidad = especialidad
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")
        print(f"Especialidad: {self.especialidad}")
        print("Rol: Profesor")

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, puesto, antiguedad):
        super().__init__(nombre, edad, dni)
        self.puesto = puesto
        self.antiguedad = antiguedad
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puesto: {self.puesto}")
        print(f"Antigüedad: {self.antiguedad} años")
        print("Rol: Administrativo")
estudiante1 = Estudiante("Juan Pérez", 20, "12345678", "Ingeniería", 4)
estudiante1.mostrar_informacion()

profesor1 = Profesor("María González", 45, "87654321", "Ciencias", "Matemáticas")
profesor1.mostrar_informacion()