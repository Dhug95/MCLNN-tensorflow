"""
This file is used to convert ogg format to wav for the ESC-10 dataset
make sure to configure the source and destination folders and have librosa installed before your execute this script
 Fady Medhat
 version 0.1
"""


import os
import librosa
from fnmatch import fnmatch


# SRC_PATH = '/Users/francesco/Desktop/Sapienza/Corsi/NeuralNetworks/MCLNN-ESC/ESC10-vanilla/'
# DST_PATH = '/Users/francesco/Desktop/Sapienza/Corsi/NeuralNetworks/MCLNN-ESC/ESC10-trim/'
SRC_PATH = '/content/ESC10-vanilla/'
DST_PATH = '/content/MCLNN-tensorflow/ESC10-dataset/data/ESC10-trim/'


folder_list = os.listdir(SRC_PATH)
folder_list.sort()


for i in range(0, len(folder_list)):
    files = os.listdir(SRC_PATH + folder_list[i])
    files.sort()
    for name in sorted(files):

        if fnmatch(name, "*.wav"):
            y, sr = librosa.load(SRC_PATH + folder_list[i] + '/' + name)

            # trim the zeros
            yt, index = librosa.effects.trim(y)

            # create a class folder if it does not exist
            if not os.path.exists(DST_PATH + folder_list[i]):
                os.makedirs(DST_PATH + folder_list[i])

            # save the trimmed file
            librosa.output.write_wav(DST_PATH + folder_list[i] + '/' + name, yt, sr)

            # print the original duration and the new one
            print(librosa.get_duration(y), librosa.get_duration(yt) , max(y), max(yt))