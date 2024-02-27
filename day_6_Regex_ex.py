import re
#Reverse swap the names with the surname
names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]

reversed = []
for name in names:
  results = re.sub(r'(\w+)\s+(\w+)', r'\2 \1', name)
  reversed.append(results)
print(reversed)

# Assignment
hashtag = []
post = "Loving the #sunny weather in #California. #travel #fun"
hashtag = re.findall(r'#\w+', post)
print(hashtag)
# Output
['#sunny', '#California', '#travel', '#fun']
