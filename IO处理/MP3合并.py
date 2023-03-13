
#coding=utf-8 
import os

class FileOperationBase(object):  
    def __init__(self, srcpath, despath, models, chunksize=1024):  
        self.chunksize = chunksize  
        self.srcpath = srcpath  
        self.despath = despath  
        self.models = models or "default"
  
    def splitFile(self):  
        'split the files into chunks, and save them into despath'  
        if not os.path.exists(self.despath):  
            os.mkdir(self.despath)  
        chunknum = 0  
        inputfile = open(self.srcpath, 'rb') #rb 读二进制文件
        try:  
            while 1:  
                chunk = inputfile.read(self.chunksize)  
                if not chunk: #文件块是空的
                    break  
                chunknum += 1  
                filename = os.path.join(self.despath, ("part--%04d" % chunknum))  
                fileobj = open(filename, 'wb')  
                fileobj.write(chunk)  
        except IOError:  
            print("read file error\n")  
            raise IOError  
        finally:  
            inputfile.close()  
        return chunknum  
  
    def mergeFile(self):  
        '将src路径下的所有文件块合并，并存储到des路径下。'  
        if not os.path.exists(self.srcpath):  
            print("srcpath doesn't exists, you need a srcpath")
            raise IOError  
        files = os.listdir(self.srcpath)  
        with open(self.despath, 'wb') as output:  
            for eachfile in files:  
                filepath = os.path.join(self.srcpath, eachfile)  
                filefullname = os.path.splitext(filepath)
                #if(filefullname[1] == '.mp3'):
                with open(filepath, 'rb') as infile:  
                    data = infile.read()  
                    output.write(data)  


def filemerge():
    filedir = os.getcwd() + '/yuliao'
    filenames = os.listdir(filedir)
    f = open('merge.mp3','w')
    for filename in filenames:
        filepath = filedir + '/' + filename
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
    f.close()

if __name__ == '__main__':
    filemerge = FileOperationBase(r'E:\Users\平平\Desktop\1\MP3',r'E:\Users\平平\Desktop\1\当我遇上你.mp3')
    filemerge.mergeFile()