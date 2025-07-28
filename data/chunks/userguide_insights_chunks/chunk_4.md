# Insights
## Parameter Importance via SHAP
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