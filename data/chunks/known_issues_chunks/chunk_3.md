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

