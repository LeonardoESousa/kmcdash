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
        subprocess.Popen(['voila',path,option])
    except:
        print('Attempting alternative!!')
        option =  " --Voila.tornado_settings=\"{'websocket_max_message_size': 209715200}\" " #old option format. Keep for a while
        command = "voila "+path+option
        subprocess.run(command, shell=True)        
