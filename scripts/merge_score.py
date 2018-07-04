import os
import pickle
import numpy as np

y_test_path = "/data0/EmotiW/Dlib/Crop/Face/Val/Val_video.txt"


f1="pred_val_vgg_video.txt"
f2 = "pred_val_res50_video.txt"
f3="pred_val_dense_video.txt"
f4 = "pred_val_dsn_vgg_video.txt"
f5 ="pred_val_fgnet_video.txt"


score1_list = [line.strip() for line in  open(f1,'r').readlines()]
score2_list = [line.strip() for line in  open(f2,'r').readlines()]
score3_list = [line.strip() for line in  open(f3,'r').readlines()]
score4_list = [line.strip() for line in  open(f4,'r').readlines()]
score5_list = [line.strip() for line in  open(f5,'r').readlines()]


label = [line.strip().split(' ')[1] for line in  open(y_test_path,'r').readlines()]
count = 0


for i in range(len(score4_list)):
    score1=[float(x) for x in score1_list[i].split(' ')]
    score2=[float(x) for x in score2_list[i].split(' ')]
    score3=[float(x) for x in score3_list[i].split(' ')]
    score4=[float(x) for x in score4_list[i].split(' ')]
    score5=[float(x) for x in score5_list[i].split(' ')]
    
    #scores = 4*np.array(score5) + np.array(score6)+ np.array(score4) + 6.5*np.array(score2)  
    #scores = 4*np.array(score5) + np.array(score6)+ np.array(score4) 
    #scores = np.array(score5) +  np.array(score2) 
    
    #scores=  (np.array(score6) + np.array(score4) + 4*np.array(score5))
    #scores = np.array(score3)+ 2.5*np.array(score4)+ 2.5*np.array(score6)
    #scores =  np.array(score4)+ np.array(score6)+ 0.25*np.array(score3)+ 4*np.array(score5)
    #scores=( (((np.array(score1)+np.array(score2))/2 + 2*np.array(score3))/3+ 4*np.array(score6))/5+ np.array(score4))/2 
    #scores = scores_1 + 2*np.array(score5)
    #print scores
    if int(scores.argmax(axis=0)) == int(label[i]):
        count += 1
    print "video",i,"predict",int(scores.argmax(axis=0)),"label",label[i]
print "accuracy", float(count)/369

