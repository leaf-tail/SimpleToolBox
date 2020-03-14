import json
def Creatbook():
    print("创建字典")
    book={}
    a=1
    
    while a==1:
        b=-1
        while b==-1:
            key=input("请输入字典的键：")
            if key in book:
                print("非法输入")
            else:
                b=1
       
        value=input("请输入字典的值：")
        book[key]=value
        a=int(input("是否继续创建字典（1代表是/0代表否）:"))
    
    return book

def Transjson(book):
    jstr=json.dumps(book)
    print("转换后的json字符串为：",jstr)
    print("类型为：",type(jstr))
    
def Reverse(book):
    re_book={}
    for k,v in book.items():
        if (v not in re_book):
            re_book[v]=k
        else:
            tem=re_book[v]
            re_book[v]=[tem,k]
            
    print("反转后的字典为：",re_book)
    print("类型为：",type(re_book))
