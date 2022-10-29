import numpy as np, os
import cv2
import time


datapath = r"D:\1. 研究生\项目\MMA-Net\dataset\mixture"  # 输入图片路径
outputdirpath = r"D:\1. 研究生\项目\MMA-Net\dataset\video"  # 输出视频路径

# 中文路径
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img


# 图片合成视频
def picvideo(path,outpath, size):
    filelist = os.listdir(path)  # 获取该目录下的所有文件名
    print(filelist)
    filelist.sort(key=lambda x: int(x[:-4]))  ##文件名按数字排序
    fps = 10
    # file_path = r"/media/result/result/img/" + str(int(time.time())) + ".mp4"  # 导出路径
    file_path = outputdirpath+'\\'+outpath+".mp4"
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for item in filelist:
        if item.endswith('.jpg'):  # 判断图片后缀是否是.png
            item = path + '/' + item
            print(item)
            # img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            img = cv_imread(item)
            video.write(img)  # 把图片写进视频

    video.release()  # 释放


dirlist = os.listdir(datapath)
for i in dirlist:
    # for j in os.listdir(datapath+'/'+i):
    picvideo(datapath+'\\'+i,i, (1280, 720))

print("视频保存在： "+outputdirpath)

# picvideo(image_path, (1280, 720))

