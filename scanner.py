from os import listdir

photos = []
for x in listdir("C:\\Users\\Jacob Viertel\\Desktop\\foto_scan\\fotos"):
    print(x)
    photos.append(x)
    
print(len(photos))


