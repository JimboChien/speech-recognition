# -*- coding: utf-8 -*-
from gtts import gTTS
from pygame import mixer
import sys

#語音輸出
def wordToSound(text):
    #====================================#
    #   使用 gTTS 將文字轉成語音的部份   #
    #====================================#
    file_name ='test2.mp3'
    tts = gTTS(text, lang='zh-tw')
    tts.save(file_name)
    #====================================#
    #     使用 pygame 播放語音的部份     #
    #====================================#
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    mixer.music.stop()
    mixer.quit()

def main():
    print('input a sentence to TTS!')
    text = input()
    wordToSound(text)

if __name__ == '__main__':
    main()

