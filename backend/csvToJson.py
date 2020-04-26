import pandas as pd
import json

df = pd.read_csv("processed_tweets.csv")

tweets = list(df["Text"])
scores = list(df["compound"])

dbfile  = open("db.json","w+")

db = {}
count = 0
dbfile.write("{'data': [")
for i in range(1000):
    data = {
        "id": count+1,
        "tweet": tweets[count],
        "score": scores[count]
    }
    dbfile.write(json.dumps(data)+",")
    count+=1

dbfile.write("]}")