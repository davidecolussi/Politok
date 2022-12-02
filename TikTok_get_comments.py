from TikTokApi import TikTokApi

fp = "verify_lb6ecx6a_WrOyZlpQ_WApI_4Bxk_AIjr_8BPXMEd1axJa"


api = TikTokApi(custom_verify_fp = fp, use_test_endpoints = True)

#Get video from id
video = api.video(id='7162585094446648582')
comments = video.comments(count=10)
for comment in comments:
    print(comment.text)


api.shutdown()