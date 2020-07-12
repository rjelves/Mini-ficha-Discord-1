import datetime
import pytz as tz

nombre_dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

mision = input("Ingresa nombre de misión: ")
fecha = input("Ingresa fecha en formato AAAAMMDD: ")
horaUTC = input("Ingresa hora UTC (ej. 21:18): ")
live = input("Ingresa nombre de la transmisión oficial, ENTER para omitir: ")
while True:
  fichaWeb = input("¿Deseas agregar la ficha web al pie? (S/N): ")
  if fichaWeb.upper() == "S":
    codigo = input("Ingresa el código del final de la dirección URL de la ficha web. Ejemplo, 2020-035a : ")
    break
  elif fichaWeb.upper() == "N":
    codigo = False
    break
  else:
    print("Respuesta inválida.")


horaUTC = horaUTC.split(":")
anio = int(fecha[0:4])
mes = int(fecha[4:6])
dia = int(fecha[6:])
hora = int(horaUTC[0])
minuto = int(horaUTC[1])

fechahora = tz.utc.localize(datetime.datetime(anio, mes, dia, hora, minuto))

print("\n**Lanzamiento:", mision + "**")
print(nombre_dias[int(fechahora.strftime("%w"))], dia, "de", nombre_meses[int(fechahora.strftime("%m")) - 1].lower(), "de", anio, fechahora.strftime("%X"), "UTC")
if live != "":
  print("Transmisión en vivo: **Sí (" + live + ")**")
else:
  print("Transmisión en vivo: No")
print("\n*Horarios según la capital de cada país:*")

horaES = fechahora.astimezone(tz.timezone('Europe/Madrid'))
horaAR = fechahora.astimezone(tz.timezone('America/Buenos_Aires'))
horaCL = fechahora.astimezone(tz.timezone('America/Santiago'))
horaCO = fechahora.astimezone(tz.timezone('America/Bogota'))
horaCR = fechahora.astimezone(tz.timezone('America/Costa_Rica'))
print(horaES.strftime("%H:%M"), ":flag_es:")
print(horaAR.strftime("%H:%M"), ":flag_ar: :flag_uy:")
print(horaCL.strftime("%H:%M"), ":flag_bo: :flag_cl: :flag_cu: :flag_do: :flag_pr: :flag_py: :flag_ve:")
print(horaCO.strftime("%H:%M"), ":flag_co: :flag_ec: :flag_mx: :flag_pa: :flag_pe:")
print(horaCR.strftime("%H:%M"), ":flag_cr: :flag_gt: :flag_hn: :flag_ni: :flag_sv:")
if codigo == False:
  print("\n*Más info:* https://fronteraespacial.weebly.com/lanzamientos.html")
else:
  print("\n*Ficha de lanzamiento:* https://fronteraespacial.weebly.com/coheteria/" + codigo)