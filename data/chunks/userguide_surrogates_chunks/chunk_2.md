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