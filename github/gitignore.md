
# .gitignore

**Link:** https://www.atlassian.com/git/tutorials/saving-changes/gitignore

Git see every file in your working copy as one of three things:

1. **Tracked:** A file that has been previously staged or committed
2. **Untracked:** A file which has not been staged/committed
3. **Ignored:** A file which Git has been explicitly told to ignore

Ignored files are usually build artefacts & machine-generated files that can be derived from your repo soruce or should otherwise not be committed. Examples are:

* Dependency caches, such as the contents of /node_modules or /packages
* Compiled code, such as `.o`, `.pyc`, and `.class` files
* Build output directories, such as `/bin`, `/out`, or `/target`
* Files generated at runtime, such as `.log`, `.lock`, or `.tmp`
* Hidden system files, such as `.DS_Store` or `Thumbs.db`
* Personal IDE config files, such as `.idea/workspace.xml`

Ignored files are tracked in a special file called `.gitignore` that is checked in at the root of your repo. Must be edited and committed by hand with new files you wish to ignore. Contains patterns checked against filenames in repo.


# Shared .gitignore files in your repo

Can choose to define multiple `.gitignore` files in different directories. Each pattern in a particular `.gitignore` file is tested relative to the directory containing that file. Convention is just one in the root.


# Personal Git ignore rules

Can define personal ignore patterns for a particular repo in a special file at `.git/info/exclude`. These aren't versioned and not distributed with your repo, so its an appropriate places to include patterns that will likely only benefit you.


# Global Git ignore rules

Can define global Git ignore patterns for all repos on local system by setting the Git `core.excludesFile` property. Have to make `.gitignore` yourself that refers to this, putting in home is a good shout, using:

```{bash}

git config --global core.excludesFile ~/.gitignore

```


# Ignoring a previously committed file

If you want to ignore a previously committed file, need to delete it from the repo and then add it to `gitignore`. Using `--cached` with `git rm` means that the file will be deleted from your repo, but will remain in your working dir as an ignore file.

```{bash}

echo debug.log >> .gitignore
git rm --cached debug.log
rm 'debug.log'
git commit -m "Start ignoring debug.log"

```
Can omit `--cached` option if you want to delete the file from both the repo and your local file system.


# Committing an ignored file

It is possible to force an ignored file to be committed to the repo using the `-f` (`--force`) option with `git add`.

```{bash}

cat .gitignore *.log
git add -f debug.log
git commit -m "Force adding debug.log"

```

Might consider doing this with a general pattern (ie `*.log`), but want to commit a specific file. But a better solution is to define an exception to the general rule:

```{bash}

echo !debug.log >> .gitignore
cat .gitignore *.log !debug.log
git add debug.log
git commit -m "Adding debug.log"

```


# Stashing an ignored file

`git stash` is a powerful Git feature for temporarily shelving and reverting local changes. It ignores ignored files, only stashing tracked changes. Can invoke with `--all` to stash ignored & untracked files too#


# Debugging .gitignore files

If you have complicated `.gitignore` patterns or those spread over multiple `.gitignore` files, can be difficult to track down why a particular file is being ignored. Can use `git check-ignore -v` to detemine which pattern is causing a particular file to be ignored:

```{bash}

git check-ignore -v debug.log .gitignore:3:*.log debug.log

```

Can pass multiple filenames to `git check-ignore` if you like and the names themselves don't even have to correspond to files that exist in your repo.
