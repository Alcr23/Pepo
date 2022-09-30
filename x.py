from blog2.models import Datos
f = open(r'C:\Users\Valo_\Desktop\toño\papi\p5.txt', 'r')
for line in f:
    data = Datos()
    line = line.split(' ')
    data.x1 = line[0]
    data.x2 = line[1]
    data.x3 = line[2]
    data.x4 = line[3]
    data.save()
