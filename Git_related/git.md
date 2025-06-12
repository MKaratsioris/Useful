mkdir ...
git init / git init --bare
- difference from --bare because you don't have the working tree so you are not blocked...

git status

cd ..

git clone origin clone

git config --local user.email "mkaratsioris@yahoo.com"
git config --local user.name "Michalis Karatsioris"


git add -A
git commit -m "..."

git log --all --graph
git log --all --graph --oneline

- in clone1
git checkout -b clone1-branch1
echo "First commit in 11" > test11.txt
git add -A
git commit -m "C11"
git push --set-upstream origin clone1-branch1

- from branch to attract
git merge clone1-branch1
* git merge --abort (jump the boat!!!!!!!)

git rebase master
- manualy resolve
- git add

git rebase --continue

GOOD PRACTICE: Rebase in master every couple of commits....


## Cloning repo and pushing new changes to a new branch
- git checkout -b <name-new-branch>
- git add .
- git commit -m "......"
- git push --set-upstream origin <name-new-branch>


git branch -d music-player-app
git fetch -p

## Resolve merging conflicts
- git config --global pull.rebase true
- git pull origin test
- git status
- Change one of the conflicts and `git add`
- git rebase --continue
- git push --force-with-lease