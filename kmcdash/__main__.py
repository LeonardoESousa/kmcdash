import os
import subprocess

def main():
    path = os.path.join(os.path.dirname(__file__),"Dashboard_KMC.ipynb")
    path = r"{} ".format(path)
    working_dir = os.getcwd()+'/'
    with open(os.path.dirname(__file__)+'/pathfile.txt','w') as f:
        f.write(working_dir+'\n')
    try:
        option = r'--Voila.tornado_settings={}'.format('''{'websocket_max_message_size': 209715200}''')
        subprocess.check_output(['voila',path,option])
    except subprocess.CalledProcessError:
        option =  " --Voila.tornado_settings \"'websocket_max_message_size'=209715200\""
        command = "voila "+path+option
        subprocess.run(command, shell=True)
