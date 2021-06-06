# GitHub Tutorial

Based on this: https://git-scm.com/docs/gittutorial



## Description

How to make new proj in Git, make changesand share changes with other developers. 



## Importing a New Project

Assuming you have the tarball project.tar.gz, can place it under Git revision control as follows;

	` tar xzf project.tar.gz `
	` cd project `
	` git init `

Will initialize an empty Git repository in `.git/`. 

Next tell Git to take a snapshot of the contents of all files under the current directory (note the `.`) with;

	` git add . `

Snapshot is stored in a temporary staging area called the "index". Permanently store contents of index in the repository with ` git commit `.

	` git commit `



## Making Changes

	` git add file1 file2 file3  ` # Modify files, add their updated contents to index
	` git diff --cached ` # Can see what is about to be committed using ` git diff ` with the `--cached` option. Without the ` --cached ` option, it will show you any changes that you've made but not yet added to the index.


If you need to make further adjustments, do so now and then add newly modified content to the inedx. Finally commit your changes with 
	
	` git commit ` # This will prompt you for a message describing the change and then record a new version of the project. 
	` git commit -a ` # Alternatively, instead of running `git add` beforehand, you can add `-a`, which will automatically notice any modified (but not new) files, add them to the index and commit, all in one step

A note on commit messages: Though not required, it’s a good idea to begin the commit message with a single short (less than 50 character) line summarizing the change, followed by a blank line and then a more thorough description. The text up to the first blank line in a commit message is treated as the commit title, and that title is used throughout Git. For example, git-format-patch[1] turns a commit into email, and it uses the title on the Subject line and the rest of the commit in the body.



### Git Tracks Content not Files

Many revision control systems provide an add command that tells the system to start tracking changes to a new file. Git’s add command does something simpler and more powerful: git add is used both for new and newly modified files, and in both cases it takes a snapshot of the given files and stages that content in the index, ready for inclusion in the next commit.



### Viewing Project History 

	` git log ` # At any point you can view the history of changes using
	` git log -p ` # To see complete diffs at each step
	` git log --stat --summary ` # Often the overview of the change is useful to get a feel for each step



### Managing Branches

	` git branch experimental ` # Create the branch
	` git branch ` # To get a list of all existing branches. Asterisk marks branch you're currently on.

	` git switch my-branch ` # To switch to my-branch


To merge changes made in my-branch to master, while in master type;

	` git merge my-branch`


TO get a nice graphical representation of the resulting history, use;

	` gitk `


After merging and when you're happy, can delete my-branch with;

	` git branch -d my-branch ` # Ensures changes in my-branch are already in the current branch

If you develop a branch crazy idea, then regret it, you can delte the branch with;

	` git branch -D crazy-idea `



### Using Git for Collaboration

Suppose that Alice has started a new project with a Git repository in /home/alice/project, and that Bob, who has a home directory on the same machine, wants to contribute.

Bob begins with:
	` bob$ git clone /home/alice/project myrepo

If Bob makes changes and commits (ie with `git commit -a`, when he's ready he tells Alice to pull changes from the repo at `/home/bob/myrepo` she does with;

	` alice$ cd /home/alice/project `
	` alice$ git pull /home/bob/myrepo master `

This changes Bob's "master" branch into Alice's current branch. If she's made changers herself, will need to manually fix. The "pull" command thus performs two operations: it fetches changes from a remote branch, then merges them into the current branch. 

Note in general, Alice would want her local changes committed, before initiating the "pull". If Bob's work conflicts with what Alice did since her histories forked, Alice will use her working tree and index to resolve conflicts, and existing local changes will interfere with the conflict resiltuon process. (Git will still perform the fetch but will refuse to merge --- Alice will have to get rid of her local changes in some way and pull again when this happens).

Alice can then peek at what Bob did without merging first using `fetch`. Allows Alice to inspect what Bob did, using a special symbol "FETCH_HEAD" in order to determine if he has anything worth pulling;

	` alice$ fetch /home/bob/myrepo master `
	` alice$ git log -p HEAD..FETCH_HEAD `

This operation is safe even if Alice has uncommitted local changes. The range notation "HEAD..FETCH_HEAD" means "show everything that is reachable from the FETCH_HEAD but exclude anything that is reachable from HEAD". Alice already knows everything that leads to her current state (HEAD), and reviews what Bob has in his state (FETCH_HEAD) that she has not seen with this command.


If Alice wants to visualise what Bob did since their histories forked she can use;

	` gitk HEAD..FETCH_HEAD `


Two dot notation, can use three dot notation to view what BOTH of them have done since forking;

	` gitk HEAD...FETCH_HEAD `


This means "show everything that is reachable from either one, but exclude anything that is reachable from both of them".

These range notations can be used with both `gitk` and "git log".


After inspecting what Bob did, if there is nothing urgent, Alice may decide to continue working without pulling from Bob. If Bob’s history does have something Alice would immediately need, Alice may choose to stash her work-in-progress first, do a "pull", and then finally unstash her work-in-progress on top of the resulting history.

When working in closely knit group, not unusual to interact with the same repo over and over. By defining a remote repo shorthand, you can make it easier;

	` alice$ git remote add bob /home/bob/myrepo `


With this, Alice can perform the first part of the "pull" operation alone using the git fetch command without merging them with her own branch, using:

	` alice$ git fetch bob `


Unlike longhand form, when Alice fetches Bob using a remote repo shorthand, set up with `git remote`, what was fetched is stored in a remote-tracking branch, in this case `bob/mnaster`, so after this;

	` alice$ git log -p master..bob/master `


Shows a list of all changes Bob made since he branched from Alice's master branch. After inspecting changes, Alice could merge changes into her master branch;

	` alice$ git merge bob/master `


Merge can also be done by pulling her own remote-tracking branch, like;

	` alice$ git pull . remotes/bob/master `


Note `git pull` always merges into the current branch, regardless of what else is given on the CL. Later, Bob can update his repo with Alice's latest change using;

	` bob$ git pull `


Note that he doesn’t need to give the path to Alice’s repository; when Bob cloned Alice’s repository, Git stored the location of her repository in the repository configuration, and that location is used for pulls:

	` bob$ git config --get remote.origin.ulr ` # This will show `/home/alice/project`


 
Git also keeps a pristine copy of Alice's master branch under the name "origin/master":

	` bob$ git branch -r `


If Bob later decides to work from a different host, he can still performe clones and pulls using the ssh protocol;

	` bob$ git clone alice.org:/home/alice/project myrepo `


Alternatively, Git has a native protocol, or can use http; see git-pull[1] for details.



### Exploring History
