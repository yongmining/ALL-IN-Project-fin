import pandas as pd

df = pd.read_json("messages.jsonl", lines=True)

df.head()