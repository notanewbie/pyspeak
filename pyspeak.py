import sys
import platform
import os
from parse import parseChars
from parse import harshChars
def Speak(words):
    #print "Speaking"
    if "win32" in sys.platform and '10' not in platform.release():
        os.system('mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""' + parseChars(words) + '"")(window.close)")')
    elif "win64" in sys.platform and '10' in platform.release():
        os.system('PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' + "'" + harshChars(parseChars(words)) + "'" + ');"');
    elif "win32" in sys.platform and '10' in platform.release():
        os.system('PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' + "'" + harshChars(parseChars(words)) + "'" + ');"');
    if "darwin" in sys.platform:
        os.system("say " + words)
