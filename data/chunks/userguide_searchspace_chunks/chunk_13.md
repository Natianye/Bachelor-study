# Search Spaces
## Constructing Full Search Spaces
### Constructing from a Dataframe

[`SearchSpace.from_dataframe`]() constructs a search space from a given dataframe.
Due to the ambiguity between discrete and continuous parameter representations when identifying parameter ranges based only on data, this function requires that the appropriate parameter definitions be explicitly provided. This is different for its subspace counterparts [`SubspaceDiscrete.from_dataframe`]() and [`SubspaceContinuous.from_dataframe`](), where a fallback mechanism can automatically infer minimal parameter specifications if omitted.

```python
from baybe.searchspace import SearchSpace

p_cont = NumericalContinuousParameter(name="c", bounds=[0, 1])
p_disc = NumericalDiscreteParameter(name="d", values=[1, 2, 3])
df = pd.DataFrame({"c": [0.3, 0.7], "d": [2, 3]})
searchspace = SearchSpace.from_dataframe(df=df, parameters=[p_cont, p_disc])
print(searchspace)
```

```default
SearchSpace
   Search Space Type: HYBRID
   SubspaceDiscrete
      Discrete Parameters
           Name                        Type  Num_Values Encoding
         0    d  NumericalDiscreteParameter           3     None
      Experimental Representation
            d
         0  2
         1  3
      Constraints
         Empty DataFrame
         Columns: []
         Index: []
      Computational Representation
            d
         0  2
         1  3
   SubspaceContinuous
      Continuous Parameters
           Name                          Type  Lower_Bound  Upper_Bound
         0    c  NumericalContinuousParameter          0.0          1.0
      Linear Equality Constraints
         Empty DataFrame
         Columns: []
         Index: []
      Linear Inequality Constraints
         Empty DataFrame
         Columns: []
         Index: []
      Non-linear Constraints
         Empty DataFrame
         Columns: []
         Index: []
```