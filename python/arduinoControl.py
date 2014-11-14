import serial
import time

class ArduinoControl(object):
    def __init__(self):
        self._ser = serial.Serial('/dev/ttyACM0',9600)
        self._running = False

    def switchOnOff(self):
        self._running = not self._running
        self._ser.write('p')
        time.sleep(6)
        self._ser.write('u')

    @property
    def running(self):
        return self._running

    def switchButton(self):
        if self.running or True:
            self._ser.write('p')
            time.sleep(0.3)
            self._ser.write('u')
