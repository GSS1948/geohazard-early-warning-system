import numpy as np

def compute_localized_weights(X_ambient, k_strain):
    """Computes region-specific inverse variance noise weights and dynamic strain acceleration booster."""
    variance_ambient = np.var(X_ambient, axis=0)
    W_baseline = 1.0 / (1.0 + variance_ambient + 1e-6)
    strain_channel = X_ambient[:, 2]
    strain_acceleration = np.diff(strain_channel, n=2)
    gamma_strain = k_strain / (np.sqrt(np.var(strain_acceleration)) + 1e-6)
    return W_baseline, gamma_strain

def apply_weighted_telemetry(X_raw, W_baseline, gamma_strain):
    """Applies baseline weights and dynamically scales strain acceleration during non-linear surges."""
    X_weighted = X_raw * W_baseline
    if X_raw.shape[1] > 2:
        strain_channel = X_raw[:, 2]
        accel = np.pad(np.diff(strain_channel, n=2), (1, 1), mode='edge')
        W_strain_dynamic = 1.0 + gamma_strain * np.maximum(0, accel)
        X_weighted[:, 2] = X_raw[:, 2] * W_strain_dynamic
    return X_weighted
