from django.test import TestCase
from ATodoGasApp.models import Persona

class PersonaTestCase(TestCase):
    def setUp(self):
        Persona.objects.create(nombre="pedrito", apellido="benitez", telefono= "3156654", email= "holi@holi.com", direccion="carrera 52 D", municipio = "valle del cauca", identificacion="0549551231")
        

    def test_persona(self):
        
        pedrito = Persona.objects.get(nombre="pedrito")
        
        self.assertEqual(pedrito.nombre, 'pedrito')
        