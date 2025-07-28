# BayBE — A Bayesian Back End for Design of Experiments
## 💻 Installation
### Optional Dependencies

There are several dependency groups that can be selected during pip installation, like

```bash
pip install 'baybe[test,lint]' # will install baybe with additional dependency groups `test` and `lint`
```

To get the most out of `baybe`, we recommend to install at least

```bash
pip install 'baybe[chem,simulation]'
```

The available groups are:

- `extras`: Installs all dependencies required for optional features.
- `benchmarking`: Required for running the benchmarking module.
- `chem`: Cheminformatics utilities (e.g. for the `SubstanceParameter`).
- `docs`: Required for creating the documentation.
- `examples`: Required for running the examples/streamlit.
- `lint`: Required for linting and formatting.
- `mypy`: Required for static type checking.
- `onnx`: Required for using custom surrogate models in [ONNX format](https://onnx.ai).
- `polars`: Required for optimized search space construction via [Polars](https://docs.pola.rs/).
- `insights`: Required for built-in model and campaign analysis (e.g. using [SHAP](https://shap.readthedocs.io/)).
- `simulation`: Enabling the [simulation](https://emdgroup.github.io/baybe/stable/_autosummary/baybe.simulation.html) module.
- `test`: Required for running the tests.
- `dev`: All of the above plus dev tools. For code contributors.