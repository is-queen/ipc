'''将image_path文件夹下的图片resize成（w，h）重命名并保存'''
import cv2
import os
def Resize_Image(image_path,w=347,h=347):
    image_path_list = os.listdir(image_path)
    image_path_list.sort()
    number=1
    for filename in image_path_list:
        file = image_path+'/'+filename
        img = cv2.imread((file), cv2.IMREAD_COLOR)
        # 调用cv2.resize函数resize图片
        new_img = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)
        img_name = str(number)+'.jpg'
        number+=1
        '''生成图片存储的目标路径'''
        save_path = image_path + '_new/'
        if os.path.exists(save_path):
            print(number)
            '''调用cv.2的imwrite函数保存图片'''
            save_img = save_path + img_name
            cv2.imwrite(save_img, new_img)
        else:
            os.mkdir(save_path)
            save_img = save_path + img_name
            cv2.imwrite(save_img, new_img)

#Resize_Image('图片文件夹路径')
Resize_Image('E:\pycharm-test\ipc\image_path')
