import numpy as np

def generate_complex_tone(frequency,
                          sample_rate,
                          num_samples,
                          amplitude=1.0,
                          phase=0.0):
    n = np.arange(num_samples)
    
    x = amplitude * np.exp(1j * (2 * np.pi * frequency * n / sample_rate + phase))
    
    return x