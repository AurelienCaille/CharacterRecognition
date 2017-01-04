#!/usr/bin/env python2
from openMNIST import load_mnist

images, labels = load_mnist()
dic = {}

"""
create a dictionnaire with 
the values of the image 
linked to
the number of pixel with the values greater than 200 
divided by the number of images
"""
print "Test images[0]"
for image in range(len(labels)):
    for lines in images[image]
        for pixel in lines:
            if pixel > 200:
                dic[str(labels[image][0])] = dic.get(str(labels[image][0]), 0) + 1
print(dic)
for key in dic:
    dic[key] = float(dic[key]) / 60000
print (dic)


#{'0': 0.6958666666666666, 
#'5': 0.4690666666666667, 
#'2': 0.5751666666666667, 
#'7': 0.47428333333333333, 
#'6': 0.5247166666666667, 
#'9': 0.4780333333333333, 
#'3': 0.6033833333333334, 
#'1': 0.40031666666666665, 
#'8': 0.5376666666666666, 
#'4': 0.4795333333333333}


