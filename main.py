from Chat import Chat
# from SpeakOnline import Speak
from Listen import Listen

if __name__=="__main__":
    while 1:
        Q=input(r"Enter : ")
        QL=Q.lower()
        GetChat=Chat(QL)
        # Speak(GetChat[0])
        print(GetChat[0])