# Simulation
## The Lookup Mechanism
### Using `None`

When testing code, it can sometimes be helpful to have an “arbitrary” lookup mechanism available without having to craft a custom one.
An example of when this is useful is when evaluating the actual lookup is too expensive and results in too long turnaround times (for instance, when the lookup is implemented by running complex code such as a computer simulation).
In these situations, using `None` as lookup can save valuable development time, which invokes the `add_fake_measurements()` utility behind the scenes to generate random target values for any given domain.