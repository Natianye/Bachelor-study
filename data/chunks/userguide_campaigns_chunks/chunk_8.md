# Campaigns
## Getting Recommendations
### Caching of Recommendations

The `Campaign` object caches the last batch of recommendations returned, in order to
avoid unnecessary computations for subsequent queries between which the status
of the campaign has not changed.
The cache is invalidated as soon as new measurements are added or a different
batch size is desired.
The latter is necessary because each batch is optimized for the specific number of
experiments requested (see note above).
