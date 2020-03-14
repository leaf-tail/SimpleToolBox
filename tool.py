import Package


print("欢迎使用简易工具箱：\n 1 Base64加密\n 2 Base64解密\n 3 自定义字典并转换为json字符串且原字典键值反转\n 4 读取txt文件内容并转换为QRcode\n 5 退出")
a=0

while a!='5':
    a=input("请输入所需功能前的序号：")
    if (a=='1'):
        C.Encrypt()
    elif (a=='2'):
        C.Decrypt()
    elif (a=='3'):
        book=D.Creatbook()
        D.Transjson(book)
        D.Reverse(book)
    elif (a=='4'):
        txt=M.Read()
        M.Make(txt)