from datetime import date

today = date.today()
yyyyddmm = today.strftime("%Y%m%d")

print(yyyyddmm)