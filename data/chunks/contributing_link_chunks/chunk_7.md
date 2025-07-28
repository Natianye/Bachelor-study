# Contributing to BayBE
## Writing Docstrings

Our docstrings generally follow the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
Basic style and consistency checks are automatically performed via
[pre-commit](https://pre-commit.com/) during development and in our CI pipeline.

Apart from that, we generally recommend adhering to the following guideline:

- Each function should have a docstring containing:
  * a short one-line summary at the top,
  * an optional extended summary or description below and
  * all relevant sections (`Args`, `Raises`, …).
- Use type hints (for variables/constants, attributes, function/method signatures, …).
  Avoid repeating type hints in docstrings.
- When referencing objects (classes, functions, …),
  use `:<key>:`path.to.function` ` where `<key>` is to be replaced with the
  respective [role](https://www.sphinx-doc.org/en/master/usage/domains/python.html#cross-referencing-python-objects)
  (`class`, `func`, …)
- Use double backticks for literals like in ```MyString```.