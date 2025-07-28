# Environment Variables
## Polars

If BayBE was installed with the additional `polars` dependency (`baybe[polars]`), it
will use the advanced methods of Polars to create the searchspace lazily and perform a
streamed evaluation of constraints. This will improve speed and memory consumption
during this process, and thus might be beneficial for very large search spaces.

Since this is still somewhat experimental, you might want to deactivate Polars without
changing the Python environment. To do so, you can set the environment variable
`BAYBE_DEACTIVATE_POLARS` to any truthy value accepted by
[`strtobool`]().