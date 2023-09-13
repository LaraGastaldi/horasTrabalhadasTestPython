import re

HOUR_PATTERN = r"^\d{1,2}\:?\d{2}$"


def insereDoisPontos(hora):
  if not re.match(r".*\:.*", hora):
    pos = 2 if len(hora) == 4 else 1
    hora = list(hora)
    hora.insert(pos, ':')
    return ''.join(hora)
  return hora


def mapeiaHoras(hora1, hora2):
  return [
      int(j) for i in
      [insereDoisPontos(hora1).split(':'),
       insereDoisPontos(hora2).split(':')] for j in i
  ]
  

def calcularHoras(hora1, hora2, almoco='00:00'):
  if not re.match(HOUR_PATTERN, hora1) or not re.match(HOUR_PATTERN, hora2):
    raise ValueError('Horas invalidas')

  hora1Hora, hora1Minuto, hora2Hora, hora2Minuto = mapeiaHoras(hora1, hora2)

  if hora2Hora < hora1Hora or (hora1Hora == hora2Hora
                               and hora2Minuto < hora1Minuto):
    aux = [hora2Hora, hora2Minuto]
    hora2Hora, hora2Minuto = hora1Hora, hora1Minuto
    hora1Hora, hora1Minuto = aux

  resultadoHora = hora2Hora - hora1Hora
  resultadoMinutos = hora2Minuto - hora1Minuto

  horasAlmoco, minutosAlmoco = [
      int(i) for i in insereDoisPontos(almoco).split(':')
  ]

  resultadoHora -= horasAlmoco
  resultadoMinutos -= minutosAlmoco

  if resultadoMinutos < 0:
    resultadoHora -= 1
    resultadoMinutos = -resultadoMinutos

  if resultadoMinutos < 10:
    resultadoMinutos = '0' + str(resultadoMinutos)

  if resultadoHora < 10:
    resultadoHora = '0' + str(resultadoHora)

  return "{hh}:{mm}".format(hh=resultadoHora, mm=resultadoMinutos)
