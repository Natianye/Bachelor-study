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