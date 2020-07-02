import os
from shutil import copyfile

dic_path = './VOC2012/ImageSets/Main'
object_categories = ['aeroplane', 'bicycle', 'bird', 'boat',
        'bottle', 'bus', 'car', 'cat', 'chair',
        'cow', 'diningtable', 'dog', 'horse',
        'motorbike', 'person', 'pottedplant',
        'sheep', 'sofa', 'train', 'tvmonitor']
train_all = []
val_all = []

source = './VOC2012/JPEGImages/'


def read_all():
    for i,str in enumerate(object_categories,long(1)):
        print(str)
        if not os.path.exists('train/'+str+'/'):
            os.makedirs('train/'+str+'/')
        if not os.path.exists('val/'+str+'/'):
            os.makedirs('val/'+str+'/')

        # train
        f = open(dic_path+"/"+str+'_train.txt')
        iter_f = iter(f)
        for line in iter_f:
            if(int((line[12:14])) == 1):
                line = line[0:11]
                copyfile(source+line+'.jpg','train/'+str+'/'+line+'.jpg')


        # val
        f = open(dic_path+"/"+str+'_val.txt')
        iter_f = iter(f)
        for line in iter_f:
            if(int((line[12:14])) == 1):
                line = line[0:11]
                copyfile(source+line+'.jpg','val/'+str+'/'+line+'.jpg')


read_all()
# print(train_all)