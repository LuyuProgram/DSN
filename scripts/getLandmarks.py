import os
import time
import cv2
import sys
import dlib
import glob
from skimage import io
from multiprocessing.dummy import Pool as ThreadPool


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

root = "/data0/EmotiW/Dlib/Crop/Test/"
root_list = "/data0/EmotiW/Dlib/list/Test/"
root_landmark = "/data0/EmotiW/Dlib/landmarks/Test/"

def single_list(list):
    dir_land = list.split('.')[0]
    img_list = open(root_list+list,'r')
    for l in img_list.readlines():
        filepath = l.strip('\n')
        #img = cv2.imread(filepath)
        dir_ori = filepath.split('/')[-2]
        file_ori = filepath.split('/')[-1]
        #dir_check = root+dir_ori+'_check'
        dir_landmark = root_landmark+dir_land+'/'+dir_ori
        if os.path.exists(dir_landmark):
            pass
        else:
            #os.makedirs(dir_check)
            os.makedirs(dir_landmark) 

        print("Processing file: {}".format(filepath))
        img = io.imread(filepath)
        dets = detector(img, 1)       
        if len(dets) > 0 :
            for index, face in enumerate(dets):
                shape = predictor(img, face)
                f = open(dir_landmark+'/'+file_ori.split('.')[0]+'_landmarks.txt','w')
                f.write(str(shape.part(0).x)+' '+str(shape.part(0).y)+'\n')
                f.write(str(shape.part(1).x)+' '+str(shape.part(1).y)+'\n')
                f.write(str(shape.part(2).x)+' '+str(shape.part(2).y)+'\n')
                f.write(str(shape.part(3).x)+' '+str(shape.part(3).y)+'\n')
                f.write(str(shape.part(4).x)+' '+str(shape.part(4).y)+'\n')
                f.write(str(shape.part(5).x)+' '+str(shape.part(5).y)+'\n')
                f.write(str(shape.part(6).x)+' '+str(shape.part(6).y)+'\n')
                f.write(str(shape.part(7).x)+' '+str(shape.part(7).y)+'\n')
                f.write(str(shape.part(8).x)+' '+str(shape.part(8).y)+'\n')
                f.write(str(shape.part(9).x)+' '+str(shape.part(9).y)+'\n')
                f.write(str(shape.part(10).x)+' '+str(shape.part(10).y)+'\n')
                f.write(str(shape.part(11).x)+' '+str(shape.part(11).y)+'\n')
                f.write(str(shape.part(12).x)+' '+str(shape.part(12).y)+'\n')
                f.write(str(shape.part(13).x)+' '+str(shape.part(13).y)+'\n')
                f.write(str(shape.part(14).x)+' '+str(shape.part(14).y)+'\n')
                f.write(str(shape.part(15).x)+' '+str(shape.part(15).y)+'\n')
                f.write(str(shape.part(16).x)+' '+str(shape.part(16).y)+'\n')
                f.write(str(shape.part(17).x)+' '+str(shape.part(17).y)+'\n')
                f.write(str(shape.part(18).x)+' '+str(shape.part(18).y)+'\n')
                f.write(str(shape.part(19).x)+' '+str(shape.part(19).y)+'\n')
                f.write(str(shape.part(20).x)+' '+str(shape.part(20).y)+'\n')
                f.write(str(shape.part(21).x)+' '+str(shape.part(21).y)+'\n')
                f.write(str(shape.part(22).x)+' '+str(shape.part(22).y)+'\n')
                f.write(str(shape.part(23).x)+' '+str(shape.part(23).y)+'\n')
                f.write(str(shape.part(24).x)+' '+str(shape.part(24).y)+'\n')
                f.write(str(shape.part(25).x)+' '+str(shape.part(25).y)+'\n')
                f.write(str(shape.part(26).x)+' '+str(shape.part(26).y)+'\n')
                f.write(str(shape.part(27).x)+' '+str(shape.part(27).y)+'\n')
                f.write(str(shape.part(28).x)+' '+str(shape.part(28).y)+'\n')
                f.write(str(shape.part(29).x)+' '+str(shape.part(29).y)+'\n')
                f.write(str(shape.part(30).x)+' '+str(shape.part(30).y)+'\n')
                f.write(str(shape.part(31).x)+' '+str(shape.part(31).y)+'\n')
                f.write(str(shape.part(32).x)+' '+str(shape.part(32).y)+'\n')
                f.write(str(shape.part(33).x)+' '+str(shape.part(33).y)+'\n')
                f.write(str(shape.part(34).x)+' '+str(shape.part(34).y)+'\n')
                f.write(str(shape.part(35).x)+' '+str(shape.part(35).y)+'\n')
                f.write(str(shape.part(36).x)+' '+str(shape.part(36).y)+'\n')
                f.write(str(shape.part(37).x)+' '+str(shape.part(37).y)+'\n')
                f.write(str(shape.part(38).x)+' '+str(shape.part(38).y)+'\n')
                f.write(str(shape.part(39).x)+' '+str(shape.part(39).y)+'\n')
                f.write(str(shape.part(40).x)+' '+str(shape.part(40).y)+'\n')
                f.write(str(shape.part(41).x)+' '+str(shape.part(41).y)+'\n')
                f.write(str(shape.part(42).x)+' '+str(shape.part(42).y)+'\n')
                f.write(str(shape.part(43).x)+' '+str(shape.part(43).y)+'\n')
                f.write(str(shape.part(44).x)+' '+str(shape.part(44).y)+'\n')
                f.write(str(shape.part(45).x)+' '+str(shape.part(45).y)+'\n')
                f.write(str(shape.part(46).x)+' '+str(shape.part(46).y)+'\n')
                f.write(str(shape.part(47).x)+' '+str(shape.part(47).y)+'\n')
                f.write(str(shape.part(48).x)+' '+str(shape.part(48).y)+'\n')
                f.write(str(shape.part(49).x)+' '+str(shape.part(49).y)+'\n')
                f.write(str(shape.part(50).x)+' '+str(shape.part(50).y)+'\n')
                f.write(str(shape.part(51).x)+' '+str(shape.part(51).y)+'\n')
                f.write(str(shape.part(52).x)+' '+str(shape.part(52).y)+'\n')
                f.write(str(shape.part(53).x)+' '+str(shape.part(53).y)+'\n')
                f.write(str(shape.part(54).x)+' '+str(shape.part(54).y)+'\n')
                f.write(str(shape.part(55).x)+' '+str(shape.part(55).y)+'\n')
                f.write(str(shape.part(56).x)+' '+str(shape.part(56).y)+'\n')
                f.write(str(shape.part(57).x)+' '+str(shape.part(57).y)+'\n')
                f.write(str(shape.part(58).x)+' '+str(shape.part(58).y)+'\n')
                f.write(str(shape.part(59).x)+' '+str(shape.part(59).y)+'\n')
                f.write(str(shape.part(60).x)+' '+str(shape.part(60).y)+'\n')
                f.write(str(shape.part(61).x)+' '+str(shape.part(61).y)+'\n')
                f.write(str(shape.part(62).x)+' '+str(shape.part(62).y)+'\n')
                f.write(str(shape.part(63).x)+' '+str(shape.part(63).y)+'\n')
                f.write(str(shape.part(64).x)+' '+str(shape.part(64).y)+'\n')
                f.write(str(shape.part(65).x)+' '+str(shape.part(65).y)+'\n')
                f.write(str(shape.part(66).x)+' '+str(shape.part(66).y)+'\n')
                f.write(str(shape.part(67).x)+' '+str(shape.part(67).y)+'\n')

                f.close()
                
       
if __name__ == '__main__':
    testlist=['4.txt','5.txt']
    pool = ThreadPool(2)
    pool.map(single_list,testlist)
    pool.close()
    pool.join()
