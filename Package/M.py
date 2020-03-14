import qrcode

def Read():
    ad=input("请输入文件的绝对路径：")
    f=open(ad,mode='r+')
    txt=f.read()
    f.close()
    return txt

def Make(txt):
    img=qrcode.make(txt)
    img_ad=input("请输入需保存二维码图片的完整路径（例如：D:\img\qrcode.jpg)：")
    img.save(img_ad)