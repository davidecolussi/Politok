import helpers
import time
import pandas as pd

hp = helpers.helpers()

max_tweets = {"max_results": 20}
max_replies = {"max_results": 100}

# get user id
usrid = hp.get_user_id("GiorgiaMeloni")

# get latest tweets
tweets = hp.get_user_tweets(usrid, params=max_tweets)


for i, tweet in enumerate(tweets["data"]):
    id = tweet["id"]
    tweet_df = pd.DataFrame(tweet)

    # get replies to the tweets
    replies = hp.get_replies(conversation_id=id, params=max_replies)
    replies = replies.get("data")

    if replies is not None:
        replies_df = pd.DataFrame(replies)
        tweet_df.to_csv(f"data/tweet_{id}.csv")
        replies_df.to_csv(f"data/replies_{id}.csv")

        print(f'Saved \t\t{i+1}/{len(tweets["data"])} Tweets.')
    else:
        print(f'Skipped \t{i+1}/{len(tweets["data"])} Tweets (not enough replies).')
    # time.sleep(5)

print("\n ----------------------------------------- \n")
print("Done!")
