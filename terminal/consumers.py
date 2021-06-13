import json
import os
import pty
import channels 
from channels.generic.websocket import WebsocketConsumer
import subprocess
import threading
import time
CHILD_PID = None
FD = None

class EndTerminal(Exception):

    def __str__(self):
        return 'Terminal has been exited'


class TerminalConsumer(WebsocketConsumer):
    _thread = None

    def connect(self):
        global CHILD_PID
        global FD
        print('Accepted')
        if CHILD_PID: 
            print('running!')
            return
        self._thread = threading.Thread(target=self.spawn_shell, daemon=True)
        self._thread.start()
    
    def spawn_shell(self):
        pty.spawn(os.environ['SHELL'], self.read_forward_pty_output)
        return True

    def disconnect(self, close_code):
        print('Disconnecting')
        pass 
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        try:
            os.write(FD, bytes(message, encoding="utf-8"))
        except OSError:
            raise EndTerminal()
    
    def read_forward_pty_output(self, fd):
        global FD
        FD=fd
        self.accept()

        max_read_bytes = 1024 * 20
        while True:
            time.sleep(.1)
            output = os.read(FD, max_read_bytes).decode()
            self.send(text_data=json.dumps({'message':output}))