# Contributing to BayBE

**All contributions to BayBE are welcome!**

… no matter if bug fixes, new features, or just typo corrections.

To shorten the overall development and review process, this page contains are a
few sections that can make your life easier.

## General Workflow

To implement your contributions in a local development environment,
we recommend the following workflow:

1. Clone a [fork](https://github.com/emdgroup/BayBE/fork) of the repository to
   your local machine.
2. Create and activate a virtual python environment using one of the supported
   python versions.
3. Change into the root folder of the cloned repository and install an editable version
   including all development dependencies:
   ```console
   pip install -e '.[dev]'
   ```
4. Run our tests to verify everything works as expected:
   ```console
   pytest
   ```
5. Install our [pre-commit](https://pre-commit.com/) hooks:
   ```console
   pre-commit install
   ```
6. Create a new branch for your contribution:
   ```console
   git checkout -b <your_branch_name>
   ```
7. **Implement your changes.**
8. Optional but recommended to prevent complaints from our CI pipeline:
   **Test your code.**

   There are several test environments you can run via `tox`, each corresponding to a
   [developer tool]() in a certain Python version.
   You can retrieve all available environments via `tox list`.
   For more information, see our [README about tests](https://github.com/emdgroup/baybe/blob/main/tests/README.md).

   For instance, running all code tests in Python 3.12 can be achieved via:
   ```console
   tox -e fulltest-py312
   ```

   Other tox tests that are useful to verify your work locally are `tox -e lint-py312`,
   `tox -e mypy-py312` and `tox -e coretest-py312`.

   If you want to challenge your machine, you can run all checks in all Python versions
   in parallel via:
   ```console
   tox -p
   ```

   This can be considered the ultimate one-stop check to make sure your code is ready
   for merge.
9. Push the updated branch back to your fork:
   ```console
   git push origin
   ```
10. Open a pull request via Github’s web page.