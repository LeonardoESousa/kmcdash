import os
import subprocess


def main():
    path = os.path.join(os.path.dirname(__file__),"Dashboard_KMC.ipynb")
    path = r"{} ".format(path)
    #option =  " --Voila.tornado_settings=\"{'websocket_max_message_size': 209715200}\" " #old option format. Keep for a while
    option =  " --Voila.tornado_settings \"'websocket_max_message_size'=209715200\""
    command = "voila "+path+option
    subprocess.run(command, shell=True)
    
