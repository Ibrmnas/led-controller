import RPi.GPIO as GPIO
from gpiozero import LED

# Global variables
led = None  # Initialize led as None
ledPin = 18
isRpiPresent: bool = True
GPIO.setwarnings(False)

try:
    GPIO.setmode(GPIO.BCM)
    led = LED(ledPin)  # Initialize the LED instance
except Exception as e:
    isRpiPresent = False
    print(f"Error initializing GPIO: {e}")

def setDummyLedState(isLedOn: bool):
    print(f"Setting dummy LED state as {isLedOn}...")

# Setup the setLedState function
setLedState = setDummyLedState

if isRpiPresent:
    def setPiLedState(isLedOn: bool):
        try:
            if isLedOn:
                led.on()
            else:
                led.off()
            print(f"Setting LED state as {isLedOn}")
        except Exception as e:
            print(f"Error while setting LED state: {e}")

    setLedState = setPiLedState

def cleanup_gpio():
    global led
    if led is not None:  # Ensure led is defined before trying to close it
        print("Cleaning up GPIO...")
        led.close()  # Close the LED instance to free the GPIO pin
        GPIO.cleanup()  # Clean up the GPIO pins
