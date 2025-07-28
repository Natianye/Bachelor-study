# Known Issues

## Installation Related Issues

### macOS-arm64 – Leaked Semaphore

We know of a number of instances where BayBE fails during runtime on macOS-arm64
systems. In particular M1 seems to be affected.

The issues often contain a reference to `semaphore`, e.g.
`UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown`.
While we do not know the exact source of the problem, it seems to be related to linked
libraries that need to be compiled from source when no `macOS-arm64` binaries are
available. Packages that seem to have regular problems are `pymatgen` or `matminer`.

### CPUs without AVX support – Installation of `polars`

The package `polars` that can be installed as an optional dependency is only supported for
CPUs with AVX support. As a consequence, you might not be able to install the optional dependency.
This is in particular the case for M1 Macs, as these do not offer this support.

### Windows – Torch Problems

Reports of crashes during runtime on Windows machines often stem from a faulty `torch`
installation, e.g. wrongly installed CUDA-`torch` combinations. Errors look like
`OSError: [WinError 126] The specified module was not found. Error loading  C:\Users\xxxx\AppData\Roaming\Python\Python310\site-packages\torch\lib\shm.dll or one of its dependencies`

## PyCharm vs. `exceptiongroup`

BayBE’s (de-)serialization machinery is build upon `cattrs`, which in turn relies on
`ExceptionGroup`s to report problems in a nicely structured format when using its
[detailed validation](https://catt.rs/en/stable/validation.html#detailed-validation)
feature. However, `ExceptionGroup`s were introduced in Python 3.11 and are
therefore not usable with earlier Python versions. To
enable the feature nevertheless, `cattrs` uses the [exceptiongroup
backport](https://pypi.org/project/exceptiongroup/), which enables the same
functionality by monkeypatching `TracebackException` and installing a special
exception hook on `sys.excepthook`.

The changes attempted by `exceptiongroup` will only be executed if **no prior
modifications have been made**. However, PyCharm appears to make similar modifications
for its own purposes, blocking those of `exceptiongroup` and thus preventing the
exceptions from being properly thrown in detailed validation mode.

The chances of encountering this problem when interacting with BayBE are rather low
as the (de-)serialization objects are usually created by BayBE itself under normal
operation, so there is little risk of them being invalid in the first place. A
potential situation where you might run into the problem is if you manually
write a BayBE configuration and try to deserialize it into a Python BayBE object.
This can happen, for example, while engineering the configuration for later API
calls and testing it locally **using PyCharm**.
