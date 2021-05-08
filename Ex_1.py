# -*- coding: utf-8 -*-
import speech_recognition as sr
import wave, pyaudio

#設定參數值
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5

#錄音程式
def recordWave():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print('Recording...')
    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)
    print('Record Done')
    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf = wave.open('record.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()

def main():
    print('wait command...')
    command = input()
    if command == 's':
        recordWave()
        r = sr.Recognizer()
        with sr.AudioFile("record.wav") as source:
            sound = r.listen(source)
        try:
            #語音辨識轉成文字
            print('Recognizing')
            target = r.recognize_google(sound, language="zh-TW")
            print(target)
            return target
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))

if __name__ == '__main__':
    main()


