#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:30:35 2020

@author: AlexanderWoelfel
"""

#import libs
import os
import numpy as np
import cv2
import tensorflow.keras.applications
import pandas as pd



#Loading all pictures of a folder, reduces dimensions, preprocesses and returns them as 3D arrays in a list. Additionally returns the filenames as a seperate list
def load_images(path):
    image_list = []
    filename_list = []
    dim = (224, 224)
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path,filename))
        name = filename
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            curr = cv2.resize(img, dim)
            curr = tensorflow.keras.applications.densenet.preprocess_input(curr, data_format=None)
            curr = np.expand_dims(curr, 0)
            image_list.append(curr)
            filename_list.append(name)
    return image_list, filename_list


#requires upper functions 
#Main method calls functions for loading the pictures from given path, preprocesses them for Dense Net and returns the file names as well as the Classification results as a list
def main (path):
    image_list, name_list = load_images(path)
    results = []
    for i in range(len(image_list)):
        y = model.predict(image_list[i])
        pred = tensorflow.keras.applications.densenet.decode_predictions(y, top = 5)
        results.append(pred)
    return name_list, results

#requires upper functions | input: list of filenames, list of results from nasnet
#writes an DataFrame with pandas for an csv export with seperate colums for each possible label, its readable name and its probability 
def write_df (name_list, results):
    pre_1_nas, pre_1_name, pre_1_prob, pre_2_nas, pre_2_name, pre_2_prob, pre_3_nas, pre_3_name, pre_3_prob, pre_4_nas, pre_4_name, pre_4_prob, pre_5_nas, pre_5_name, pre_5_prob = ([] for i in range(15))
    for i in range(0, len(results)):    
        pre_1_nas.append(results[i][0][0][0])
        pre_1_name.append(results[i][0][0][1])
        pre_1_prob.append(results[i][0][0][2])
        pre_2_nas.append(results[i][0][1][0])
        pre_2_name.append(results[i][0][1][1])
        pre_2_prob.append(results[i][0][1][2])
        pre_3_nas.append(results[i][0][2][0])
        pre_3_name.append(results[i][0][2][1])
        pre_3_prob.append(results[i][0][2][2])
        pre_4_nas.append(results[i][0][3][0])
        pre_4_name.append(results[i][0][3][1])
        pre_4_prob.append(results[i][0][3][2])
        pre_5_nas.append(results[i][0][4][0])
        pre_5_name.append(results[i][0][4][1])
        pre_5_prob.append(results[i][0][4][2])     
    df = pd.DataFrame({"Filename": name_list, "Result#1_n": pre_1_nas, "Result#1_Name": pre_1_name, "Result#1_Probability":pre_1_prob, "Result#2_n": pre_2_nas, "Result#2_Name": pre_2_name, "Result#2_Probability":pre_2_prob, "Result#3_n": pre_3_nas, "Result#3_Name": pre_3_name, "Result#3_Probability":pre_3_prob, "Result#4_n": pre_4_nas, "Result#4_Name": pre_4_name, "Result#4_Probability":pre_4_prob, "Result#5_n": pre_5_nas, "Result#5_Name": pre_5_name, "Result#5_Probability":pre_5_prob})
    return df

#exports the DataFrame as a csv-file
def exporter(df, path_to_new_csv):
    df.to_csv(path_or_buf = path_to_new_csv)
    

#Methodenaufruf
model = tensorflow.keras.applications.DenseNet201(weights='imagenet') 
names, results = main("/Volumes/SD_Alex/avt_image_db_selection/")
data_f = write_df(name_list=names, results=results)
exporter(df=data_f, path_to_new_csv="results_29-12_densenet.csv")