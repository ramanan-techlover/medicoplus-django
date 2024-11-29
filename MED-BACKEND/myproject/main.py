import serial
import webbrowser
import time

# Set your serial port (adjust as needed)
ser = serial.Serial('COM7', 115200, timeout=1)

last_key_value = None  # Variable to store the last key value detected

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if "Key Value:" in line:
            # Extract key from the serial line
            key_value = line.split(":")[1].strip()
            
            # Check if the key value has changed
            if key_value != last_key_value:
                last_key_value = key_value  # Update last key value
                url = f"http://localhost:8000/myapp/nfc-scan/{key_value}/"  # Update with your Django server URL
                print(f"Navigating to {url}")
                webbrowser.open(url)  # Open the URL in the default browser
                
                time.sleep(2)  # Delay to avoid rapid multiple openings (adjust as needed)
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Error: {e}")
