import os
from shutil import copyfile


cwd = os.getcwd()
data = os.path.join(cwd,'data')
copydir = os.path.join(cwd, 'total')
labelList = []
for fold in os.listdir(data):
    if(fold not in labelList):
        labelList.append(fold)
    label = labelList.index(fold) + 1
    d = os.path.join(data,fold)
    for f in os.listdir(d):
        if(f != 'train'):
            continue
        imageDir = os.path.join(d,f)
        for image in os.listdir(imageDir):
            print(copyfile(os.path.join(imageDir,image), os.path.join(copydir,str(label)+ "_" + str(image))))

