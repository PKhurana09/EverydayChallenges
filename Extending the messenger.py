from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass


class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        
    def receive(self, message):
        self.messages.append({'message': message, 'time': getCurrentTime()})
        
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []

