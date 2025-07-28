# Asynchronous Workflows

Asynchronous workflows describe situations where the loop between measurement and
recommendation is more complex and needs to incorporate various other aspects. These
could for instance be:

- **Distributed workflows**: When recommendations are distributed across several
  operators, e.g. at different locations or in several reactors, some experiments might
  have been started, but are not ready when the next batch of recommendations is requested.
  Without further consideration, the algorithm would be likely to recommend the pending
  experiments again (since they were and still are considered most promising), as it is
  unaware they were already started.
- **Partial targets**: When dealing with multiple targets that require very different
  amounts of time to measure, the targets of previously recommended points might only be
  partially available when requesting the next batch of recommendations. Still, these
  partial experiments should ideally be considered when generating the recommendations.

With *pending experiments* we mean experiments whose measurement process has
been started, but not yet completed by time of triggering the next set of
recommendations – this is typically the case when at least one of the configured
targets has not yet been measured.

There are two levels of dealing with such situations:

1. **Marking experiments as pending**: If an experiment is not completed (meaning at least one target is not yet measured), its
   data cannot be added as a regular measurement. However, it can be marked as pending via
   `pending_experiments` in `recommend`.
2. **Adding partial results**: If an experiment is partially completed (meaning at least one target has been
   measured), we can already update the model with the available information
   by adding a *partial* measurement.

<a id="pending-experiments"></a>