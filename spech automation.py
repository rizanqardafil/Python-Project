from gtts import gTTS
from playsound import playsound
text = "Hello, Good Morning, How Are You To Day"
i = gTTS(text, lang='id', slow=False)
i.save("code.mp3")
playsound("code.mp3")