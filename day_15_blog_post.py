import json

posts = {}
with open("Day_15_blog_post.json", "r") as json_file:
    blog = json.load(json_file)

posts = blog["posts"]
summarizedPosts = []
for post in posts:
    summarizedPost = {
        "title": post["title"],
        "author": post["author"],
        "number_of_commnets": len(post["comments"]),
    }
    summarizedPosts.append(summarizedPost)


with open("summarized_posts.json", "w") as file:
    json.dumps(summarizedPosts, file, indent=4)
