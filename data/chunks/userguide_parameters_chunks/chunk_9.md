# Parameters
## Discrete Parameters
### TaskParameter

Often, several experimental campaigns involve similar or even identical parameters but
still have one or more differences.
For example, when optimizing reagents in a chemical reaction, the reactants remain
constant, so they are not parameters.
Similarly, in a mixture development for cell culture media, the cell type is fixed and
hence not a parameter.
However, once we plan to mix data from several campaigns, both reactants and cell
lines can also be considered parameters in that they encode the necessary context.
BayBE is able to process such context information with the [`TaskParameter`]().
In many cases, this can drastically increase the optimization performance due to the
enlarged data corpus.

#### SEE ALSO
For details, refer to [transfer learning](transfer_learning.md).