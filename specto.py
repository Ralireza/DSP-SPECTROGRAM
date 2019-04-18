import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

class specto:

    def calculate_spectrogram(signal_data, nfft, count_in_frame, window, overlap_percent):
        iterate_number = 0

        final_spectroggram = np.ndarray((nfft, 1))
        while iterate_number < signal_data.size - count_in_frame:
            signal_segment = signal_data[iterate_number:iterate_number + count_in_frame]
            signal_segment = signal_segment * window
            frame = np.fft.fft(signal_segment, nfft)
            frame = np.abs(frame) ** 2
            frame = np.reshape(frame, (frame.size, 1))
            iterate_number = iterate_number + overlap_percent
            final_spectroggram = np.column_stack((final_spectroggram, frame))
        return final_spectroggram


    def read_file(filename='sound.wav'):
        sampling_frequency, signal_data = wavfile.read(filename=filename)
        one_channel = signal_data[:, 0]  # the sound hava two channel
        return one_channel, sampling_frequency


    def show_spetrogram(spectrogram_matrix, nfft):
        plt.figure()
        plt.pcolormesh(np.log10(np.float32(spectrogram_matrix)))
        plt.ylim([0, nfft // 2])
        plt.xlim(1, )
        plt.show()






# main
my_magic_number = 128
overlap_percent = ((my_magic_number * 4) // 5)
signal_data, fs = specto.read_file()
specto_matrix = specto.calculate_spectrogram(signal_data=signal_data,
                                      nfft=my_magic_number,
                                      count_in_frame=my_magic_number,
                                      window=np.blackman(my_magic_number),
                                      overlap_percent=overlap_percent)


specto.show_spetrogram(specto_matrix, nfft=my_magic_number)
