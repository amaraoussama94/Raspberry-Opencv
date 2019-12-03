import cv2
import numpy as np
import time
import sys


############Trait img
def laitue(pic) :
    #############################################################################
    #collect Green
    lowerBound1=np.array([65,26,56]) #  min limits green color object of each pixels
    upperBound1=np.array([124,238,255]) # max limits green color object of each pixels

        ########################################################################################
    

    #2d matrix called kernal which is basically to control the effects of opening and closing
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((6,6))
    ###################################################################################
    # create the Filter of  diff rang  of Green
    mask1=cv2.inRange(pic,lowerBound1,upperBound1)
    #Find contours from this mask

    maskT=mask1+mask2+mask3+mask4+mask5+mask6
    ################################################################################"
    #morphology ;cleaning all the noise
    maskOpen=cv2.morphologyEx(maskT,cv2.MORPH_OPEN,kernelOpen)
    #creation dune  zone 
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    ##################################################################################
    #Find contours from this mask
    maskFinal=maskClose

    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #draw Contours
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    #imwrite("img.jpg",img) #save  img
    #################################################################################
    #cal Dist
    maskClose = cv2.medianBlur(maskClose,9)
    rows,cols= maskClose.shape
    print(rows  , cols)
    i=215
    d=0
    for j in range(cols):
        k = maskClose[i,j]
        #print(j,k)
        if (k>200):
         d=d+1
    d=d*0.5+0.5
    print(d)
    
    ############################################################################    
    #mouv
    #val app
    if len(conts) > 0:
        c = max(conts, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print("cx= %d",cx)
        print("cy=%d",cy)
        if cx >= 120:
	        print("Tourner a gauche")
	        
        elif cx < 120 and cx > 50:
                print("Avant")
                
        elif cx <= 50:
                print("Tourner a droite")
                

    return (maskClose,maskOpen,maskT,img)


def articho(pic) :
    #############################################################################
    #collect 
    lowerBound1=np.array([45,45,44]) #  min limits green color object of each pixels
    upperBound1=np.array([59,171,176]) # max limits green color object of each pixels

    ########################################################################################
    

    #2d matrix called kernal which is basically to control the effects of opening and closing
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((6,6))
    ###################################################################################
    # create the Filter of  diff rang  of Green
    mask1=cv2.inRange(pic,lowerBound1,upperBound1)
 
    maskT=mask1+
    ################################################################################"
    #morphology ;cleaning all the noise
    maskOpen=cv2.morphologyEx(maskT,cv2.MORPH_OPEN,kernelOpen)
    #creation dune  zone 
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    ##################################################################################
    #Find contours from this mask
    maskFinal=maskClose

    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #draw Contours
    cv2.drawContours(img,conts,-1,(255,0,0),3)

    #imwrite("img.jpg",img) #save  img
    #################################################################################
    #cal Dist
    maskClose = cv2.medianBlur(maskClose,9)
    rows,cols= maskClose.shape
    print(rows  , cols)
    i=215
    d=0
    for j in range(cols):
        k = maskClose[i,j]
        print(j,k)
        if (k>200):
         d=d+1
    d=d*0.5+0.5
    print(d)

    ############################################################################    
    #mouv
    #val app
    if len(conts) > 0:
        c = max(conts, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print("cx= %d",cx)
        print("cy=%d",cy)
        if cx >= 120:
	        print("Tourner a gauche")
	        
        elif cx < 120 and cx > 50:
                print("Avant")
                 
        elif cx <= 50:
                print("Tourner a droite")
                

    return (maskClose,maskOpen,maskT,img)

#main()


while True :

        
        ### Trait  img
        # Get the next frame.
        img=cv2.imread("20.jpg")
        img=cv2.resize(img,(340,220))#resize it to make it a small fixed size for faster processing
        ##############################################################################
        #Rotation  d image
        #rows,cols,dim= img.shape
        #M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        #img = cv2.warpAffine(img,M,(cols,rows))
        #translation
        #num_rows, num_cols = img.shape[:2]
        #translation_matrix = np.float32([ [1,0,20], [0,1,0] ])# x y
        #img= cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
        ########################################################################################
        # region d interest
        #height=img.shape[0] # dim image
        #polygons=np.array([
        #    [(20,height),(289,height),(170,130)]
        #    ])
        #mask=np.zeros_like(img) 
        #cv2.fillPoly(mask,polygons,[255,255,255])
        #masked_image=cv2.bitwise_and(img,mask) #som mat


        ########################
        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        a=input("select 1-laitus 2-articho")
        if (a=='1'):
                maskClose,maskOpen,maskT,img=laitue(imgHSV)
                #################################################################################
                cv2.imshow("maskClose",maskClose)
                cv2.imshow("maskOpen",maskOpen)
                cv2.imshow("mask",maskT)
                cv2.imshow("cam",img)
                cv2.waitKey(10)

        elif (a=='2'):
                maskClose,maskOpen,maskT,img=articho(imgHSV)
                #################################################################################
                cv2.imshow("maskClose",maskClose)
                cv2.imshow("maskOpen",maskOpen)
                cv2.imshow("mask",maskT)
                cv2.imshow("cam",img)
                cv2.waitKey(10)

        else :    
                print("erreur")
                sys.exit()


