# Utilities
## Adding Fake Target Measurements and Parameter Noise

When creating test scripts, it is often useful to try the recommendation loop for a few
iterations. However, this requires some arbitrary target measurements to be set. Instead
of coming up with a custom logic every time, you can use the
[`add_fake_measurements`]() utility to add fake target
measurements and the [`add_parameter_noise`]()
utility to add artificial parameter noise:

```python
from baybe.utils.dataframe import add_fake_measurements, add_parameter_noise

# Get recommendations
recommendations = campaign.recommend(5)

# Add fake target measurements and artificial parameter noise to the recommendations.
# The utilities modify the dataframes inplace.
measurements = recommendations.copy()
add_fake_measurements(measurements, campaign.targets)
add_parameter_noise(measurements, campaign.parameters)

# Now continue the loop, e.g. by adding the measurements...
```