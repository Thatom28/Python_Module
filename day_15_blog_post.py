import json

posts = {}
with open("Day_15_blog_post.json", "r") as json_file:
    posts = json.load(json_file)

posts2 = {}
for post in posts:
    posts2 = {**posts, "comments": (post["comments"]).count()}

print(posts2)
