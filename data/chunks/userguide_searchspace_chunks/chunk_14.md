# Search Spaces
## Restricting Search Spaces Using Constraints

Most constructors for both subspaces and search spaces support the optional keyword argument `constraints` to provide a list of [`Constraint`]() objects.
When constructing full search spaces, the type of each constraint is checked, and the consequently applied to the corresponding subspace.

```python
constraints = [...]
# Using one example constructor here
searchspace = SearchSpace.from_product(parameters=parameters, constraints=constraints)
```

