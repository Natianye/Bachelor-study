# Transfer Learning

BayBE offers the possibility to mix data from multiple, *similar but not identical*
campaigns in order to accelerate optimization – a procedure called **transfer learning**.
This feature is automatically enabled when using a
[Gaussian process surrogate model]()
in combination with a [`TaskParameter`]().

## Unlocking Data Treasures Through Transfer Learning

A straightforward approach to combining data from different campaigns is to quantify
the differences between their contexts via one or few explicitly measured parameters
and then constraining these parameters in the active campaign to
the relevant context.

Examples where this is possible:

* **Optimization of a chemical reaction at different temperatures:**<br />
  \\\\
  Data obtained from a chemical reaction optimized at a certain temperature can be used
  in a new campaign, where the same reaction needs to be optimized again at a different
  temperature.
* **Optimization of a simulation involving a particle size:**<br />
  \\\\
  Data obtained at a smaller particle size can be utilized when starting a new
  optimization for a larger particle size or vice versa.

In these examples, the temperature and the particle size take the
role of *aligning* the individual measurement campaigns along their corresponding
context dimension. That is, the context is static *within* each campaign
(i.e., each campaign is executed at its fixed context parameter value) but the
parameter establishes an explicit relationship between the data gathered *across*
campaigns. Transfer of knowledge from one campaign to another can thus simply happen
through the existing mechanisms of a surrogate model by feeding the context
parameter as an additional regular input to the model.

Unfortunately, there are many situations where it can be difficult to quantify the
differences between the campaigns via explicit context parameters in the first place.
This might be the case if the parameters distinguishing the contexts

1. have not been recorded and cannot be measured anymore,
2. are too many and explicitly modelling them is out of question or
3. are simply unknown.

Examples for situations where explicit quantification of the context can be difficult:

* **Cell culture media optimization for different cell types:**<br />
  \\\\
  Cell types differ among many possible descriptors, and it is not known a priori
  which ones are relevant to a newly started campaign.
* **Optimization in industrial black-box contexts:**<br />
  \\\\
  When materials (such as cell lines or complex substances) stem from customers,
  they can come uncharacterized.
* **Transfer of a complicated process to another location:**<br />
  \\\\
  The transferred machinery will likely require a new calibration/optimization, which
  could benefit from the other location’s data. However, is not necessarily clear what
  parameters differentiate the location context.

**Transfer learning** in BayBE offers a solution for situations such as the latter,
because it abstracts each context change between campaigns into a single dimension
encoded by a [`TaskParameter`]().
Over the course of an ongoing campaign, the relationship between current campaign data
and data from previous campaigns can then be *learned* instead of requiring hard-coded
context parameters, effectively enabling you to utilize your previous data through
an additional machine learning model component.
In many situations, this can unlock data treasures coming from similar but not identical
campaigns accumulated over many years.