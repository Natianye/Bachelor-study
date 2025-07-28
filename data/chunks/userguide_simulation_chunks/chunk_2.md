# Simulation
BayBE offers multiple functionalities to “simulate” experimental campaigns with a given lookup mechanism. This user guide briefly introduces how to use the methods available in our [simulation subpackage]().

For a wide variety of applications of this functionality, we refer to the corresponding [examples]().

## Terminology: What do we mean by “Simulation”?

The term “simulation” can have two slightly different interpretations, depending on the applied context.

1. It can refer to “backtesting” a particular experimental campaign on a fixed finite dataset.
   Thus, “simulation” means investigating what experimental trajectory we would have observed if we had used different setups or recommenders and restricted the possible parameter configurations to those contained in the dataset.
2. It can refer to the simulation of an *actual* DOE loop, i.e., recommending experiments and retrieving the corresponding measurements, where the loop closure is realized in the form of a callable (black-box) function that can be queried during the optimization to provide target values. Such a callable could for instance be a simple analytical function or a numerical solver of a set of differential equations that describe a physical system.