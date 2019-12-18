"""
使用Process创建两个子进程，同时复制
一个文件，分别复制前半部分和后半部分，
形成两个新的文件
"""
"""
父进程中创建IO，子进程从父进程中获取IO对象，实际上
他们操作的是同一个IO，属性相互影响
如果在各自进程中创建IO对象，那么这些IO对象互相没有
任何影响
"""
from multiprocessing import Process
import os

filename="./bc.jpeg"
size=os.path.getsize(filename)

# 复制上半部
def top():
    fr=open(filename,"rb")
    fw=open("/home/tarena/top.jpeg","wb")
    n=size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
# 复制下半部
def end():
    fr=open(filename,"rb")
    fw=open("/home/tarena/end.jpeg","wb")
    fw.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()
p1=Process(target=top)
p2=Process(target=end)
p1.start()
p1.join()
p2.start()
p2.join()