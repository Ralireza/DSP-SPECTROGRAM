# DSP-SPECTROGRAM
create spectrogram of signal from scratch
![example](https://raw.githubusercontent.com/4lrz/dsp-spectrogram/master/Figure_1.png)

## Description
specto class divided into 3 origin function:
### 1- readfile(filename='sound.wav')
read wave sound and get one channel of sound 

return =>  signal of that channel and sampeling frequency

### 2- calculate_spectrogram(signal_data, nfft, count_in_frame, window, overlap_percent)
It splited signal into overlapping sections and applies the window specified by the window parameter to each section

after that it compute discrete time fourier transform for each section and return final_spectrogram.

### 3- show_spetrogram(spectrogram_matrix, nfft)
show imagee of spectrogram by matplotlib.pyplot

#### feel free to play with params :)
