## How does Lookbehind work:

- you want to return a word only if it is after a particular word or character
- e.g balance = "you have R500 in your account" -> Checks whether the pattern to the right of the parser's current position match
- (?<=you have).*: this expression will match "R500 in your account" because it comes after the words mentioned in the expression
- (?<=you have).*\d -> this expression will only match the "R500" because the expression is saying that, match the digits after the words "you have"
- if the expression is not found "None" will be returned.
- in conclusion: LookBehind expression checks whtehr the charaters after the specified expession in the regex expression matches with the requirements that are specified after the words. In the above example, it wants to match the digits that come after the word that has been specified.