# Contributing to BayBE
## Developer Tools

In order to maintain a high code quality, we use a variety of code developer tools.
When following the above described workflow, [pre-commit](https://pre-commit.com/)
will automatically trigger (most) necessary checks during your development process.
In any case, these checks are also conducted in our CI pipeline, which must pass
before your pull request is considered ready for review.
If you have questions or problems, simply ask for advice.

| Tool                                                                                            | Purpose                                   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------|
| [ruff](https://docs.astral.sh/ruff/)                                                            | code linting and formatting               |
| [mypy](https://mypy.readthedocs.io/)                                                            | static type checking                      |
| [pydocstyle](http://www.pydocstyle.org/)   <br/> [pydoclint](https://github.com/jsh9/pydoclint) | analyzing docstrings                      |
| [typos](https://github.com/crate-ci/typos)                                                      | basic spell checking                      |
| [pytest](https://docs.pytest.org/)                                                              | testing                                   |
| [pytest-cov](https://pytest-cov.readthedocs.io/)                                                | measuring test coverage                   |
| [sphinx](https://www.sphinx-doc.org/)                                                           | generating our documentation              |
| [pip-audit](https://github.com/pypa/pip-audit)                                                  | detecting vulnerabilities in dependencies |
| [tox](https://tox.wiki/)                                                                        | orchestrating all the above               |

Executing a specific one of these tools is easiest by using the corresponding
[tox](https://tox.wiki/) environment,

```console
tox -e <env>
```

where `<env>` is any of the environment names found via `tox list`.

<a id="code-design"></a>