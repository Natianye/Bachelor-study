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