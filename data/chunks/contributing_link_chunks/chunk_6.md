# Contributing to BayBE
## Extending BayBE’s Functionality

For most parts, BayBE’s code and functional components are organized into different
subpackages.
When extending its functionality (for instance, by adding new component subclasses),
make sure that the newly written code is well integrated into the existing package and
module hierarchy.
In particular, public functionality should be imported into the appropriate high-level
namespaces for easier user import. For an example, see our
[parameter namespace](https://github.com/emdgroup/baybe/blob/main/baybe/parameters/__init__.py).