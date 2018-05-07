from textblob import TextBlob
wiki = TextBlob('Maybe try to call me sometimes to find out my needs. They always done better for me all of time. The last time they called, they were telling me I needed to see an eye doctor and I really, really appreciate that. For now, you guys are doing a good job, I have glasses now, I am going to see my doctor so I am good.')
yolo = wiki.tags
waka = wiki.words
print(yolo)
bolo = wiki.sentiment
print(bolo)
