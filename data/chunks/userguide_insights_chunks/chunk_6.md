# Insights
## Parameter Importance via SHAP
### Experimental and Computational Representations

[`SHAPInsight`]() by default analyzes the experimental
representation of the measurements, i.e. the that specifies parameter and target values
in terms of their actual (physical) quantities. This comes with certain limitations:

A feature importance study can still be performed by looking at the computational
representation of the data points, activated by the `use_comp_rep` flag. Since all
entries in this representation are numeric by construction, there are no limitations on
the explainer type used. A study of the computational representation might also be
useful if a deeper analysis of descriptors used is of interest to the user. In general,
for each non-numerical parameter in the experimental representation, there will be
several descriptors the computational representation:

```python
insight = SHAPInsight.from_campaign(campaign, use_comp_rep=True)
insight.plot("bar")
```

![SHAP_Bar_Comp_Rep](_static/insights/shap_bar_comp_rep.svg)

In addition to SHAP-based explainers, we also support
[LIME](https://arxiv.org/abs/1602.04938) and
[MAPLE](https://papers.nips.cc/paper_files/paper/2018/hash/b495ce63ede0f4efc9eec62cb947c162-Abstract.html)
variants. For example:

```python
insight = SHAPInsight.from_campaign(
    campaign, explainer_cls="LimeTabular", use_comp_rep=True
)
insight.plot("bar")
```

![SHAP_Bar_Lime](_static/insights/shap_bar_lime.svg)

As expected, the result from [`LimeTabular`](https://shap.readthedocs.io/en/stable/generated/shap.explainers.other.LimeTabular.html#shap.explainers.other.LimeTabular) are very
similar to the results from the SHAP [`KernelExplainer`](https://shap.readthedocs.io/en/stable/generated/shap.KernelExplainer.html#shap.KernelExplainer) because
both methods involve linear local approximations.