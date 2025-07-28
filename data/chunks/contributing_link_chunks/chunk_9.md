# Contributing to BayBE
## Writing classes
### Conventions for `attrs` classes

- Place attribute docstrings below the attribute declaration, not in the class
  docstring.
  Separate different attributes using a blank line.
  For example:
  ```python
  @define
  class Cookies:
    """A delicious recipe for chocolate-banana cookies."""

    chocolate: float
    """Chocolate is naturally measured in terms of floats."""

    bananas: int
    """For bananas, we use integers, of course."""
  ```
- Unless another more specific name is suitable, use our default naming convention for
  `attrs` defaults and validators:
  ```python
  @my_attribute.default
  def _default_my_attribute(self): ...

  @my_attribute.validator
  def _validate_my_attribute(self, attribute, value): ...
  ```

  A one-line docstring suffices for these methods, but they should have a `Raises:`
  section if applicable. Linter warnings regarding missing attribute docstrings can be
  silenced using `# noqa: DOC101, DOC103`.