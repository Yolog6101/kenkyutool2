"3D plot with Distance Image(Depth map) for gif"

import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import cv2
from io import BytesIO
from PIL import Image
import sys

def make(file,elev,azim):
    fig=plt.figure()
    ax=fig.add_subplot(projection='3d')
    
    
    depth=cv2.imread(file)[:,:,0]
    lenx=depth.shape[0]
    leny=depth.shape[1]
    img=cv2.imread("./data/Color/"+os.path.basename(file).split(sys.argv[1])[0]+".png")
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB).astype(np.float32)
    img=(img/255).astype(np.float32)


    xlist=[]
    ylist=[]
    cmap=[]
    zlist=[]
    for y in range(0,leny):
        for x in range(0,lenx):
            xlist.append(x)
            ylist.append(y)
            cmap.append([img[y][x][0],img[y][x][1],img[y][x][2]])
            zlist.append(depth[y][x])
               

    colormap=np.array(cmap)
                    
    xarray=np.array(xlist,dtype=np.uint8)
    yarray=np.array(ylist,dtype=np.uint8)
    zarray=np.array(zlist,dtype=np.uint8)


    ax.scatter(zarray,xarray,yarray,marker=".",color=colormap)
    ax.set_xlabel("Depth(distance)")
    ax.set_ylabel("x")
    ax.set_zlabel("y")
    ax.invert_yaxis()
    ax.invert_zaxis()

    ax.view_init(elev=0+elev,azim=0+azim)

    buf=BytesIO()
    fig.savefig(buf)
    plt.clf()
    plt.close()
    return Image.open(buf)



if __name__=="__main__":
    frame=[]
    filelist=glob.glob("./data/Depth/*"+sys.argv[1])
    for file in filelist:
        print(file)#Depthデータ
        frame=[make(file,d_elev,0) for d_elev in range(-20,20)]

        frame[0].save("./result/sample_"+os.path.basename(file).split(sys.argv[1])[0]+".gif",save_all=True,append_images=frame[1:],loop=0)

    




    
       
        


