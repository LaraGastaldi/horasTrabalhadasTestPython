import pytest
from main import calcularHoras

def testHorasErro():
  with pytest.raises(ValueError) as excinfo:  
    calcularHoras('0103:00', '1221:00')       
  assert str(excinfo.value) == 'Horas invalidas'


def testDeveInserirHorasCorretas():
  assert calcularHoras('12:00', '18:00') == '06:00'

def testSubtrairHoras():
  assert calcularHoras('12:00', '18:00', '01:00') == '05:00'

def testHorasInvertidas():
  assert calcularHoras('18:00', '12:00') == '06:00'

def testHoraSemDoisPontos():
  assert calcularHoras('1200', '18:00') == '06:00'