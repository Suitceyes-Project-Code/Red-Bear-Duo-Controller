import PyCmdMessenger

class Vest:
    """
    Basic interface for sending commands to the vest using a
    serial port connection.
    """

    commands = [["PinSet","gg"],
                ["PinMute","g"],
                ["GloveSet","g*"],
                ["GloveMute",""],
                ["FreqSet","g"],
                ["PinGet","g"],
                ["FreqGet",""],
                ["PinState","gg"],
                ["FreqState","g"],
                ["StringMsg","s"],
                ["DebugSet","g"]]

    def __init__(self, device):
        """
        Creates a new instance of Vest.
        Inputs:        
            device:
                The path to the device, e.g.: "/dev/ttyACM0" or "COM3"
        """
        self._board = PyCmdMessenger.ArduinoBoard(device, baud_rate=115200)
        self._connection = PyCmdMessenger.CmdMessenger(self._board, Vest.commands, warnings=False)        

    def __enter__(self):
        self.set_frequency(0)
        return self

    def __exit__(self, type, value, traceback):
        # Make sure the vest is muted and that the connection is closed.
        self.mute()
        self._board.close()

    def set_pin_value(self,pin,value):
        """
        Sets a pin to a given value. This sets the vibration intensity of a given pin.
        Inputs:
            pin: 
                The pin index whose value should be set. This should be a byte value.
            value:
                A byte value (0-255) representing the vibration intensity. 0 is no vibration, 255
                is the max intensity.
        """
        self._connection.send("PinSet",pin,value)

    def mute_pin(self,pin):
        """
        Sets the vibration intensity for a given pin to 0.
        Inputs:
            pin: The pin which will be muted.
        """
        self._connection.send("PinMute", pin)

    def mute(self):
        """
        Mutes all pins on the vest.
        """
        self._connection.send("GloveMute")
    
    def set_frequency(self,frequency):
        """
        Sets the frequency of the entire vest.
        Inputs:
            frequency: The frequency in milliseconds.
        """
        self._connection.send("FreqSet", frequency)
    
    def get_pin_value(self,pin):
        """
        Gets the vibration intensity for a given pin.
        Inputs:
            pin: The pin index whose intensity should be fetched.
        """
        self._connection.send("PinGet", pin)
        return self._connection.receive()