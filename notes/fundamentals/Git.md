### What is GIT?

GIT is a distributed version control system created by Linus Torvalds, used for tracking changes in source code during software development. It allows for recording changes in files, creating branches, merging changes, and much more.

### Basic GIT Commands

1. **git init** - Initializes a new GIT repository in the current directory.
   ```git
   git init
   ```
   
2. **git clone [url]** - Clones the repository from the given URL.
   ```git
   git clone https://github.com/example/repo.git
   ```
   
3. **git status** - Shows the status of changes in the repository.
   ```git
   git status
   ```
   
4. **git add [file]** - Adds a file to the staging area.
   ```git
   git add file.txt
   ```
   
5. **git commit -m "message"** - Records changes in the repository with an appropriate message.
   ```git
   git commit -m "Added new feature"
   ```
   
6. **git push [remote] [branch]** - Sends changes to the remote repository.
   ```git
   git push origin master
   ```
   
7. **git pull [remote] [branch]** - Fetches changes from the remote repository and merges them with the current branch.
   ```git
   git pull origin master
   ```
   
8. **git branch [branch-name]** - Creates a new branch.
   ```git
   git branch new-branch
   ```
   
9. **git checkout [branch-name]** - Switches to another branch.
   ```git
   git checkout new-branch
   ```
   
10. **git merge [branch-name]** - Merges changes from the given branch into the current branch.
    ```git
    git merge new-branch
    ```

11. **git log** - Displays the history of changes.
    ```git
    git log
    ```
    
12. **git diff** - Shows the differences between changes.
    ```git
    git diff
    ```

### Best Practices

- Regularly commit your changes with meaningful messages.
- Maintain a clean change history by using rebase instead of merge where possible.
- Before starting work on a new feature/bug fix, ensure you are working on the latest version of the code by performing `git pull`.
- Use branch naming that describes its purpose or type of work, e.g., `feature/new-feature` or `bugfix/bug-fix`.

## Learning Resources
- **[How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ)** - review a video tutorial on the workings of Git.
- **[Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)** - basic information about git.
- **[Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0)** - git merge vs git rebase.