import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from pydub import AudioSegment

# Load the audio file
audio_path = './supido drums.m4a'
audio = AudioSegment.from_file(audio_path)

# Convert audio to numpy array
samples = np.array(audio.get_array_of_samples())
samples = samples.astype(np.float32)

# Apply a moving average filter to smooth the signal (optional)
window_size = 50  # Adjust the window size for more or less smoothing
smoothed_signal = np.convolve(samples, np.ones(window_size) / window_size, mode='same')

# Detect peaks
peaks, _ = find_peaks(smoothed_signal, height=None, distance=sr//2)  # Adjust the distance parameter as needed

# Convert peak indices to time
peak_times = peaks / sr

# Plot the smoothed audio signal with peak markers
plt.figure(figsize=(14, 6))
plt.plot(np.linspace(0, len(smoothed_signal) / sr, num=len(smoothed_signal)), smoothed_signal, label='Smoothed Audio Signal')
plt.plot(peak_times, smoothed_signal[peaks], "x", label='Detected Peaks')
plt.title('Smoothed Audio Signal with Peak Markers')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Print the detected peak times
print("Detected peaks (in seconds):")
print(peak_times)
