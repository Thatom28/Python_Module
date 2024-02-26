import re
#  Regex -> regulae Expression
#Pattern match in a string

numbers = "6932874, 762434, 739148732, 47326487, 49374914743"

#To find the credit card numbers
  #they start with 4
  #they have 16 digts
## Methods to ue regex
# 1. serch
#2.findAll
# 3.sub
qoute ="to be or not to be"
is_be = re.search('be$', qoute)  #checks whether the quote ends with "be"
output = "present" if is_be else "not present"
print(is_be)  #we use r instead of f in this
print(output)
#if a value is not ofund it returns a none

#---------------findAll---------------------
find_be = re.findall('be', qoute)
print(find_be)   #returns all be 

qoute1="funny funy, funnny fuzzy"
#use the raw string to ignore the escape character
find_be2 = re.findall(r'fu[nz]{2}y', qoute1)

#-----------------sub------------------------
#substitute the first match
tweet ="Spoiler: this movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"
censor_text=re.sub(r'(spoiler|but)','*'*7, tweet)  #censors "spoiler or "but"
censor_text=re.sub(r'(spoiler|but)','*'*7, tweet, flags= re.IGNORECASE)  #the content is caps sensitive
print(censor_text)

#---------------------groups--------
list_websites="facebook.com, google.com, twitter.in"

#only capture the .com

result = re.sub(r'(\w+)\.com', 'blacklist.com', list_websites)  #replace the website names with.com with te blacklist.com
#convert .com to .in
results2 = re.sub(r'(\w+)(\.com)', r'\2', list_websites)  #the second group will be returned
results2 = re.sub(r'(\w+)(\.com)', r'\1.subdomain.\2', list_websites)
print(result)

