# GitHub Commands

## Git Configuration
`git config --global user.name "Your Name"` - Set the global username for Git.  
`git config --global user.email "your.email@example.com"` - Set the global email for Git.  
`git config --list` - View the current Git configuration.  

## Initialize Repository
`git init` - Initialize a new Git repository.  
`git clone <repo_url>` - Clone an existing repository from GitHub.  

## Staging and Committing
`git add <file>` - Stage a specific file for commit.  
`git add .` - Stage all changes in the directory.  
`git commit -m "commit message"` - Commit staged changes with a message.  
`git commit --amend -m "new message"` - Amend the last commit message.  

## Branching
`git branch` - List all branches.  
`git branch <branch_name>` - Create a new branch.  
`git checkout <branch_name>` - Switch to a different branch.  
`git checkout -b <branch_name>` - Create and switch to a new branch.  
`git branch -d <branch_name>` - Delete a local branch.  
`git push origin --delete <branch_name>` - Delete a remote branch.  

## Merging
`git merge <branch_name>` - Merge a branch into the current branch.  
`git merge --no-ff <branch_name>` - Merge a branch and keep the history.  
`git merge --abort` - Abort a merge in progress.  

## Rebasing
`git rebase <branch_name>` - Reapply commits on top of another base branch.  
`git rebase -i HEAD~3` - Interactive rebase for the last 3 commits.  
`git rebase --abort` - Abort an ongoing rebase.  
`git rebase --continue` - Continue a paused rebase.  

## Pushing and Pulling
`git push origin <branch_name>` - Push changes to a remote repository.  
`git push --force` - Force push changes (use with caution).  
`git pull origin <branch_name>` - Pull changes from a remote repository.  
`git fetch` - Fetch changes from the remote repository without merging.  

## Resetting and Reverting
`git reset --soft HEAD~1` - Undo the last commit, keeping changes staged.  
`git reset --mixed HEAD~1` - Undo the last commit, keeping changes unstaged.  
`git reset --hard HEAD~1` - Undo the last commit and remove all changes.  
`git revert <commit_id>` - Create a new commit that undoes a specific commit.  

## Stashing Changes
`git stash` - Stash uncommitted changes.  
`git stash pop` - Apply the most recent stashed changes.  
`git stash list` - View all stashed changes.  
`git stash drop` - Remove the most recent stash.  

## Logging and Status
`git status` - Show the status of the working directory.  
`git log` - View commit history.  
`git log --oneline` - View commit history in a compact format.  
`git log --graph --decorate --oneline` - View a graphical commit history.  

## Tagging
`git tag <tag_name>` - Create a new tag for a commit.  
`git tag -a <tag_name> -m "message"` - Create an annotated tag.  
`git push origin <tag_name>` - Push a tag to a remote repository.  
`git push origin --tags` - Push all tags to a remote repository.  

## Remote Management
`git remote -v` - List remote repositories.  
`git remote add origin <repo_url>` - Add a remote repository.  
`git remote remove origin` - Remove a remote repository.  

## Undoing Changes
`git checkout -- <file>` - Discard changes in a file.  
`git reset HEAD <file>` - Unstage a file.  

## Cherry-picking
`git cherry-pick <commit_id>` - Apply a specific commit from another branch.  
`git cherry-pick --continue` - Continue cherry-picking if conflicts occur.  
`git cherry-pick --abort` - Abort an ongoing cherry-pick.  

## Squashing Commits
`git rebase -i HEAD~3` - Squash the last 3 commits interactively.  
`git commit --squash <commit_id>` - Squash a specific commit into the previous one.  

## Bisecting (Finding Bugs)
`git bisect start` - Start the bisect process.  
`git bisect bad` - Mark the current commit as bad.  
`git bisect good <commit_id>` - Mark a commit as good.  
`git bisect reset` - End the bisect process.  

## Submodules
`git submodule add <repo_url>` - Add a submodule to the repository.  
`git submodule update --init --recursive` - Initialize and update submodules.  
`git submodule deinit -f <submodule_path>` - Remove a submodule.  

## Worktrees (Multiple Workspaces)
`git worktree add <path> <branch>` - Create a new worktree.  
`git worktree list` - List all worktrees.  
`git worktree remove <path>` - Remove a worktree.  
