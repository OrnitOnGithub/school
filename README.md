# Share your revision sheets and notes
This github repo was made to share your revision sheets.

Here you can find revision sheets and notes from all subjects.

Sometimes it may be worth checking out [the contributions branch](https://github.com/OrnitOnGithub/school/tree/contributions) to find more information. The `master` branch is kind of like the official branch. It recieves the changes from `contributions` a bit later since they usually get modified before getting merged into `master`.

# Contribute
- Check [the rules](#Rules)
- make changes or add your file
- create a pull request. If you do not know how to do this, check out [the tutorial](#how-to-create-a-PR).

# Rules
- Preferably have your file in markdown format
- If a revision sheet not too different from yours exists, consider contributing to the existing one rather than making your own.
- Of course place everything in the right folder
   - Folders work like this: `Subject/Chapter/document.md`
- Commit messages don't have to be very detailed, but still make it clear what you did.

# How to create a PR

You can also do this more lazily with visual studio code's build-in git stuff.

- Fork the repository. This will create a copy of it on your own github account.
- Inside Visual Studio Code (The easiest way to do this) open a terminal and run `git clone url-of-your-fork`, for example `git clone https://github.com/ornitongithub/my-fork`
- This will create a new directory (folder). Open it with VS code or whatever.
- Create a new branch with the command `git checkout -b my-branch-name`
- Make all of your modifications.
- Add them all either with `git add .` or add specific ones with `git add path-to-file`
- Create a commit message with `git commit -m "Here's what I did in one simple sentence"`
- Add all the modifications to your online repository with `git push origin my-branch-name`
- Now on github, go to your fork repository and click "New Pull Request" and choose the branch `contributions` as the branch to push to.
- After this I will accept your PR.
