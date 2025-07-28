# Targets
## Limitations

#### IMPORTANT
`NumericalTarget` enables many use cases due to the real-valued nature of most
measurements. But it can also be used to model categorical targets if they are ordinal.
For example: If your experimental outcome is a categorical ranking into “bad”,
“mediocre” and “good”, you could use a `NumericalTarget` with bounds (1, 3), where the
categories correspond to values 1, 2 and 3 respectively.
If your target category is not ordinal, the transformation into a numerical target is
not straightforward, which is a current limitation of BayBE.
We are looking into adding more target options in the future.