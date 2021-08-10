# Basic GitHub Usage

Based on this video: https://www.youtube.com/watch?v=GgjIvUrOpmg

## Worflow

### Starting New Branch

Check what branches exist with

	` git branch -a `



Make a new branch

	` git branch my-branch ` # Recommend to name the branch after yourself and the feature, ie euan-feature





### Once You Make a Change, Add, Commit and Push

If you make a change, use the below

	` git add -A `
	` git commit -m `



Can check the log to see who's added what

	` git lg `



Push the commits to github

	` git push --set-upstream origin my-branch `





### Pull Request (from GitHub)

Can pull from the GitHub account. This will merge your branch with the master branch

Can press "Compare & pull request" button on GitHub page, will pop up after you've pushed to GitHub

OR

1. Go to "Pull requests" tab
2. Press "New pull request"
3. Set base as "master", set compare to "my-branch". Will tell you if you can merge it.
4. Then create pull request with button. Can give it a name and add some comments.
5. Submit. Others in the team can add comments before the final merge.
6. Once you're all happy, can press the final merge and delete the branch my-branch





### Pull Request (from local/own PC)

Want to then pull the updated master from GitHub.

	` git co master ` # Checkout the master
	` git pull ` # To pull the changed master locally
	` git log ` # To check proper merging of GitHub master with local
	` git branch --delete my-branch ` # To delete local branch
	` git branch --delte -r origin/my-branch ` # To delete the local tracking branch as well





### Handling Conflicts

Basically just do the above but if it conflicts with a change made to the master branch etc. Push it to git and then go to GitHub. Keep going and open a pull request.

If there's a conflict, it will automatically tell you that there's a conflict and won't let you merge, but you can still create a merge request. Can resolve the conflict on GitHub, isolating where the conflict was.






### General Visualisation

Can go to "Graphs" tab and look at the timeline of branches/merges etc
