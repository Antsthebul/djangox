import json
import os
import pty 
from channels.generic.websocket import WebsocketConsumer
import subprocess
import threading
import time
CHILD_PID = None
FD = None



class TerminalConsumer(WebsocketConsumer):

    def connect(self):
        global CHILD_PID
        global FD
        print('accepted')
        if CHILD_PID: 
            print('running!')
            return
        # (CHILD_PID, FD) = pty.fork()
        
        threading.Thread(target=self.spawn_shell, daemon=True).start()
        print('Child: {} FD:{}'.format(CHILD_PID, FD))
        if CHILD_PID == 0:
            # child process
            return
    
    def spawn_shell(self):
        pid = pty.spawn(os.environ['SHELL'], self.read_forward_pty_output)
        print('Pid', pid)

    def disconnect(self, close_code):
        pass 
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        return os.write(FD, bytes(message, encoding="utf-8"))
    
    def read_forward_pty_output(self, fd):
        global FD
        FD=fd
        self.accept()

        max_read_bytes = 1024 * 20
        while True:
            time.sleep(.1)
            output = os.read(FD, max_read_bytes).decode()
            self.send(text_data=json.dumps({'message':output}))