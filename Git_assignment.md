# Git Squash
- used to re-package commits that are related to each other 
   (they could be related to a single bug fix or related to a feature and does not need to be on its own)
- when using squash, the dev branch replays and lists all the commits from the master branch, commits 
  the changes made plus the previous commit once.
- Therefore, instead of having multiple commits for the same bug fix of additional functionallity in 
  the clsas, you can use squash to get the commits and have less commits in your repository.

# git Rebase
- git checks the commits that the feature branch and the master branch have in common, it then checks the latest commit that the mater have.
- If a the master branch commits while working on the feature branch, git collects the changes it found in the 
  master branch and bases the feature branch on the latest commit.
- the feature branch in git rebase always uses the recent commit from the master as a base, irrespective of when the commit
   was made.

# Git forks
- Git fork is when you create a copy of a the existing repository, this allows  you to work independently on the copied repository.
- You can request to merge after you have worked on the copy.
- the copy is not linked to the original copy of the repository.

# git rebase -i
- it is used in git to perfome interactive rebase.
- This allows you to edit commits from the base commits.