# import numpy as np

# from input.simulator import generate_complex_tone


# frequency = 100_000
# sample_rate = 1_000_000
# num_samples = 10_000
# amplitude = 1.0
# phase = 0.0


# iq = generate_complex_tone(
#     frequency,
#     sample_rate,
#     num_samples,
#     amplitude,
#     phase
# )


# print("Number of samples:", len(iq))
# print("Data type:", iq.dtype)

# print("\nFirst 5 IQ samples:")
# print(iq[:5])

# print("\nMagnitude of first 5 samples:")
# print(np.abs(iq[:5]))

# print("\nPhase of first 5 samples:")
# print(np.angle(iq[:5]))

import numpy as np
import matplotlib.pyplot as plt

from input.simulator import generate_complex_tone


# Signal parameters
frequency = 100_000
sample_rate = 1_000_000
num_samples = 1000
amplitude = 1.0
phase = 0.0


# Generate IQ signal
iq = generate_complex_tone(
    frequency,
    sample_rate,
    num_samples,
    amplitude,
    phase
)


# Separate I and Q
I = np.real(iq)
Q = np.imag(iq)


# # Time axis
# t = np.arange(num_samples) / sample_rate


# # Plot I and Q
# plt.figure(figsize=(10, 5))

# plt.plot(t[:100] * 1e6, I[:100], label="I")
# plt.plot(t[:100] * 1e6, Q[:100], label="Q")

# plt.xlabel("Time (µs)")
# plt.ylabel("Amplitude")
# plt.title("Synthetic IQ Signal")
# plt.legend()
# plt.grid()
# plt.savefig("iq_signal.png", dpi=150, bbox_inches="tight")
# print("Plot saved as iq_signal.png")

# plt.figure(figsize=(6, 6))

# plt.plot(I, Q, "o")

# plt.xlabel("I")
# plt.ylabel("Q")
# plt.title("IQ Constellation")
# plt.grid()
# plt.axis("equal")

# plt.savefig("iq_constellation.png", dpi=150, bbox_inches="tight")
# print("Constellation saved as iq_constellation.png")

# FFT
N = len(iq)

spectrum = np.fft.fft(iq)
frequencies = np.fft.fftfreq(N, 1 / sample_rate)

# Shift zero frequency to the center
spectrum = np.fft.fftshift(spectrum)
frequencies = np.fft.fftshift(frequencies)

# Magnitude
magnitude = np.abs(spectrum)

plt.figure(figsize=(10, 5))

plt.plot(frequencies / 1000, magnitude)

plt.xlabel("Frequency (kHz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum")
plt.grid()

plt.savefig("fft_spectrum.png", dpi=150, bbox_inches="tight")

print("FFT spectrum saved as fft_spectrum.png")