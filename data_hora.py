from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = str(agora.year)[2:4]

print("{}/{:02d}/{}".format(dia, mes, ano))
