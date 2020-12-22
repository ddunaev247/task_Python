#среднее ариф. и среднее гео..
a = float(input("введите число а:", ))
b = float(input("введите число b:", ))
sr_ar = (a + b) / 2
sr_geo = (a * b) ** .5
pro = a * b
if pro >= 0:
   sr_geo = float(sr_geo)
else:
   sr_geo = 'указанно отриц.число или 0'   
print("Ср.ариф: {0}. Ср.гео: {1}.".format(sr_ar, sr_geo))
