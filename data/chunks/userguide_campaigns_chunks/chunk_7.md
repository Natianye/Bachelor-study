# Campaigns
## Getting Recommendations
### Candidate Control in Discrete Spaces

For discrete search spaces, campaigns provide additional control over how the candidate
set of recommendable points is built based on the trajectory the campaign has taken so
far. This is done by setting the following Boolean flags:

- `allow_recommending_already_measured`:  Controls whether points that have already been
  measured can be recommended.
- `allow_recommending_already_recommended`: Controls whether previously recommended points can
  be recommended again.
- `allow_recommending_pending_experiments`: Controls whether points marked as
  `pending_experiments` can be recommended (see [asynchronous
  workflows](async.md#pending-experiments)).