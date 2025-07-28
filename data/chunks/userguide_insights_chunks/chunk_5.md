# Insights
## Parameter Importance via SHAP
### Explainers

In general, SHAP is an exhaustive method testing all combinations of features. This
exhaustive algorithm (implemented by the [`shap.ExactExplainer`](https://shap.readthedocs.io/en/stable/generated/shap.ExactExplainer.html#shap.ExactExplainer) class) is
often not feasible in practice, and various approximate variants are available (see
[supported explainers]()). For details about their inner
mechanics, we refer to the [SHAP documentation](https://shap.readthedocs.io/en/latest/api.html#explainers).

The explainer can be changed when creating the insight:

```python
insight = SHAPInsight.from_campaign(
    campaign, explainer_cls="KernelExplainer"
)  # default explainer
```