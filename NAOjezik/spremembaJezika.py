from naoqi import ALProxy

nao_ip = "192.168.0.130"
port = 9559

tts = ALProxy("ALTextToSpeech", nao_ip, port)

tts.setLanguage("German")

print("Language changed to:", tts.getLanguage())
