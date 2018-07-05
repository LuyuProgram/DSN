import subprocess
import glob
import os
import sys


def get_output_size(path, width = 1024):

    command = ["ffprobe", path]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    res = p.communicate()[0]
    asr = res[res.find("DAR "):].split(']')[0][4:].split(':')
    try:
        asr = map(float, asr)
    except ValueError:
        asr = res[res.find("DAR "):].split(' ')[1].split(':')
        asr[1] = asr[1].split(",")[0]
        asr = map(float, asr)

    height = int(width / (asr[0]/asr[1]))
    return "{}x{}".format(width, height)


def extract_frames(src, dest, asr):
   
    print src
    print asr
    print dest
    
    command = ["ffmpeg", "-i", src, "-s", asr, "-qscale", "1", dest]
    subprocess.call(command)
    
if __name__ == "__main__":
    avi_path = "/data0/EmotiW/OriginalData/Test/"
    img_path = "/data0/EmotiW/Frames/Test/"
    file_list = glob.glob("{}/*.avi".format(avi_path))
    file_list.sort()  
    error = 0
    for f in range(0, file_list.__len__()):
        try:
            aviName = file_list[f].split('/')[-1].rstrip('.avi')              
            save_path = "{}/{}".format(img_path, aviName)
        
            if not os.path.isdir(save_path):
                os.makedirs(save_path)
                            
            print file_list[f], '\n'
            print save_path, '\n'
            output = "{}/{}-%3d.png".format(save_path,aviName)
            print 'get aspect ratio'
            asr = get_output_size(file_list[f])         
            print 'asr: ', asr, '\n'
            print 'extract frames'
            extract_frames(file_list[f], output, asr)
            print aviName + ' done' + '\n'
        except:
            error += 1
            print aviName + ' failed' + '\n'
    