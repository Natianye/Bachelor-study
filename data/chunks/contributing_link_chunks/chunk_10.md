# Contributing to BayBE
## Writing classes
### Method overrides

When overriding methods in subclasses, decorate them with `@typing_extensions.override`
to make the relationship explicit:

```python
from typing_extensions import override

class Parent:

   def le_method():
      """The method of the parent class."""
      ...

class Child:

   @override
   def le_method():
      """Overridden method of the child class."""
      ...
```

Using the decorator provides a type-safe approach for defining inheritance structures
that eliminates two potential sources of unintended class design:

* An intended override is does not occur because the method names differ between
  the parent and child classes (e.g. if the parent method is renamed)
* An unintended override occurs because a method name that exists in the parent class
  is used in the child class by mistake.
  In both cases, `mypy` will complain and force you to fix the problem.