import re

qoute1 = "funny funy, funnny fuzzy"

# return funny and fuzzy
rep = re.findall(r"fu[\w]{3}y", qoute1)
print(rep)

optional_char = re.findall(r"colou?r", "color colour")
print(optional_char)

alter = re.findall(r"(to|be)", "to be or ot to be")
print(alter)

first_word = "hello world"
groups = re.search(r"(\w+)\s+(\w+)", first_word)
print(groups.groups())

groups1 = re.sub(r"(\w+)\s+(\w+)", r"\2 \1", first_word)
print(groups1)

# Assignment
hashtag = []  # 1
post = "Loving the #sunny weather in #California. #travel #fun"  # 3
hashtag = re.findall(r"#\w+", post)  # 2
print(hashtag)
# Output
["#sunny", "#California", "#travel", "#fun"]

# -- list comprehension
hashtag1 = [re.findall(r"#\w+", post)]
print(hashtag1)
