import base64
Base64code="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+/="

def Encrypt():
    s=input("请输入需加密语句：")
    s=bytes(s,encoding='utf-8')
    st=base64.b64encode(s)
    print("加密后语句为",st)

def Decrypt():
    a=-1
    while a==-1:
        s=input("请输入需解密语句：")
        num=len(s)
        
        if len(s)%4==0:
            a=1
        else:
            print("输入的为非法语句，请重新输入\n")
            
        if a==1:
            for i in range(len(s)):
                a=Base64code.find(s[i])
                if a==-1:
                    print("输入的为非法语句，请重新输入\n")
                    break
                    
        if a==1:
            b=s.find("=")
            if b!=num-1 or b!=num-2 or b!=-1:
                print("输入的为非法语句，请重新输入\n")
                a=-1
                
    s=bytes(s,encoding='utf-8')
    st=base64.b64decode(s)
    print("解密后语句为",st)