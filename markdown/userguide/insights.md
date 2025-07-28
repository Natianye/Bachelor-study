# Insights

In BayBE, insights provide a way of analyzing your experimental results beyond what is
required for the basic measure-recommend loop. Dependencies needed for insights are
optional and available by installing `baybe` with the respective dependency group, e.g.
via `pip install baybe[insights]`.

## Parameter Importance via SHAP

[**SH**apley **A**dditive ex**P**lanations](https://shap.readthedocs.io/en/latest/index.html)
are a popular way of interpreting models to gain insight into the importance of the
features utilized. In the context of Bayesian optimization (BO), this enables analyzing
the importance of the parameters spanning the search space. This can be useful
for identifying which parameters play a key role and which do not – learnings that can
be applied in designing future campaigns. The interface is provided by the
[`SHAPInsight`]() class.

### Basic Usage

A [`SHAPInsight`]() can be obtained in several ways:

- From a [`Campaign`]() via
  [`from_campaign`]():
  ```python
  insight = SHAPInsight.from_campaign(campaign)
  ```
- From a surrogate model via [`from_surrogate`]():
  ```python
  insight = SHAPInsight.from_surrogate(surrogate, data)
  ```
- From a recommender that has an underlying surrogate model and implements
  [`get_surrogate`]()
  via [`from_recommender`]():
  ```python
  insight = SHAPInsight.from_recommender(recommender, searchspace, objective, data)
  ```

In these examples, `data` is the background data used to build the underlying explainer
model. Typically, you would set this to the measurements obtained during your
experimental campaign (for instance, [`from_campaign`]()
automatically extracts the `measurements` from the `campaign` object).

### Plots

After creating the insight, various methods are available to visualize the results via
the [.plot]()
interface, please refer to [available SHAP plots]().

```python
insight.plot("bar")
```

![SHAP_Bar_Exp_Rep](_static/insights/shap_bar_exp_rep.svg)

This result agrees well with the chemical intuition that ligands are the most important
reactants to activate the conversion, resulting in higher yields.

Such plots can also be created for data sets other than the background data that
was used to generate the insight. If this is desired, pass your data frame as second
argument:

```python
insight.plot("beeswarm", new_measurements)
```

![SHAP_Beeswarm_Exp_Rep](_static/insights/shap_beeswarm_exp_rep.svg)

The `force` plot type requires the user to additionally select which single data point
they want to visualize by specifying the corresponding `explanation_index`:

```python
insight.plot(
    "force", explanation_index=3
)  # plots the force analysis of the measurement at positional index 3
```

![SHAP_Force](_static/insights/shap_force.svg)

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
