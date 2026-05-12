import json
import pandas as pd

with open("Sarcasm_Headlines_Dataset.json", "r") as f:
    data = [json.loads(line) for line in f]

df = pd.DataFrame(data)
df = df[["headline", "is_sarcastic"]]
df.columns = ["text", "label"]
df.to_csv("sarkazmdata.csv", index=False)
