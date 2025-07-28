# Active Learning

When deciding which experiments to perform next, e.g. for a data acquisition campaign
to gather data for a machine learning model, it can be beneficial to follow a guided
approach rather than selecting experiments randomly. If this is done via iteratively
measuring points according to a criterion reflecting the current model’s uncertainty,
the method is called **active learning**.

Active learning can be seen as a special case of Bayesian optimization: If we have the
above-mentioned criterion and set up a Bayesian optimization campaign to recommend
points with the highest uncertainty, we achieve active learning via Bayesian
optimization. In practice, this is procedure is implemented by setting up a
probabilistic model of our measurement process that allows us to quantify uncertainty
in the form of a posterior distribution, from which we can then construct an
uncertainty-based acquisition function to guide the exploration process.

Below you find which acquisition functions in BayBE are suitable for this endeavor,
including a few guidelines.