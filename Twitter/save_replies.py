import helpers
import pandas as pd

hp = helpers.helpers()

p = {"max_results": 100}
id = "1598431890960162847"

replies = hp.get_replies(conversation_id=id, params=p)

df = pd.DataFrame(replies["data"])
df.to_csv(f"replies_{id}.csv")
