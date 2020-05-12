import numpy as np
import soundfile as sf
import sounddevice as sd

def record(fs = 44100):
    '''Interactive way of recording audio. Please call this function 
    if you want the user to input an amount of 
    time in seconds and record that exact amount.'''
    
    timeValue = int(input('Please enter the amount of time (in seconds) to record: '))
    start = input('Press Enter to start recording.')

    print('Recording...')
    
    audio = sd.rec(frames = timeValue * fs, samplerate = fs, channels = 1)
    sd.wait()
    
    print('Recorded succesfully.')
    
    file_name = str(input('Write a name for the file: '))
    sf.write(str(file_name + '.wav'), audio, fs)
    
    print('Your file was saved as ' + file_name + '.wav')
    
    return audio

num = 1

while num != -1:
    print('s')
    num = num -1