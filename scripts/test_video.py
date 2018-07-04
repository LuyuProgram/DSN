import numpy as np
import time
import os
import sys
import json
import sys
import socket
import logging
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import caffe
import random
import copy
import pickle
from collections import defaultdict 
caffe.set_mode_gpu()
caffe.set_device(6)

MODEL_DEF = 'deploy.prototxt'
MODEL_PATH = 'dsn_vgg_iter_300000.caffemodel'

SIZE = 256 #256
CROP_SIZE = 224 #224

mean = np.array((104.0, 117.0, 123.0), dtype=np.float32)
def predict(image,the_net):
    inputs = []
    try:
        tmp_input = image
        tmp_input = cv2.resize(tmp_input,(SIZE,SIZE))
        tmp_input = tmp_input[16:16+224,16:16+224];
        tmp_input = np.subtract(tmp_input,mean)
        tmp_input = tmp_input.transpose((2, 0, 1))
        tmp_input = np.require(tmp_input, dtype=np.float32)
    except Exception as e:
        raise Exception("Image damaged or illegal file format")
        return
    the_net.blobs['data'].reshape(1, *tmp_input.shape)
    the_net.reshape()
    the_net.blobs['data'].data[...] = tmp_input
    the_net.forward()
    scores = the_net.blobs['prob'].data[0]
    return copy.deepcopy(scores)

if __name__=="__main__":
    f = open("/data0/EmotiW/Dlib/Crop/Face/Val/Val_video.txt","rb")
    f_w = open("pred_val_dsn_vgg_video.txt","wb")
    net = caffe.Net(MODEL_DEF, MODEL_PATH, caffe.TEST)
    count = 0
    acc = 0

    
    for line in f.readlines():
        line = line.strip().split(" ")
        video_label = line[1]
        imgs = os.listdir(line[0])
        indexs = range(len(imgs))
        random.shuffle(indexs)
        scores= 0
        count += 1
        if count==1:
            start_time = time.time()
        imgs = [imgs[i] for i in indexs]
        
        for img in imgs:
            img_ = line[0]+'/'+str(img)
            cv_img = cv2.imread(img_)
            score = predict(cv_img,net)
            scores += score
            
        if int(scores.argmax(axis=0)) == int(video_label):
            acc += 1

    
    

        print "video",line[0],"predict",int(scores.argmax(axis=0)),"label",video_label
    
        #f_w.write(line[0]+" "+str(int(scores.argmax(axis=0)))+"\n")
        for i in scores:
            f_w.write(str(i)+' ')
        f_w.write('\n')
    f.close()
    f_w.close()

    
    
    print "acc total",acc
    print " total",count
    end_time = time.time()
    run_time = end_time - start_time
    print "accuracy: ", float(acc)/(count)
    print "run_time: ",run_time
    print "per_run_time: ",float(run_time)/count




