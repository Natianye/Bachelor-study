# Campaigns
## Creating a Campaign
### Creation From a JSON Config

Instead of using the default constructor, it is also possible to create a `Campaign`
from a JSON configuration string via
[`Campaign.from_config`]().
Herein, the expected JSON schema of the string should mirror the class
hierarchy of the objects nested in the corresponding campaign object.
The string can be easily validated using
[Campaign.validate_config]() without
instantiating the object, which skips the potentially costly search space creation step.
For more details and a full exemplary config, we refer to the corresponding
[example]().