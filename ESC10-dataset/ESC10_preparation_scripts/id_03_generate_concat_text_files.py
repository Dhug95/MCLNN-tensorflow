"""
This script generates repetition of the file name for each sound file to be used by ffmpeg to concatenate
 Several files together
make sure to configure the source and destination folders before your execute this script
 Fady Medhat
 version 0.1
"""

import os

# DATASET_PATH = '/Users/francesco/Desktop/Sapienza/Corsi/NeuralNetworks/MCLNN-ESC/ESC10-trim'
DATASET_PATH = '/content/MCLNN-tensorflow/ESC10-dataset/data/ESC10-trim'
CONCAT_COUNT = 2

folder_list = os.listdir(DATASET_PATH)
folder_list.sort()

for i in range(0, len(folder_list)):
    files = os.listdir(os.path.join(DATASET_PATH , folder_list[i]))
    files.sort()
    for name in sorted(files):
        file = open(os.path.join(DATASET_PATH, folder_list[i] , str.replace(name, '.wav', '.txt')), 'w')
        for j in range(CONCAT_COUNT):
            file.write('file \'' +  str.replace(name, '.txt', '.wav') + '\'\n')
        file.close()