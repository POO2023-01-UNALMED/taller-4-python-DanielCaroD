from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], listadoAlumnos=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.grado = "Grado 12"
        self.listadoAlumnos = listadoAlumnos

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
