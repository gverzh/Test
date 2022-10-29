import cv2,string
import numpy as np, os


data = []  # 输入图片的位置
outputpath = r"D:/1. 研究生/项目/MMA-Net/dataset/mixture"  # 图像输出位置
dataset_dir = r"D:/1. 研究生/项目/MMA-Net/dataset/VIL100"  # 图像1文件夹路径
output_dir = r"D:/1. 研究生/项目\MMA-Net/dataset/output/VIL100/60_lr0.001deay1e-6_sgd" # 模型图片路径，图像2输入路径

def read1():
    datapath = r"D:/1. 研究生/项目/MMA-Net/dataset/VIL100/data/test.txt"  # 测试数据集txt文件
    file = open(datapath,"r")
    for i in file.readlines():
        data.append(i.strip())

    # print(data)
    file.close()


# 中文路径问题
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img


read1()

for i in data:
    imagepath1 = dataset_dir+i
    imagepath2 = output_dir+i.replace("jpg","png")[11:]

    # img1 = cv2.imread(imagepath1)
    # img2 = cv2.imread(imagepath2)
    img1 = cv_imread(imagepath1)
    img2 = cv_imread(imagepath2)

    imgadd = cv2.add(cv2.resize(img1,(1280,720)), cv2.resize(img2,(1280,720)))
    # cv2.imshow('imgadd', imgadd)
    # cv2.imwrite((r"D:/1. 研究生/项目/MMA-Net/dataset/mixture")+i[11:], imgadd)

    dir = outputpath+i[11:(i.find("frames")+6)]
    print(dir)

    os.makedirs(dir, exist_ok=True)
    cv2.imencode('.jpg', imgadd)[1].tofile(r"D:/1. 研究生/项目/MMA-Net/dataset/mixture"+i[11:])
    # 其中image_array:图像数组；image_path图像的保存全路径

    cv2.waitKey(0)

print("文件保存在: "+outputpath)
