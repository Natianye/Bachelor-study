# Environment Variables
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