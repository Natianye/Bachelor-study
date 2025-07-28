# Insights
## Parameter Importance via SHAP
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