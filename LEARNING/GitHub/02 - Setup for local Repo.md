- Creating Version 
```
//Creating Enviroment
git init

//Seeing changes
git status

//Add code into the Staging
git add .

//Add code into Local repo
git commit -m "version-1"

//To Rename from master to main
git branch -m master main
```
- Configure the email and name [Priority - 1]
```
//Refer the document
git config email 

//Refer the document
git config name 
```
- Put Code from Staging Stage to the working Stage [Reverse-order] Staging Stage --> Working Stage [ 2 -> 1] decrement
```
git reset . [or specfic file]
```
- Put the code from working directory to Undo means remove from the working directory [Reverse-order] Working Stage -> remove
```
git checkout -- .[or specific file]
```
- See the Git log 
```
//Show current commit
git log 

//show all commit [Head will show the currect version]
git log --all

//Show the branch of version
git log --all --graph
```
- Go back to the version lets consider we have three version we need to go back we need to do
```
git checkout <commit hast long String>
```
- This is how it will do if we override the previous version
![[Pasted image 20250430204038.png]]
```
//Show the branch of version
git log --all --graph

//quit from the command
q - for quit

master commit to the latest commit
```

- How to restore our code into the version we want
```
git checkout <version> . [or filename]
```
- We can create a alies
```
//Refer the Document
git config alias.s "status"
```
- To delete the git
```
rm -rf .git or in windows [rd /s /q .git]
```

```
--set-upstream -- used to sent the origin once decleared we dont want to mention the origin
```

```
If we want to override the exisiting code the we can use the 
git push -f //Not until unless we needed dont use this

```