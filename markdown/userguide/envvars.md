# Environment Variables

Several aspects of BayBE can be configured via environment variables.

## Basic Instructions

Setting an environment variable with the name `ENVVAR_NAME` is best done before calling
any Python code, and must also be done in the same session unless made persistent, e.g.
via `.bashrc` or similar:

```bash
ENVAR_NAME="my_value"
python do_baybe_work.py
```

Or on Windows:

```shell
set ENVAR_NAME=my_value
```

Note that variables set in this manner are interpreted as text, but converted internally
to the needed format. See for instance the [`strtobool`]()
converter for values that can be set so BayBE can interpret them as Booleans.

It is also possible to set environment variables in Python:

```python
import os

os.environ["ENVAR_NAME"] = "my_value"

# proceed with BayBE code ...
```

However, this needs to be done carefully at the entry point of your script or session and
will not persist between sessions.

## Telemetry

Monitored quantities:

* `batch_size` used when querying recommendations
* Number of parameters in the search space
* Number of constraints in the search space
* How often [`recommend`]() was called
* How often [`add_measurements`]() was called
* How often a search space is newly created
* How often initial measurements are added before recommendations were calculated
  (“naked initial measurements”)
* The fraction of measurements added that correspond to previous recommendations
* Each measurement is associated with a truncated hash of the user- and hostname

The following environment variables control the behavior of BayBE telemetry:

- `BAYBE_TELEMETRY_ENABLED`: Flag that can turn off telemetry entirely (default is
  `True`). To turn it off set it to `False`.
- `BAYBE_TELEMETRY_ENDPOINT`: The receiving endpoint URL for telemetry data.
- `BAYBE_TELEMETRY_VPN_CHECK`: Flag turning an initial telemetry connectivity check
  on/off (default is `True`).
- `BAYBE_TELEMETRY_VPN_CHECK_TIMEOUT`: The timeout in seconds for the check whether the
  endpoint URL is reachable.
- `BAYBE_TELEMETRY_USERNAME`: The name of the user executing BayBE code. Defaults to a
  truncated hash of the username according to the OS.
- `BAYBE_TELEMETRY_HOSTNAME`: The name of the machine executing BayBE code. Defaults to
  a truncated hash of the machine name.

## Polars

If BayBE was installed with the additional `polars` dependency (`baybe[polars]`), it
will use the advanced methods of Polars to create the searchspace lazily and perform a
streamed evaluation of constraints. This will improve speed and memory consumption
during this process, and thus might be beneficial for very large search spaces.

Since this is still somewhat experimental, you might want to deactivate Polars without
changing the Python environment. To do so, you can set the environment variable
`BAYBE_DEACTIVATE_POLARS` to any truthy value accepted by
[`strtobool`]().

## Disk Caching

For some components, such as the
[`SubstanceParameter`](), some of the
computation results are cached in local storage.

By default, BayBE determines the location of temporary files on your system and puts
cached data into a subfolder `.baybe_cache` there. If you want to change the location of
the disk cache, change:

```bash
BAYBE_CACHE_DIR="/path/to/your/desired/cache/folder"
```

By setting

```bash
BAYBE_CACHE_DIR=""
```

you can turn off disk caching entirely.

## EXPERIMENTAL: Floating Point Precision

In general, double precision is recommended because numerical stability during optimization
can be bad when single precision is used. This impacts gradient-based optimization,
i.e. search spaces with continuous parameters, more than optimization without gradients.

If you still want to use single precision, you can set the following Boolean variables:

- `BAYBE_NUMPY_USE_SINGLE_PRECISION` (defaults to `False`)
- `BAYBE_TORCH_USE_SINGLE_PRECISION` (defaults to `False`)
