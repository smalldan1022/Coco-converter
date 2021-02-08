import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import json
import numpy as np
import utility as ut


# Convert the numpy data type into python data type
class MyEncoder(json.JSONEncoder):
    
    def default(self, obj):
        
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj) 
        
        
if __name__ == "__main__":        
    
    
    # Initialize the coco
    coco_dataset = {"images":[], "categories":[{}], "annotations":[]}

    # TODO:Change the image paths to yours
    path = "/home/smalldan/Downloads/QuPath-0.2.3/bin/coco_test/"
    image_paths = glob.glob(path + "*")
    
    # TODO:Change the image size 
    width = 512
    height = 512

    # The coco dataset id is accumulated, thus you need to check your own accumulated number and replace it
    dataset_id = 31
    categories_id = dataset_id
    
    # The coco image id (starting_id) and annotation id (starting_annotation) are accumulated, thus you need to check your own accumulated number and replace them
    starting_id = 6078
    starting_annotation = 2002

    # The dataset and category name (basically I set the same name)
    dataset_name = "coco_convert_test"
    
    
    # Start the set all the parameters into coco format json
    for i in range(len(image_paths)):
        
        ## images part ##
        
        coco_dataset["images"].append({})
        
        coco_dataset["images"][i]["id"] = str(starting_id + i)
        coco_dataset["images"][i]["dataset_id"] = dataset_id
        coco_dataset["images"][i]["category_ids"] = []
        coco_dataset["images"][i]["path"] = "/dataset/{}/".format(dataset_name) + image_paths[i].split("/")[-1]
        coco_dataset["images"][i]["width"] = 512
        coco_dataset["images"][i]["height"] = 512
        coco_dataset["images"][i]["file_name"] = image_paths[i].split("/")[-1]
        coco_dataset["images"][i]["annotated"] = False
        coco_dataset["images"][i]["annotating"] = []
        coco_dataset["images"][i]["num_annotations"] = 0
        coco_dataset["images"][i]["metadata"] = {}
        coco_dataset["images"][i]["deleted"] = False
        coco_dataset["images"][i]["milliseconds"] = 0
        coco_dataset["images"][i]["events"] = []
        coco_dataset["images"][i]["regenerate_thumbnail"] = False
        
        
        ## categories part ##
        
        coco_dataset["categories"][0]["id"] = categories_id
        coco_dataset["categories"][0]["name"] = dataset_name
        coco_dataset["categories"][0]["supercategory"] = ''
        coco_dataset["categories"][0]["color"] = "#c94f74"
        coco_dataset["categories"][0]["metadata"] = {}
        coco_dataset["categories"][0]["keypoint_colors"] = []
        
        
        contours, area = ut.Get_x_y_and_Area(image_paths[i])
        
        annotations = ut.x_y_convert(contours)
        
        print(annotations)
            
        bbox = ut.Find_the_bbox(annotations)
        
        coco_dataset["annotations"].append({})
        coco_dataset["annotations"][i]["segmentation"] = []
        
        for j in range(len(annotations)):
        
            ## segmentation part ##
            
            coco_dataset["annotations"][i]["id"] = str(starting_annotation + j)
            coco_dataset["annotations"][i]["image_id"] = str(starting_id + i)
            coco_dataset["annotations"][i]["category_id"] = categories_id
            coco_dataset["annotations"][i]["segmentation"].append( annotations[j] )
            coco_dataset["annotations"][i]["area"] = area
            coco_dataset["annotations"][i]["bbox"] = bbox
            coco_dataset["annotations"][i]["iscrowd"] = False
            coco_dataset["annotations"][i]["isbbox"] = False
            coco_dataset["annotations"][i]["color"] = "#edc91c"
            coco_dataset["annotations"][i]["metadata"] = {}

    
    # Save the coco json
    with open(path+"coco.json", "w") as outfile:
        json.dump(coco_dataset, outfile, cls=MyEncoder)
        
    
    
