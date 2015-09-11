#encoding=utf-8
#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

#在一个分配的目录里面得到所有文件
def get_files(path):
        filepath=os.listdir(path)
        print filepath
        files=[]
        for fp in filepath:
                fppath=path+fp
                print fppath
                if(os.path.isfile(fppath)):
                        files.append(fppath)
                elif(os.path.isdir(fppath)):
                        fppath+='\\'
                try:
                        files+=get_files(fppath)#递归
                except WindowsError:
                            pass
        return files
        

#在特定的文件里面计算行数和空行和注释行

def count_lines(files):
    line,blank,note=0,0,0
    for filename in files:
            f=open(filename,'rb')
            for l in f:
                l=l.strip()
                line +=1
                if l==' ':
                    blank+=1
                elif l=='#':
                    note+=1
            f.close()
    return (line,blank,note)

if __name__=='__main__':
    files=get_files(raw_input("> "))
    print files
    lines=count_lines(files)
    print 'Line(s): %d,blank line(s): %d,note line(s): %d' % (lines[0],lines[1],lines[2])
    
