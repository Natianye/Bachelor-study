# Serialization
## Deserialization from configuration strings

The workflow described [above](#json-serialization) most naturally applies to
situations where we start inside the Python ecosystem and want to make an object
leave the running session.
However, in many cases, we would like to kickstart the process from the other end and
rather specify a BayBE object **outside** Python for use in a later computation.
Common examples are when we wish to interact with an API or simply want to persist
a certain BayBE component in the form of a “configuration” file.

The following sections give an overview of the flexibilities that are offered for this
task. Of course, the underlying concepts can be mixed and matched arbitrarily.