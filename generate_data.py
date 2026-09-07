"""
generate_data.py
----------------
Generates a synthetic Cleveland Heart Disease-style dataset.
Used as a fallback when the UCI URL is not reachable.
"""

import numpy as np
import pandas as pd


def generate_heart_dataset(n: int = 1000, random_state: int = 42) -> pd.DataFrame:
    """
    Generate a synthetic dataset matching the Cleveland Heart Disease schema.

    Features (same as UCI Cleveland dataset):
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal, target
    """
    rng = np.random.default_rng(random_state)

    age      = rng.integers(29, 78, n)
    sex      = rng.integers(0, 2, n)
    cp       = rng.integers(0, 4, n)
    trestbps = rng.integers(90, 200, n)
    chol     = rng.integers(120, 570, n)
    fbs      = (rng.random(n) < 0.15).astype(int)
    restecg  = rng.integers(0, 3, n)
    thalach  = rng.integers(71, 202, n)
    exang    = (rng.random(n) < 0.33).astype(int)
    oldpeak  = np.round(rng.uniform(0, 6.2, n), 1)
    slope    = rng.integers(0, 3, n)
    ca       = rng.integers(0, 4, n)
    thal     = rng.integers(1, 4, n)

    # Synthetic target: higher risk with older age, male sex, high cp, low thalach
    log_odds = (
        -4.0
        + 0.04  * (age - 55)
        + 0.5   * sex
        + 0.6   * cp
        - 0.03  * (thalach - 150)
        + 0.5   * exang
        + 0.4   * oldpeak
        + 0.4   * ca
    )
    prob   = 1 / (1 + np.exp(-log_odds))
    target = (rng.random(n) < prob).astype(int)

    df = pd.DataFrame({
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,
        'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach,
        'exang': exang, 'oldpeak': oldpeak, 'slope': slope, 'ca': ca,
        'thal': thal, 'target': target
    })
    return df


if __name__ == '__main__':
    df = generate_heart_dataset(n=1000)
    df.to_csv('heart.csv', index=False)
    print(f'Saved heart.csv  shape={df.shape}  target balance={df.target.mean():.2f}')
