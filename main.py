from tkinter import *
import pandas as pd
from added_st import main
from input import input
from superimpose import superimpose

class Body():
    def __init__(self):
        super().__init__()

    def get_cover_page():
        im_path=input()[0]
        fest=input()[0]
        style_layer=["conv1_1","conv2_1","conv3_1","conv4_1","conv5_1"]
        #intializing output directory
        output_dir="./output"
        image_for_style="./"+fest+".jpg"
        content_image=im_path

        image_width=800
        image_height=600
        color_channels=3

        beta=5#less content ratio
        alpha=200#or else try 200
        l=1e4

        mean_values= np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))
        main()
        superimpose()

