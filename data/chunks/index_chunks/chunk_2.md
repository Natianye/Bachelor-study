# BayBE — A Bayesian Back End for Design of Experiments

The **Bay**esian **B**ack **E**nd (**BayBE**) is a general-purpose toolbox for Bayesian Design
of Experiments, focusing on additions that enable real-world experimental campaigns.

## 🔋 Batteries Included

Besides its core functionality to perform a typical recommend-measure loop, BayBE
offers a range of ✨**built‑in features**✨ crucial for real-world use cases.
The following provides a non-comprehensive overview:

- 🛠️ Custom parameter encodings: Improve your campaign with domain knowledge
- 🧪 Built-in chemical encodings: Improve your campaign with chemical knowledge
- 🎯 Numerical and binary targets with min, max and match objectives
- ⚖️  Multi-target support via Pareto optimization and desirability scalarization
- 🔍 Insights: Easily analyze feature importance and model behavior
- 🎭 Hybrid (mixed continuous and discrete) spaces
- 🚀 Transfer learning: Mix data from multiple campaigns and accelerate optimization
- 🎰 Bandit models: Efficiently find the best among many options in noisy environments (e.g. A/B Testing)
- 🔢 Cardinality constraints: Control the number of active factors in your design
- 🌎 Distributed workflows: Run campaigns asynchronously with pending experiments and partial measurements
- 🎓 Active learning: Perform smart data acquisition campaigns
- ⚙️ Custom surrogate models: Enhance your predictions through mechanistic understanding
- 📈 Comprehensive backtest, simulation and imputation utilities: Benchmark and find your best settings
- 📝 Fully typed and hypothesis-tested: Robust code base
- 🔄 All objects are fully (de-)serializable: Useful for storing results in databases or use in wrappers like APIs