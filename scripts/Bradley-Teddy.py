import numpy as np
import pymc as pm
import arviz as az
import pandas as pd

def main():
    # Load your CSV file (replace 'your_file.csv' with your actual file name)
    df = pd.read_csv('./data/forced_choice/Human_forced_choice_result_long.csv')

    # Count the occurrences in the 'selected_human_like' column
    counts = df['selected_human_like'].value_counts()

    # Extract the counts for 'Human' and 'GPT'
    n_human = counts.get('Human', 0)
    n_gpt = counts.get('GPT', 0)
    n_wins = n_human  # or n_gpt, depending on which you want as "wins"
    n_trials = n_human + n_gpt
    
    print(f"Human: {n_human}, GPT: {n_gpt}, Total Trials: {n_trials}")

    with pm.Model() as model:
        theta = pm.Normal("theta", mu=0, sigma=1, shape=2)
        theta_ref = pm.Deterministic("theta_ref", theta - theta[1])
        lambda_i = pm.Deterministic("lambda", pm.math.exp(theta_ref))
        p_i = pm.Deterministic("p_i", lambda_i / pm.math.sum(lambda_i))
        p_12 = pm.math.invlogit(theta_ref[0] - theta_ref[1])
        pm.Binomial("wins_0_1", n=n_trials, p=p_12, observed=n_wins)
        trace = pm.sample(1000, tune=1000, return_inferencedata=True)

    summary_theta = az.summary(trace, var_names=["theta_ref"], hdi_prob=0.95)
    summary_lambda = az.summary(trace, var_names=["lambda"], hdi_prob=0.95)
    summary_p = az.summary(trace, var_names=["p_i"], hdi_prob=0.95)

    print("Posterior summary for log-strengths (theta_ref):")
    print(summary_theta)
    print("\nPosterior summary for strengths (lambda):")
    print(summary_lambda)
    print("\nPosterior summary for normalized probabilities (p_i):")
    print(summary_p)

    p_i_samples = trace.posterior["p_i"].values
    p_m1_gt_m2 = np.mean(p_i_samples[:, :, 0] > p_i_samples[:, :, 1])
    print(f"P(p_M1 > p_M2) = {p_m1_gt_m2:.3f}")

if __name__ == "__main__":
    main()
