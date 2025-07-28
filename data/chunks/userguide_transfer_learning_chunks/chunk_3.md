# Transfer Learning
## The Role of the TaskParameter

The [`TaskParameter`]() is used to “mark” the context of individual experiments and thus
to “align” different campaigns along their context dimension.
The set of all possible contexts is provided upon the initialization of a
[`TaskParameter`]() by providing them as `values`.
In the following example, the context might be one of several reactors in which
a chemical experiments can be conducted.

```python
from baybe.parameters import TaskParameter

TaskParameter(name="Reactor", values=["ReactorA", "ReactorB", "ReactorC"])
```

If not specified further, a campaign using the [`TaskParameter`]() as specified above
would now make recommendations for all possible values of the parameter. Using the
`active_values` argument upon initialization, this behavior can be changed such that
the `campaign` only makes recommendations for the corresponding values.

The following example models a situation where experimentation data from three
different reactors are available, but new experiments should only be conducted in
`ReactorC`.

```python
from baybe.parameters import TaskParameter

TaskParameter(
    name="Reactor",
    values=["ReactorA", "ReactorB", "ReactorC"],
    active_values=["ReactorC"],
)
```

The same pattern can be easily applied to other scenarios such as changing substrates
(while screening the same reaction conditions) or formulating mixtures for different cell lines:

```python
TaskParameter(
    name="Substrate",
    values=["3,5-dimethylisoxazole", "benzo[d]isoxazole", "5-methylisoxazole"],
    active_values=["3,5-dimethylisoxazole"],
)
TaskParameter(
    name="Cell_Line",
    values=["Liver cell", "Heart cell", "Hamster brain cell"],
    active_values=["Liver cell"],
)
```