# Surrogates

Surrogate models are used to model and estimate the unknown objective function of the
DoE campaign. BayBE offers a diverse array of surrogate models, while also allowing for
the utilization of custom models. All surrogate models are based upon the general
[`Surrogate`]() class. Some models even support transfer
learning, as indicated by the `supports_transfer_learning` attribute.

## Available Models

BayBE provides a comprehensive selection of surrogate models, empowering you to choose
the most suitable option for your specific needs. The following surrogate models are
available within BayBE:

* [`GaussianProcessSurrogate`]()
* [`BayesianLinearSurrogate`]()
* [`MeanPredictionSurrogate`]()
* [`NGBoostSurrogate`]()
* [`RandomForestSurrogate`]()

<a id="multi-output-modeling"></a>

## Multi-Output Modeling

Depending on the use case at hand, it may be necessary to model multiple output
variables simultaneously. However, not all surrogate types natively provide (joint)
predictive distributions for more than one variable, as indicated by their
`supports_multi_output` attribute.

In multi-output contexts, it may therefore be necessary to assemble several
single-output surrogates into a composite model to build a joint predictive model from
independent components for each output. BayBE provides two convenient mechanisms to
achieve this, both built upon the
`CompositeSurrogate` class:

### Surrogate Replication

The simplest way to construct a multi-output surrogate is to replicate a given
single-output model architecture for each of the existing output dimensions.

To replicate a given surrogate, you can either call its
`replicate()` method or use the
[`CompositeSurrogate.from_replication()`]()
convenience constructor:

```python
from baybe.surrogates import CompositeSurrogate, GaussianProcessSurrogate

composite_a = GaussianProcessSurrogate().replicate()
composite_b = CompositeSurrogate.from_replication(GaussianProcessSurrogate())

assert composite_a == composite_b
```

However, there are very few cases where such an explicit conversion is required. Because
using a single-output surrogate model in a multi-output context would trivially fail, and
because BayBE cares deeply about its users’ lives, it automatically performs this conversion
for you behind the scenes:

<a id="auto-replication"></a>

The consequence of the above is that you can use the same model object regardless
of the modeling context and its multi-output capabilities.

There is *one* notable exception where an explicit replication may still make
sense: if you want to bypass the existing multi-output mechanics of a surrogate that is
inherently multi-output compatible.

### Composite Surrogates

An alternative to surrogate replication is to manually assemble your
`CompositeSurrogate`. This can be useful if you want
to

* use the same model architecture but with different settings for each output or
* use different architectures for the outputs to begin with.

```python
from baybe.surrogates import (
    CompositeSurrogate,
    GaussianProcessSurrogate,
    RandomForestSurrogate,
)

surrogate = CompositeSurrogate(
    {
        "target_a": GaussianProcessSurrogate(),
        "target_b": RandomForestSurrogate(),
    }
)
```

A noticeable difference to the replication approach is that manual assembly requires
the exact set of target variables to be known at the time the object is created.

## Extracting the Model for Advanced Study

In principle, the surrogate model does not need to be a persistent object during
Bayesian optimization since each iteration performs a new fit anyway. However, for
advanced study, such as investigating the posterior predictions, acquisition functions
or feature importance, it can be useful to directly extract the current surrogate model.

For this, BayBE provides the `get_surrogate` method, which is available for the
[`Campaign`]() or for
[recommenders]().
Below an example of how to utilize this in conjunction with the popular SHAP package:

```python
# Assuming we already have a campaign created and measurements added
data = campaign.measurements[[p.name for p in campaign.parameters]]
model = lambda x: campaign.get_surrogate().posterior(x).mean

# Apply SHAP
explainer = shap.Explainer(model, data)
shap_values = explainer(data)
shap.plots.bar(shap_values)
```

## Using Custom Models

BayBE goes one step further by allowing you to incorporate custom models based on the
ONNX architecture. Note however that these cannot be retrained. For a detailed
explanation on using custom models, refer to the comprehensive examples provided in the
corresponding [example folder]().
