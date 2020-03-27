import os

path = "C:\\Users\\Rodrigo\\Desktop\\fotos - isolados\\azul_claro"
i = 50
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'azul_claro_isoladas_'+str(i)+'.jpg'))
    i = i +1
