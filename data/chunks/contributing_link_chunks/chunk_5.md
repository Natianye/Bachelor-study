# Contributing to BayBE
## Code Design

When reading BayBE’s code, you will notice certain re-occurring design patterns.
These patterns are by no means enforced, but following them can streamline your
own development process:

* We build most our classes with [attrs](https://www.attrs.org/), which is useful
  for lean class design and attribute validation.
* Our (de-)serialization machinery is built upon [cattrs](https://catt.rs/), separating
  object serialization from class design.
* The modular nature of BayBE’s components is reflected in our test suite through
  the use of [hypothesis](https://hypothesis.readthedocs.io/) property tests.