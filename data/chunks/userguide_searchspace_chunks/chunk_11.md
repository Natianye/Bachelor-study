# Search Spaces
## Constructing Full Search Spaces

There are several methods available for creating full search spaces.
### From the Default Constructor

It is possible to construct a search space by simply using the default constructor of the `SearchSpace` class.
The required parameters are derived from the `__init__` function of that class.
In the simplest setting, it is sufficient to provide a single subspace for creating either a discrete or continuous search, or provide two subspaces for creating a hybrid search space.

```python
searchspace = SearchSpace(discrete=discrete_subspace, continuous=continuous_subspace)
```

While this constructor is the default choice, it might not be the most convenient.
Consequently, other constructors are available.