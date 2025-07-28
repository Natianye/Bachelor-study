# Known Issues
## Installation Related Issues
### CPUs without AVX support – Installation of `polars`

The package `polars` that can be installed as an optional dependency is only supported for
CPUs with AVX support. As a consequence, you might not be able to install the optional dependency.
This is in particular the case for M1 Macs, as these do not offer this support.