import os

#path = r"C:\Users\95340\Desktop\2018-A-打印\保险"
path = input(r"请输入需要改名的文件所在路径")
filelist = os.listdir(path)
namelist_f = list(range(200))
for c in range(0,200):
    namelist_f[c] = "daugacigduscdsc"
for count in range(0,200):
    namelist_f[count] = input("粘贴学生列表，结束后请输入end: ")
    if namelist_f[count] == "end":
        break
namelist = [str(ixx) for ixx in namelist_f]

name_num = 0
for name in namelist:
    name_num += 1
    n = 0
    for i in filelist:
        n += 1
        if name in i:
            #print(name,i,'name_n=',name_num,'n=',n)
            oldname = path+os.sep+ i
            newname = path+os.sep+str(name_num)+'-'+i
            print(newname)
            os.rename(oldname,newname)
    #     n +=1
    #     if i.find(name) != -1:
    #         oldname = path+ os.sep + filelist[n]
    #         newname = path + os.sep + str(name_num)+'-'+filelist[n]
    #         os.rename(oldname,newname)
    #         print(oldname,'->',newname)
    