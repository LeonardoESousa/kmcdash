import os
import subprocess


def main():
    path = os.path.join(os.path.dirname(__file__),"Dashboard_KMC.ipynb")
    path = r"{} ".format(path)
    option = r'--Voila.tornado_settings={}'.format('''{'websocket_max_message_size': 209715200}''')
    subprocess.call(['voila',path,option])
    