# BayBE — A Bayesian Back End for Design of Experiments
## ⚡ Quick Start
### Advanced Example: Chemical Substances

BayBE has several modules to go beyond traditional approaches. One such example is the
use of custom encodings for categorical parameters. Chemical encodings for substances
are a special built-in case of this that comes with BayBE.

In the following picture you can see
the outcome for treating the solvent, base and ligand in a direct arylation reaction
optimization (from [Shields, B.J. et al.](https://doi.org/10.1038/s41586-021-03213-y)) with
chemical encodings compared to one-hot and a random baseline:
![Substance Encoding Example](examples/Backtesting/full_lookup_light.svg)
