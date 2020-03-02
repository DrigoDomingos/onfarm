import os

path = 'C:\Users\Rodrigo\Desktop\Azul_Claro Etapa 1 Revisado'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,str(i)+'.jpg'))
    i = i +1