# Writing a paper in LaTeX with git

This repository is a template repository for writing papers in LaTeX. It contains a tufte-latex template for a handout - but more importantly it contains a GitHub action to compile the .tex files whenever there is a new commit. So in principle, you can write a paper in the GitHub editor, without ever needing to install a TeX compiler. A knockoff Overleaf without all the good features - but with better git integration.

It also has some guidelines and tutorials for the right workflow to make this type of editing work well, with justifications for why they are worth the effort.

# Why use git with GitHub instead of just Overleaf?

The basic reason to use git with GitHub instead of just using Overleaf is to keep track of document history in a sensible way, and to separate comments about the development of the paper from the actual LaTeX code of the paper itself. We also want to make use of the branches and pull requests features to get around the frustrations of editing each others' proofs and then having a hard time telling what was changed.

We can also make use of the GitHub issue tracker to keep track of changes that need to be made, instead of writing a comment that something needs to change inside of the actual LaTeX document.

The ideal is that the version of the paper in the main branch of the repository is always in a nice and readable state, without scratchpadding or scattered meta comments - it may be very incomplete, but what is in there should look like it is ready to be submitted.

# The general git development workflow

We will assume that you already know the basics of how git works, so these instructions are intended to explain the right workflow to use it efficiently, not to explain those basics. If you do not know the basics, there is a decent [guide to the theory](https://idrissi.eu/post/git-2-theory) here. For the practical side, see the software suggestions heading.

You want the main branch to always be in a state of "ready to publish except with holes and omissions" - things should either not be there at all, or be in there in a state where you are happy for a reviewer to read it.

When you start working on a new lemma or theorem, create a new branch for this, and work on it in that branch. Then, when it is in a state you are happy to include in the paper, create a pull request - and your collaborators can see the changes being made in the pull request, and comment on them and discuss before it is merged into main.

If your branch involves changes to other places in the paper that someone else is also working on, it may make sense to have a treelike structure of one branch for both your changes, and then branches off of that branch for your two interacting lemmas that you are editing. You can then merge your sub-branches into that branch more regularly, to keep each other's notations aligned, without needing to merge things into main until both lemmas are up to date and harmonized with each other.

# Software suggestions

The [GitHub Desktop client](https://desktop.github.com/) should be more than sufficient for your git needs. For actual editing of the LaTeX, as mentioned in the intro you can theoretically do without, since the Continuous Integration will compile things for you. In practice, you probably want an actual LaTeX editor for any serious needs.

# Do's and Do nots/Patterns and antipatterns

There are some things that make sense to do when editing in a "linear" fashion with no or little versioning that are bad practices when working in git. Here are some of them:

1. Never remove sections by commenting them out. Remove them entirely - they will still be available in the version history, and the removal of the text will be visible in the diff of the commit, while a commenting-out is much less obvious in the diff.
2. Never define commands for complicated expressions. If you have some quantity that you do not yet know the exact expression for, do not do something like `\newcommand{thatUnknownQuantity}{\alpha}` and then write `Thus, we have seen that $\phi(x) < \thatUnknownQuantity^3`, intending to later replace the `\alpha` by what you find the quantity should be.
What is going to happen is that you discover that it should be $(\beta + 1)^2$, edit that into your `\newcommand`, and start working elsewhere with that, getting lines like `\sqrt{\thatUnknownQuantity}+2 = \beta + 3`. Then you change your notation, edit your `\thatUnknownQuantity` to instead be $\log(\gamma)$, and suddenly your previously sensible line says $\sqrt{\log(\gamma)} + 2 = \beta + 3$ with no justification - and there is absolutely no way to find all these nonsense spots without reading through the entire paper to find every place you used `\thatUnknownQuantity` and trying to remember what that command was defined as at the time you wrote the command.
Your version history will be no help here either - a change of the definition of `\thatUnknownQuantity` will cause your actual displayed text to change without being a change in that location in the source of the document that you can search for in version history. This is ***bad***. You may think you are saving yourself effort, but in the long term, you are not.
What you should do instead is the same thing you would do in handwritten notes - write *in the actual text* that "we let $\alpha$ be this unknown quantity", write `\alpha` in the source code, and then when you discover what it should be, edit each instance of `\alpha` to the right thing. This will be visible in the version history, and in the long term much easier to work with.
3. Do be very willing to split sections out into their own individual documents. It makes it easier to get an overview of the history of each section.
4. Try to avoid leaving comments in the actual document about pretty much anything except possibly how unusually complicated LaTeX expressions work. The source of the paper is not the right place for discussions about how it should develop - have those discussions in the comments on pull requests of changes, or in the issue tracker. Comments explaining the reason for a change belong in the commit message of the change, not in the source itself.
5. Avoid "scratchpadding" in the main branch - things in the main branch should not need to be cleaned up later, they should be in a ready state. Of course, one may discover errors or possible improvements that necessitate changes - but if one is *aware* of changes that still need to be made, the branch should not be merged into the main branch before those changes have been made.
6. Commits should be atomic, unless they are just a few typo fixes. That is, each commit should contain one logical unit of changes to one specific thing. For example, if you are changing your notation from $\alpha$ to $\mathcal{A}$, you should have a single commit where every instance of `\alpha` is changed to `\mathcal{A}`. If you are changing a step in a proof, the commit should contain only those changes. So, you should neither be committing logically disjoint changes in the same commit, nor splitting logical units of change into multiple commits. If each branch reflects the logical unit of a theorem or a lemma, each commit should also be a smaller logical unit inside the theorem.
7. There should be no `.tex` files in the repo that are not included into the actual paper. At a glance, one will assume that everything in there will be included into the actual paper, so make sure this assumption is true. When editing in a linear fashion, like on Overleaf, it can make sense to move large sections one removes into a non-included file with a name like `lemma_3_backup.tex` - this is not necessary in git, since the removed text will still be there in the version history, and should be avoided as unnecessarily confusing.
8. Commit messages should be used to explain why a change was made - what was wrong with the previous version or why the new version is better. Use them to save your collaborators the work of figuring out why a change was made.

These standards should be adhered to very strictly in the main branch, but can be much slacker inside a branch in progress - the branch should converge to following these standards as it matures towards being ready to merge into the main branch.
