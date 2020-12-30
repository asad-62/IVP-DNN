# IVP_Seminar_ws2020

**Contains the Code for the Group Project Topic 2: Image Classification**

## General information

Supervisor: Rakesh Rao Ramachandra Rao: rakesh-rao.ramachandra-rao@tu-ilmenau.de

Image classification refers to a process that can classify an image according to its visual content. 
For example, an image classification algorithm may be designed to tell if an image contains a cat or not. 
Many image classificaton algorithms, both classical and machine-learning-based, have been proposed in literature. 

**The main goals of this task are as follows:**
* Select 3 image classification algorithms of your choice
  * The choice should be based on an objective reason
  * These algorithms can either be classical or machine-learning-based
* Apply these 3 algorithms on the dataset that is provided 
* Analyse the results of the 3 classification algorithms

**submit a 4-page IEEE style paper (including references) until 04.02.2021 (11:59 PM) to Ashutosh Singla via email.**

## Current project status:
### Selection of Approaches
Selected three CNN-Approaches for image classification based on state-of-the-art benchmarks for **CNNs trained on ImageNet database** (TOP 1 and TOP 5 accuracy | different amount of training pictures) that are part of the Keras API (https://www.tensorflow.org/api_docs/python/tf/keras/applications?hl=de)
  * NASNetLarge https://arxiv.org/abs/1707.07012
  * EfficientNetB7 https://arxiv.org/abs/1905.11946
  * DenseNet201 https://arxiv.org/abs/1608.06993  
* Further reading:
  * https://paperswithcode.com/task/image-classification
  * https://towardsdatascience.com/state-of-the-art-image-classification-algorithm-fixefficientnet-l2-98b93deeb04c 
  * https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/ 
  * *(Not choosen due to lack of fitting implementation, but interesting performance) FixEfficientNet-L2 https://github.com/facebookresearch/FixRes*
 
### Ground truth for data
* Did a ground truth on the 200 pictures https://cloud.tu-ilmenau.de/s/9ffWqt7G9oLziAk with up to 20 possilbe labels per image ('picture_all-labels.csv' in the git)
* Selected one lable for each picture for a TOP 1 Accuracy calculation ('picture_one-label.csv' in the git)

**(tbd): If we compare our ground truth with the classification results of the three algorithms, the meaning of the gt and tbe classification labels often match, but the wording is not identically**
 * If we would automate the checkup based on the current gt labels, there would not be a high amount of correct classifications due to the differt wording 
 * But: if you take a glace at the image and the according classification results, you would eventually count it as a right classification result 

|     Image    | Current accepted results (based on gt)                | TOP-5 results from NASNetLarge                                                             |
|:------------:|-------------------------------------------------------|--------------------------------------------------------------------------------------------|
| 0AKZCRZA.png <br> ![](https://drive.google.com/uc?export=view&id=14J8Lir-uKsqtujJF7GbJHduqPBLA_2dU)| train, Train, industry, railway, Railway, sky, sunset | 'freight_car', 'electric_locomotive', 'passenger_car', 'trailer_truck', 'steam_locomotive' |


**Conclusion:** we need an other objective approach (ground truth) in order to decide if an image was classified correctly or not

Idea to tackle the problem:
Our three selected cnns were all trained on the ImageNet database, which leads to the same 1000 possible outputs/classification results. We use this fact by doing a second ground truth, for which we assign a small amount (1 to 5) of the possible labels (out of the 1000) for each image, that we consider as best fitting. This ground thruth would be compareable, since all network have the same chance for hitting the assinged ground truth label.
<br> Also a scripted comparision of the results and our ground truth woulb be possible with this approach.
 
### Working with high resolution images 

~~**DUE TO LIMITED PROCESSING POWER: UNTIL NOW ONLY USED IMAGES WITH SHRINKED RESOLUTION** </br>
https://cloud.tu-ilmenau.de/s/AKo8jqwEXLFs7Q3 </br>
Used the Image Resizer application with following options: </br>
custom width x height (450 x 300) | rotate and flip option: keep original | output setting **Retain the original format**~~<br>
FIXED: This isn't the case anymore - all results from 29.12.2020 are based on the full resolution images

</br> **Identified possible approaches for working with high resolution images** 
* **Brute force approach**: Resizing to required dimension (Open CV | cv2.resize) within the preprocessing for the specific cnn-approach
* **PCA approach**: (@Asad, @Abhinav, @Muhammad) until 03.01.2021

### Get the classification results

**NasNet Large**
- [x] Brute force approach: finished (@Alex)
  * results in csv
  * statistical measurements in excel
- [ ] PCA approach: doing until 03.01.2021 (@Asad, @Abhinav, @Muhammad)

**EfficientNetB7**
- [X] Brute force approach: finished (@Alex)
- [ ] PCA approach: doing until 03.01.2021 (@Asad, @Abhinav, @Muhammad)

**DenseNet 201**
- [X] Brute force approach: finished (@Alex)
- [ ] PCA approach: doing until 03.01.2021 (@Asad, @Abhinav, @Muhammad)


## Possible next steps in the project 
* compare the results of the networks with ground truth (challenges/problems in the ground truth paragraph) 
  * **TOP 5 Acc with all available up to 20 gt-labels (no ranking)**
  * (tbd) TOP 5 Acc with 1 gt-label (label chosen by hand)
  * (tbd) TOP 1 Acc with all available up to 20 gt-labels (no ranking)
  * (tbd) TOP 1 Acc with 1 gt-label (label chosen by hand)
 
* (tbd) compare the influence of the pre-processing resizing vs. PCA

* write the paper until 16.01.2021 for getting feedback before the final hand-in (@Kenneth is already working on the paper)
 
* ~~(tbd) Run the pre-processing with open cv or PCA on the full resolution images (difficult due to processing power)~~<br>
This isn't the case anymore: all results from 29.12.2020 are based on the full resolution images
