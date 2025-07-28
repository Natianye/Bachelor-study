# Search Spaces
## Discrete Subspaces
### Creating a Simplex-Bound Discrete Subspace

[`SubspaceDiscrete.from_simplex`]() can be used to efficiently create a discrete search space (or discrete subspace) that is restricted by a simplex constraint, limiting the maximum sum of the parameters per dimension.
This method uses a shortcut that removes invalid candidates already during the creation of parameter combinations and avoids to first create the full product space before filtering it.

In the following example, a naive construction of the subspace would first construct the full product space, containing 25 points, although only 15 points are actually part of the simplex.

```python
parameters = [
    NumericalDiscreteParameter(name="p1", values=[0, 0.25, 0.5, 0.75, 1]),
    NumericalDiscreteParameter(name="p2", values=[0, 0.25, 0.5, 0.75, 1]),
]
subspace = SubspaceDiscrete.from_simplex(max_sum=1.0, simplex_parameters=parameters)
```

```default
       p1    p2
 0   0.00  0.00
 1   0.00  0.25
 2   0.00  0.50
 ..   ...   ...
 12  0.75  0.00
 13  0.75  0.25
 14  1.00  0.00

 [15 rows x 2 columns]
```

Note that it is also possible to provide additional parameters that then enter in the form of a Cartesian product.
These can be provided via the keyword `product_parameters`.
