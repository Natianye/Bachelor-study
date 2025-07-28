# Getting Recommendations
## Excluding Configurations
### Permanent Exclusion

Permanently excluding certain parameter configurations from the recommendation is
generally done by adjusting the `SearchSpace` object
accordingly, which defines the set of candidate configurations that will be considered.

BayBE provides several ways to achieve this, which we’ll illustrate by comparing against
the following “full” search space:

```python
searchspace_full = TaskParameter("p", ["A", "B", "C"]).to_searchspace()
```

Depending on the specific needs and complexity of the filtering operation, one approach
may be preferred over the other, but generally these mechanisms exist:

* Restricting individual parameter objects via `active_values`:
  ```python
  searchspace_reduced = TaskParameter(
      "p", ["A", "B", "C"], active_values=["A", "B"]
  ).to_searchspace()
  ```

  This is possible for all [label-like parameters](parameters.md#label-like).
* Specifying only a subset of configurations (discrete spaces only):
  ```python
  searchspace_reduced = SearchSpace.from_dataframe(
      pd.DataFrame({"p": ["A", "B"]}),
      parameters=[TaskParameter("p", ["A", "B", "C"])],
  )
  ```
* Filtering the search space using constraints:
  ```python
  searchspace_reduced = SearchSpace.from_product(
      parameters=[CategoricalParameter("p", ["A", "B", "C"])],
      constraints=[DiscreteExcludeConstraint(["p"], [SubSelectionCondition(["C"])])],
  )
  ```
* Using specialized constructors like
  `from_simplex()`.