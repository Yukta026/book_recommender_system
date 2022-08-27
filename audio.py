
from gtts import gTTS
import re
src = []
l = []
a=[1,2,3]
filename1 = int(input('Enter name of file'))
filename = 'billion.txt'
with open(filename,'r') as f:
       src = f.readlines()


src = src[:102]


test = re.sub('\[\d\]','', src[26])

clean_src = []
clean_src = [re.sub('\[\d\]','',i) for i in src]

txt = ''.join(clean_src)
tts = gTTS(txt, lang='en', tld = 'ca')
tts.save('billion.mp3')