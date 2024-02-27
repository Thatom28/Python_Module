## Regex functions
- \d every number between 0 and 9 for only one number (\d\d\d) will match numbers between 0 and 9 for 3 numbers
- \D anything exept a number
- . -. any character
- \. -> match exactly dot
- [abc] match a ro b or c
#[abc]s match-> a or b or c and s
#[cmf]an  match-> must match c or m or f and have to contain a and n
#[^abc] match -> should not contain a or b or c
#[abc]s match-> should not match a or b or c, s can be included, ithe 
#[a-z]\d  [a-g]  [5-7] match -> a to z followed by a digit
#[A - Z] match -> A to Z in capital letters
#\w matches any word character and digits
#\W matches any non word character or digits
#funnny -> fun{3}y_> matches fun with 3 n's
#fun{2,5}y -> match fun that has 2 to 5 n's
#fu[nz]{2}y -> must match fu and any letter not l, the letter must be repeated twice
#fun+y  match -> one or more n's
#fun*y match ->0 or more n's
- fan?n 
- \s match-> space
- \S anything but he space
- \d\.\s+abc any number + a dot + any number of space then abc
- ^..$  cap is used for start, and dollar sign is for the end
- ^Mission  -. start with the word Mission
- ^Mission: successful$
- CaptureGroup = ^(file_\w*).pdf  i will take the "file_any character"
- subGroup (\D*(\d*)) or (\D{3} (\d{4})) with will match the jan 1987 and 1987
- capture all (\d+)x(\d+) or (\d{4})x(\d{3,})
- (.*)x(.*)
- or operator This(is|was)cool  will check for is or was after this in a sentence
- I love (cats|dogs)