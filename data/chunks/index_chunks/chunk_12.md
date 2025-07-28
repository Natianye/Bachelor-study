# BayBE — A Bayesian Back End for Design of Experiments
## 💻 Installation
### From Local Clone

Alternatively, you can install the package from your own local copy.
First, clone the repository, navigate to the repository root folder, check out the
desired commit, and run:

```bash
pip install .
```

A developer would typically also install the package in editable mode (‘-e’),
which ensures that changes to the code do not require a reinstallation.

```bash
pip install -e .
```

If you need to add additional dependencies, make sure to use the correct syntax
including `''`:

```bash
pip install -e '.[dev]'
```