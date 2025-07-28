# Environment Variables
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