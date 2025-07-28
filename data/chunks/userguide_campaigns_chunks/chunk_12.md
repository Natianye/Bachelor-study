# Campaigns
## Serialization

Like other BayBE objects, [`Campaigns`]() can be (de-)serialized
using their [`from_json`]()/
[`to_json`]() methods, which
allow to convert between Python objects and their corresponding representation in JSON
format:

```python
campaign_json = campaign.to_json()
reconstructed = Campaign.from_json(campaign_json)
assert campaign == reconstructed
```

General information on this topic can be found in our
[serialization user guide](serialization.md).
For campaigns, however, this possibility is particularly noteworthy as it enables
one of the most common workflows in this context –
persisting the current state of a campaign for long-term storage and continuing the
experimentation at a later point in time:

1. Get your campaign object
   * When initiating the workflow, create a new campaign object
   * When coming from the last step below, **deserialize** the existing campaign object
2. Add the latest measurement results
3. Get a recommendation
4. **Serialize** the campaign and store it somewhere
5. Run your (potentially lengthy) real-world experiments
6. Repeat

## Further Information

Campaigns are created as a first step in most of our
[examples]().
For more details on how to define campaigns for a specific use case, we thus propose
to have a look at the most suitable example.