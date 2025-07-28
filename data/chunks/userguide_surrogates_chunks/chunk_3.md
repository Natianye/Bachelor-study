# Surrogates
## Multi-Output Modeling

Depending on the use case at hand, it may be necessary to model multiple output
variables simultaneously. However, not all surrogate types natively provide (joint)
predictive distributions for more than one variable, as indicated by their
`supports_multi_output` attribute.

In multi-output contexts, it may therefore be necessary to assemble several
single-output surrogates into a composite model to build a joint predictive model from
independent components for each output. BayBE provides two convenient mechanisms to
achieve this, both built upon the
`CompositeSurrogate` class: