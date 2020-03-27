# Vest
Python class for communicating with [RedBear Duo](https://github.com/redbear/Duo) via a serial port. It can instruct the device to set a given pin to a certain vibration intensity or globally set a vibration frequency.

## Prequisites
This requires the following package to be installed:
- [PyCmdMessenger](https://github.com/harmsm/PyCmdMessenger) via pip3 or by cloning.

## Example
```python
import suitceyes

# Initialize the vest with a given port. E.g., "/dev/ttyACM0" or "COM3"
with suitceyes.Vest("COM3") as vest:
    # sets the pin at index 0 to maximum vibration intensity  
    vest.set_pin_value(0,255) 
```

## Authors
- James Gay (james.gay@hs-offenburg.de)