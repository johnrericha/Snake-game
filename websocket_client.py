import socket
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Client configuration
HOST = '127.0.0.1'  # Server address
PORT = 12345  # Server port

class ChatApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.messages = TextInput(size_hint=(1, 0.9), readonly=True, multiline=True)
        self.input_box = TextInput(size_hint=(1, 0.1), multiline=False)
        self.send_button = Button(text="Send", size_hint=(0.2, 0.1))
        self.send_button.bind(on_press=self.send_message)

        self.layout.add_widget(self.messages)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.send_button)

        threading.Thread(target=self.receive_messages, daemon=True).start()
        return self.layout

    def send_message(self, instance):
        message = self.input_box.text
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.input_box.text = ""

    def receive_messages(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))

        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.messages.text += message + '\n'
            except:
                break

if __name__ == "__main__":
    ChatApp().run()