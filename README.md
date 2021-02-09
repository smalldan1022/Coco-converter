# Coco converter for the AI model inference segmentation tasks  


![Logo](https://github.com/smalldan1022/Coco-converter/blob/main/Dan_Logo_3.png)

[![Website online](https://img.shields.io/website/http/huggingface.co/transformers/index.html.svg?down_color=red&down_message=offline&up_message=online)](https://github.com/smalldan1022)




## Introduction    

This project aims to help the label problem of reusing the inferenced data.

When it comes to the segmentation task , labeling is the hardest and the most time-consuming part, not to mention if you want to improve your segmentation model by reusing inferenced data.



Coco annotator provides us a good way for labeling. However, if we want to reuse the results of our AI model inference, the best way is that we create a Json file that is in the coco dataset format. By doing so, we could get these results into coco annotator and refine these results. After, we use these refined data to train the AI model again so as to make the AI model more general and robust.




## Pipeline

    1.Train an AI model 

    2.Use the AI model to inference 

    3.Use the coco converter to convert these inference data into coco format Json file

    4.Create a new category in your coco annotator

    5.Create a new dataset in your coco annotator

    6.Get all the images and the coco format Json file into the folder created by step 5.6.

    7.Get into the dataset you created (in your local computer, it should be a fold) and press scan

    8.Press import COCO and import the coco format Json file 

  *Hint:You should create the category (step 5.) and the dataset (step 6.) in the same name*

## Result


![Result](https://github.com/smalldan1022/Coco-converter/blob/main/pics/coco_converter.png)




## Limitation

There are still some limitations of the coco converter.

-  You need to manually check your dataset id, image id and category id. 
- Can not be used in multi label tasks ( But of course you can modify the code yourself to help you do this)
- Slightly imprecise between the model inference and the converted coco annotations

*Hint:The dataset id, image id and category id are important, and these three values are cumulated by the coco annotator. You can check these three numbers at the Undo section of the coco annotator*



## How to use the Coco converter

Assume you have all the needed dataset. If not, go through the [Pre-requisites](#Pre-requisites) and get all the needed dataset


#### Use the main.py and modify the parameters

``` bash
python main.py


Below are parameters desciptions. You need to change manually.
====================================================

# Parameters needed to be modified are below:

# Change the image paths to yours
path = "/home/smalldan/Downloads/QuPath-0.2.3/bin/coco_test/"
    
# Change the image size 
width = 512
height = 512

# The coco dataset id is accumulated, thus you need to check your own accumulated number and replace it
dataset_id = 31
categories_id = dataset_id
    
# The coco image id (starting_id) and annotation id (starting_annotation) are accumulated, thus you need to check your own accumulated number and replace them
starting_id = 6078
starting_annotation = 2002

# The dataset and category name (basically I set the same name)
dataset_name = "coco_dataset"
```


  
## Reference

Thanks to the coco-annotator authors

```shell
  @MISC{cocoannotator,
    author = {Justin Brooks},
    title = {{COCO Annotator}},
    howpublished = "\url{https://github.com/jsbroks/coco-annotator/}",
    year = {2019},
  }
```



