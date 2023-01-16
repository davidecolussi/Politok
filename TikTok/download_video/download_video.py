# download_video.py

import os
from TikTokApi import TikTokApi
import moviepy.editor as mp
import pandas as pd
import numpy as np
import datetime
import math

def extract_INF_video(file_name):
    #build a dataframe containing the file information
    df=pd.DataFrame(pd.read_excel(file_name))
    #from the link extract all the video id
    video_id=[df["Link"][i].split("/")[5].split("?")[0] for i in range(len(df))] 
    #re-write the data time in a specific way
    df["Date"]=[df["Date"][i].strftime('%m-%d-%Y') for i in range(len(df))]
    #add a column into the dataframe containing the video id
    df["video_id"]=video_id
    #create a list of name 
    name=[df["Politician"][i] if df["Influencer/tiktoker"][i] is np.nan else df["Influencer/tiktoker"][i] for i in range(len(df))] 
    name=[name[i].replace(" ", "_") for i in range(len(name))]
    return df,video_id,name


def download_video(cos_key,video_id,name):
    #extract the video bytes using the tiktokapi library
    with TikTokApi(custom_verify_fp=cos_key) as api:
        video = api.video(id=video_id)
        video_data = video.bytes()        
        #create a specific directory and name for the video 
        file_name="Audio/{}_vid_{}.mp4".format(name,video_id)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        #save the video into an mp4 file
        with open(file_name, "wb") as out_file:
            out_file.write(video_data)
        api.shutdown()
    #convert the mp4 file into a mp3 file
    with mp.VideoFileClip(file_name) as clip:
        clip.audio.write_audiofile(r"Audio/{}_vid_{}.wav".format(name,video_id))
    os.remove(file_name)
    return
    
filename=input("insert the file name: ")
if type(filename) != str:
    print("The input variable (filename) must be a string")
    exit()
v=input("insert the verify key for TikTokApi: ")
if type(v) != str:
    print("The input variable (v) must be a string")
    exit()
    

df,video_id,name=extract_INF_video(filename)

for i in range(len(video_id)):
    print("checkpoint_{}".format(i))
    download_video(v,video_id[i],name[i])
