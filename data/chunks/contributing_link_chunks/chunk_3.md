# Contributing to BayBE
## Synchronizing Pull Requests

A common situation encountered when submitting a pull request (PR) is that the upstream
branch has evolved since the moment your PR branch was created, and a synchronization
is needed in order to prepare your branch for a merge (e.g., to remove existing
conflicts).

Because we care about our Git history and would like to keep it clean and
easy to follow, we generally recommend **rebasing** your branch onto the latest
upstream commit in such situations, especially if your changes are orthogonal to what
has happened on the remote branch in the meantime. Compared to merging, this has the
advantage of keeping the history of your commits (and thus of the entire repository)
linear, and your own PR free of changes that happened remotely, which also
greatly simplifies the review process (e.g., it produces simpler diffs).

That said, the above is only a recommendation and by no means a requirement. However,
depending on the complexity of your PR commit history, we reserve the right to merge
your branch using a squash-rebase as a last resort to keep our history clean.
By following the guideline above, this step can be easily avoided in most cases.

<a id="developer-tools"></a>