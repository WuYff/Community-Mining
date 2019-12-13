from PIL import Image
import os

# # 裁剪图片
def image_crop(root, m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            path = root + 'test/{}.gif'.format(str(j))
            print(path)
            image = Image.open(path)
            if image.mode == "P":
                image = image.convert('RGB')
            width = image.width
            height = image.height
            image2 = image.crop((width/2-220, height/2-240, width/2+220, height/2+200))
            newPath = root + 'temp/{}.gif'.format(str(j))
            print(newPath)
            image2.save(newPath)

def image_crop_single(path):
    image = Image.open(path)
    if image.mode == "P":
        image = image.convert('RGB')
    width = image.width
    height = image.height
    image2 = image.crop((width / 2 - 220, height / 2 - 240, width / 2 + 220, height / 2 + 200))
    image2.save(path)

# # 图像二值化
def image_binary(root, m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            path = root + 'temp/{}.gif'.format(str(j))
            img = Image.open(path)
            img = img.convert('L')
            table = []
            threshold = 160
            print(img.getpixel((1, 1)))
            if img.getpixel((1, 1)) < 180:  #深色为底色
                for k in range(256):
                    if k < threshold:
                        table.append(0)
                    else:
                        table.append(1)
            else:                             #浅色为底色
                for k in range(256):
                    if k < threshold:
                        table.append(1)
                    else:
                        table.append(0)
            # 图片二值化
            photo = img.point(table, '1')
            photo.save(root + 'res/{}.gif'.format(str(j)))
def image_binary_single(path):
    img = Image.open(path)
    img = img.convert('L')
    table = []
    threshold = 160
    print(img.getpixel((1, 1)))
    if img.getpixel((1, 1)) < 180:  # 深色为底色
        for k in range(256):
            if k < threshold:
                table.append(0)
            else:
                table.append(1)
    else:  # 浅色为底色
        for k in range(256):
            if k < threshold:
                table.append(1)
            else:
                table.append(0)
    # 图片二值化
    photo = img.point(table, '1')
    photo.save(path)

def changeFileName(path):
    # 获取该目录下所有文件，存入列表中
    filelist = os.listdir(path)
    n = 0
    for i in filelist:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + filelist[n]  # os.sep添加系统分隔符
        # 设置新文件名
        newname = path + os.sep + str(n + 1) + '.jpg'
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)
        n += 1

# 创建文件夹
def createFile(path, m):
    for i in range(1, m+1):
        filepath = path + 'class{}'.format(str(i))
        print(filepath)
        os.mkdir(filepath)

# root = '/Users/yulin1998/Downloads/'
# path1 = root + 'CM_images_jpg/'
# path2 = root + 'temp/'
# path3 = root + 'res/'

# createFile(path2, 21)
# createFile(path3, 21)


# image_crop(root, 3, 9)
# image_binary(root, 3, 9)
# image_crop(root, 1, 13)
# image_binary(root, 1, 13)

# files = os.listdir(path)
# print(os.sep)
# for file in files:
#     index = 1
#     for img in os.listdir(path + '/{}'.format(file)):
#         newName = '{}.jpg'.format(str(index))
#         os.rename(img, newName)
#         index = index + 1

path = '/Users/yulin1998/Downloads/CM_images_rename/'
# fileList = os.listdir(path)
# print(fileList)
# for file in fileList:
#     subFilePath = path + file
#     for img in os.listdir(subFilePath):
#         imgPath = subFilePath + os.sep + img
#         print(imgPath)
#         image_crop_single(imgPath)
#         image_binary_single(imgPath)
# changeFileName(path + 'C1')
filelist = os.listdir(path + 'C1')
print(filelist)
# filelist = os.listdir(path)
# for file in filelist:
#     subFilePath = path + file
#     changeFileName(subFilePath)
