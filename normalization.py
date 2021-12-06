import argparse
import array
import math
import numpy as np
import random
import wave
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean_file', type=str, required=True)
    parser.add_argument('--noise_file', type=str, required=True)
    parser.add_argument('--output_clean_file', type=str, default='')
    parser.add_argument('--output_noise_file', type=str, default='')
    parser.add_argument('--output_noisy_file', type=str, default='', required=True)
    parser.add_argument('--snr', type=float, default='', required=True)
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    args = get_args()
    clean_file = args.clean_file
    noise_file = args.noise_file
    snr = args.snr
    clean_wav = wave.open(clean_file, "r")
    noise_wav = wave.open(noise_file, "r")