# Known Issues
## Installation Related Issues

### Windows – Torch Problems

Reports of crashes during runtime on Windows machines often stem from a faulty `torch`
installation, e.g. wrongly installed CUDA-`torch` combinations. Errors look like
`OSError: [WinError 126] The specified module was not found. Error loading  C:\Users\xxxx\AppData\Roaming\Python\Python310\site-packages\torch\lib\shm.dll or one of its dependencies`