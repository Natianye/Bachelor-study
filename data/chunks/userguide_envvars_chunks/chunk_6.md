# Environment Variables
## EXPERIMENTAL: Floating Point Precision

In general, double precision is recommended because numerical stability during optimization
can be bad when single precision is used. This impacts gradient-based optimization,
i.e. search spaces with continuous parameters, more than optimization without gradients.

If you still want to use single precision, you can set the following Boolean variables:

- `BAYBE_NUMPY_USE_SINGLE_PRECISION` (defaults to `False`)
- `BAYBE_TORCH_USE_SINGLE_PRECISION` (defaults to `False`)