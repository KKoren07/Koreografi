from naoqi import ALProxy

# Replace the IP address and port with your NAO's IP and port
nao_ip = "192.168.0.130"
port = 9559

tts = ALProxy("ALTextToSpeech", nao_ip, port)

tts.setLanguage("German")

print("Language changed to:", tts.getLanguage())
