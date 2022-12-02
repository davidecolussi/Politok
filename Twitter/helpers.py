import requests
import os


class helpers:
    def __init__(self) -> None:

        self.bearer_token = os.environ.get("BEARER_TOKEN")

        pass

    def create_headers(self):

        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}

        return headers

    def get_user_id(self, username: str) -> str:
        """
        Get the ID of a Twitter user via their username.
        """

        url = f"https://api.twitter.com/2/users/by/username/{username}"

        try:
            response = requests.get(url, headers=self.create_headers())

        except Exception as e:
            print("Error occured", e)

        return response.json()["data"]["id"]

    def get_user_tweets(self, userid: str, params=None) -> dict:
        """
        Get the most recent Tweets of a specific user. To get a userid see self.get_user_id().
        """

        url = f"https://api.twitter.com/2/users/{userid}/tweets"

        try:
            response = requests.get(url, headers=self.create_headers(), params=params)

        except Exception as e:
            print("Error occured", e)

        return response.json()

    def get_replies(self, conversation_id: str, params=None) -> dict:
        """
        Get the replies to a Tweet. This need the conversation_id which is the same as the id of original the Tweet.
        """

        url = "https://api.twitter.com/2/tweets/search/recent"

        # add query to params
        if params is not None:
            params["query"] = f"conversation_id:{conversation_id}"

        else:
            params = {"query": f"conversation_id:{conversation_id}"}

        try:
            response = requests.get(url, headers=self.create_headers(), params=params)

        except Exception as e:
            print("Error occured", e)

        return response.json()
