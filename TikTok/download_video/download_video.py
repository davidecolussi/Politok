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
    return df,video_id,name


def download_video(cos_key,video_id,name,data_time):
    #extract the video bytes using the tiktokapi library
    with TikTokApi(custom_verify_fp=cos_key) as api:
        video = api.video(id=video_id)
        video_data = video.bytes()
        api.shutdown()
    #create a specific directory and name for the video 
    file_name="{}/{}_{}.mp4".format(name,data_time,video_id[-3:])
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    #save the video into an mp4 file
    with open(file_name, "wb") as out_file:
        out_file.write(video_data)
    #convert the mp4 file into a mp3 file
    clip = mp.VideoFileClip(file_name)
    clip.audio.write_audiofile(r"{}/{}_{}.mp3".format(name,data_time,video_id[-3:]))
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

for i in range(lan(video_id)):
    download_video(api,video_id[i],name[i],df["Date"][i])
    
