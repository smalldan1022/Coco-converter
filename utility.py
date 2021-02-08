import cv2


def x_y_convert(contours):
    
    """
    input:  contours -> the contours of your image mask
    output: coco     -> a list of coco format cordinates
    """
    
    coco = []
    counter = 0

    for segment in contours:

        coco.append([])

        for element in segment:

            x = element[0][0]
            y = element[0][1]

            coco[counter].append(x)
            coco[counter].append(y)

        counter += 1
    
    return coco


def Get_x_y_and_Area(img_path):
    
    """
    input:  img_path -> the coco annotations
    output: contours -> a list of bbox cordinates
            area     -> a list of bbox cordinates
    """
 
    img = cv2.imread(img_path)
    
    tmp_img = img.copy()

    gray = cv2.cvtColor(tmp_img,cv2.COLOR_BGR2GRAY)  

    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  

    contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(tmp_img,contours,-1,(255,255,255),-1)

    area = (tmp_img==255).sum()

    return contours, area

def Find_the_bbox(annotations):
    
    """
    input:  annotations -> the coco format annotations
    output: bbox        -> a list of bbox cordinates , i.e:[0,155,23,56]
    """
    
    bbox_0 = 1000
    bbox_1 = 1000
    bbox_2 = 0
    bbox_3 = 0
    
    for annotation in annotations:
 
        bbox_0 = int( min(bbox_0, min(annotation[0::2])) )
        bbox_1 = int( min(bbox_1, min(annotation[1::2])) )
        bbox_2 = int( max(bbox_2, max(annotation[0::2]) ) )
        bbox_3 = int( max(bbox_3, max(annotation[1::2]) ) )
        
    bbox_2 = bbox_2 - bbox_0
    bbox_3 = bbox_3 - bbox_1

    bbox = [bbox_0, bbox_1, bbox_2, bbox_3]
    
    return bbox
 
