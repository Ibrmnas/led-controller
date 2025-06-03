# Default values
led = None
ledPin = 18
isRpiPresent: bool = False  # Assume false by default

try:
    import RPi.GPIO as GPIO
    from gpiozero import LED

    isRpiPresent = True
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    led = LED(ledPin)  # Initialize the LED instance
except Exception as e:
    print(f"[Non-RPi] GPIO not available: {e}")

def setDummyLedState(isLedOn: bool):
    print(f"[Dummy] Setting LED state as {isLedOn}")

# Set default LED control function to dummy
setLedState = setDummyLedState

if isRpiPresent:
    def setPiLedState(isLedOn: bool):
        try:
            if isLedOn:
                led.on()
            else:
                led.off()
            print(f"[Raspberry Pi] LED state set to {isLedOn}")
        except Exception as e:
            print(f"[Error] Failed to set LED state: {e}")

    setLedState = setPiLedState

def cleanup_gpio():
    global led
    if led is not None:
        print("Cleaning up GPIO...")
        led.close()
        GPIO.cleanup()
    else:
        print("[Dummy] No GPIO to clean up")
