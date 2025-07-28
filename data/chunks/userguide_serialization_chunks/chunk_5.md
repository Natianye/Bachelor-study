# Serialization
## Deserialization from configuration strings
### Using default values

Just like default values can be omitted when working in Python,
they can be omitted from the corresponding serialization string:

```python
from baybe.parameters import CategoricalParameter

p1 = CategoricalParameter(name="Setting", values=["low", "high"])
p2 = CategoricalParameter(name="Setting", values=["low", "high"], encoding="OHE")

p1_json = """
{
    "name": "Setting",
    "values": ["low", "high"]
}
"""
p2_json = """
{
    "name": "Setting",
    "values": ["low", "high"],
    "encoding": "OHE"
}
"""

p1_via_json = CategoricalParameter.from_json(p1_json)
p2_via_json = CategoricalParameter.from_json(p2_json)

assert p1 == p1_via_json == p2 == p2_via_json
```