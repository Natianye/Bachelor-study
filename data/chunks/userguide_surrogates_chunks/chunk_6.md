# Surrogates
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