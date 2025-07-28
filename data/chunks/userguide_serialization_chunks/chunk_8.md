# Serialization
## Deserialization from configuration strings
### Using abbreviations

Classes that have an `abbreviation` class variable defined can be conveniently
deserialized using the corresponding abbreviation string:

```python
from baybe.acquisition.base import AcquisitionFunction

acqf1 = AcquisitionFunction.from_json('{"type": "UpperConfidenceBound"}')
acqf2 = AcquisitionFunction.from_json('{"type": "UCB"}')

assert acqf1 == acqf2
```

<a id="nested-objects"></a>