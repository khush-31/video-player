import os
def recmovieposterlist():
    fileList = []
    dirpath='recmovieposter'
    for f in os.listdir(dirpath):
        fpath = os.path.join(dirpath, f)
        if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg','.jfif')):
            fileList.append(fpath)
    return fileList

def recmoviename():
    l=recmovieposterlist()
    L=[]
    for i in l:
        l1=i.split('\\')
        l2=l1[1].split('.')
        L.append(l2[0])
    return L

recmovieposterlist()

