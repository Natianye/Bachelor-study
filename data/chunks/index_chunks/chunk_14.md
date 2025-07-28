# BayBE — A Bayesian Back End for Design of Experiments
## 📡 Telemetry

BayBE collects anonymous usage statistics **only** for employees of Merck KGaA,
Darmstadt, Germany and/or its affiliates. The recording of metrics is turned off for
all other users and is impossible due to a VPN block. In any case, the usage statistics
do **not** involve logging of recorded measurements, targets/parameters or their names
or any project information that would allow for reconstruction of details. The user and
host machine names are anonymized with via truncated hashing.

- You can verify the above statements by studying the open-source code in the
  `telemetry` module.
- You can always deactivate all telemetry by setting the environment variable
  `BAYBE_TELEMETRY_ENABLED` to `false` or `off`. For details please consult
  [this page](https://emdgroup.github.io/baybe/stable/userguide/envvars.html#telemetry).
- If you want to be absolutely sure, you can uninstall internet related packages such
  as `opentelemetry*` or its secondary dependencies from the environment. Due to the
  inability of specifying opt-out dependencies, these are installed by default, but the
  package works without them.