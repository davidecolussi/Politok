## Video download
The main script is "download_video.py", it contains:
-a function wiìhich extract the information from the excel file and build a dataframe
-a second function which use TikTokApi to download the video, and using moviepy library convert the video into an .mp3 file
There is a jupyter usefull to show the dataframe
The TikTokApi does not work into a jupyter because there are problems with asyncio loop.