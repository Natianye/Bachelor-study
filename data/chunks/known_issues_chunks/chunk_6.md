# Known Issues
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