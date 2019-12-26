class Test_partir_string(unittest.TestCase):

  def solucion(self, valor):
    return valor.split(',')
    
  def test_function_defined(self):
    
    try:
        partir_string('')
    except NameError:
        self.fail('La función partir_string no está definida')
    
  def test_valores(self):
    self.probar_valores('68,47,24,1995')
    self.probar_valores('321,654,3,612,85')
    
  def probar_valores(self, valor):
    valor_obtenido = partir_string(valor)
    valor_solucion = self.solucion(valor)
    self.assertEqual( valor_obtenido, valor_solucion, f'El valor obtenido para el parámetro "{valor}", fue "{valor_obtenido}" y debería ser "{valor_solucion}".' )
    