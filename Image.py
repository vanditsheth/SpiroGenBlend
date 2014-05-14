#Generate a spirograph, blend it with another image and then apply filters.
#Made by:- Vandit Sheth

from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
import math

#Setting the ALPHA value for blending
ALPHA=0.3

def display():
    global ALPHA
    i=0
    j=0
    glPushMatrix()
    #The loop to generate spirograph image with lines.
    glBegin(GL_LINES)
    for i in range(-200,200,1):
        #The colors are imported from a color palette file.
        file=open('palette.txt',"r+")
        for j in range(-200,200,1):
            #Read color line by line
            tmp=file.readline()
            tmp=tmp.strip('\n')
            tmp=tmp.split(' ,')
            glColor3d(float(tmp[0]), float(tmp[1]), float(tmp[2]))
            #The Spirograph equation in terms of sin and cos. The multipliers can be changed to generate different spirographs.
            #Different equations can be used to generate different images. Presently it uses the spirograph algorithm
            x=(6)*cos(j) + cos((10)*j) 
            y=(6)*sin(j) + sin((10)*j) 
            glVertex2d(x,y)
        file.close()
    glEnd()
    glFlush()
    glPopMatrix()
    
    #Get the image height and width from viewport
    ox, oy, width, height = glGetIntegerv(GL_VIEWPORT)
    
    #The values of pixels of the generated image is stored in the array 'a'
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    a=glReadPixels(0,0,width,height,GL_RGBA,GL_UNSIGNED_BYTE)
    image = Image.fromstring("RGBA", (width,height), a)
    image=image.transpose(Image.FLIP_TOP_BOTTOM)
    
    #The image is stored as png for transparency which will help in blending.
    image.save("RandomImage.png","PNG")
    image.save("RandomImage.jpg","JPEG")
    im1 = Image.open("RandomImage.png")

    #Checking if the file exists
    try:
        im2 = Image.open("Design.png")
    except:
        print 'No Design image found. Please keep one with the name Design.png'
        exit()

    #Cropping the image in-case it doesn't fit the size
    box=[0,0,400,400]
    im2=im2.crop(box)
    #The generated image is blended with a stored design image.
    Im=Image.blend(im1,im2,ALPHA)
    Im.save("Blended_ORIGINAL.jpg","JPEG")

    #Different filters are applied on the blended image.

    #Black and White filter
    ImBW = Im.convert('1')
    ImBW.save('Blended_B&W.jpg',"JPEG")
    
    #Min filter
    ImMin = Im.filter(ImageFilter.MinFilter(3))
    ImMin.save('Blended_MIN.jpg',"JPEG")
    
    #Max filter
    ImMax = Im.filter(ImageFilter.MaxFilter(3))
    ImMax.save('Blended_MAX.jpg',"JPEG")
    
    #Median filter
    ImMedian = Im.filter(ImageFilter.MedianFilter(size=3))
    ImMedian.save('Blended_MEDIAN.jpg',"JPEG")
    
    #Mode filter
    ImMode = Im.filter(ImageFilter.ModeFilter(size=3))
    ImMode.save('Blended_MODE.jpg',"JPEG")
    
    #Invert image (obtain negative)
    ImInv = ImageChops.invert(Im)
    ImInv.save('Blended_INV.jpg',"JPEG")
         
    #BLUR filter
    ImBlur = Im.filter(ImageFilter.BLUR)
    ImBlur.save('Blended_BLUR.jpg',"JPEG")
     
    #Gaussian BLUR filter
    ImGBlur = Im.filter(ImageFilter.GaussianBlur(radius = 20))
    ImGBlur.save('Blended_GAUSSIANBLUR.jpg',"JPEG")
    
    #CONTOUR filter
    ImContour = Im.filter(ImageFilter.CONTOUR)
    ImContour.save('Blended_CONTOUR.jpg',"JPEG")
     
    #DETAIL filter
    ImDetail = Im.filter(ImageFilter.DETAIL)
    ImDetail.save('Blended_DETAIL.jpg',"JPEG")
     
    #EDGE_ENHANCE filter
    ImEH = Im.filter(ImageFilter.EDGE_ENHANCE)
    ImEH.save('Blended_EDGEENHANCE.jpg',"JPEG")
     
    #EDGE_ENHANCE_MORE filter
    ImEHM = Im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    ImEHM.save('Blended_EEM.jpg',"JPEG")
     
    #EMBOSS filter
    ImEmb = Im.filter(ImageFilter.EMBOSS)
    ImEmb.save('Blended_EMBOSS.jpg',"JPEG")
     
    #FIND_EDGES filter
    ImEdges = Im.filter(ImageFilter.FIND_EDGES)
    ImEdges = ImEdges.save('Blended_FIND_EDGES.jpg',"JPEG")
     
    #SMOOTH filter
    ImSmooth = Im.filter(ImageFilter.SMOOTH)
    ImSmooth = ImSmooth.save('Blended_SMOOTH.jpg',"JPEG")
     
    #SMOOTH_MORE filter
    ImSmoothMore = Im.filter(ImageFilter.SMOOTH_MORE)
    ImSmoothMore = ImSmoothMore.save('Blended_SMOOTH_MORE.jpg',"JPEG")
     
    #SHARPEN filter
    ImSharp = Im.filter(ImageFilter.SHARPEN)
    ImSharp = ImSharp.save('Blended_SHARPEN.jpg',"JPEG")

    ImS = Im.filter(ImageFilter.Kernel((3,3),[],None,0)
    ImS.save('Blended_SHEN.jpg',"JPEG")

    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(0, 0)
glutCreateWindow("Spirograph")
glutDisplayFunc(display)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-10,10,-10,10,-10,10)
glutMainLoop()
