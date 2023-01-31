import pickle
import os
import sys
from PIL import Image
import numpy as np
import time

#Fichier : data_batch_1
#Image : b'batch_label'
#Image : b'labels'
#Image : b'data'
#Image : b'filenames'

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def main(repertoire):
    numérotation = 0

    liste = os.listdir(repertoire)

    for fichier in liste:
        #print("Fichier : %s" % fichier)
        liste_image = unpickle(repertoire + "/" + fichier)
        #print("Liste Image : %s" % liste_image)

        for label, data in zip(liste_image[b'labels'], liste_image[b'data']) :
            #print("Type Item : ", type(item))
            #print("Label : ", classes[label])
            #print("Data : ", data)
            #print("Longueur de Data : ", len(data))
            nom_fichier = classes[label] + "_" + str(numérotation) + '.jpg'

            LeTableau = np.array_split(data,3)
            #print("Le Tableau: ", LeTableau)
            MonImageRGB = np.array(list(zip(LeTableau[0], LeTableau[1], LeTableau[2])))
            #print("Mon Image : ", MonImageRGB)
            #print("Longueur MonImage : ", len(MonImageRGB))
            MonImage = MonImageRGB.reshape((32,32,3))
            #print("Shape MonImage : ", MonImage.shape)
            image = Image.fromarray(MonImage)
            image.save("Images/" + nom_fichier)
            numérotation += 1


if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print('USAGE: {} image_filename'.format(sys.argv[0]))
    else:
        t1 = time.time()
        main(sys.argv[1])
        print('Temps de Traitement : %d s' %(time.time()-t1))