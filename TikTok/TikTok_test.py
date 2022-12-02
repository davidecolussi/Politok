from TikTokApi import TikTokApi
import pandas as pd
try:
    import cPickle as pickle
except ImportError:  # Python 3.x
    import pickle


fp = "verify_lb5dvwme_BytDZmXX_76gD_4mx3_9aEb_oQHSWdNxQXxk"

api = TikTokApi(custom_verify_fp = fp, use_test_endpoints = True)

#Get video from id
video = api.video(id='7162585094446648582')
data = video.info()
print(data)

#Get user from username (not working)
# user = api.user(username='therock')
# print(user.info())

#Save result in pickle file
with open('data.p', 'wb') as dp:
     pickle.dump(data, dp, protocol=pickle.HIGHEST_PROTOCOL)

api.shutdown()