import qrcode
import time
import hashlib
import os

# 1. Configuration
SECRET_KEY = "COVENANT_UNI_MATH_101" # This stays on the lecturer's device
TIME_STEP = 10 # The QR code changes every 10 seconds

def generate_token():
    # Calculate the current time window
    # Math: floor(current_time / 10)
    window = int(time.time() // TIME_STEP)
    
    # Create a unique hash based on the secret and the time window
    raw_data = f"{SECRET_KEY}{window}"
    hash_digest = hashlib.sha256(raw_data.encode()).hexdigest()
    
    # Return a 6-character short code from the hash for the QR
    return hash_digest[:6].upper()

print("--- CU Dynamic Attendance System Prototype ---")
print(f"Refreshing every {TIME_STEP} seconds. Press Ctrl+C to quit.")

try:
    while True:
        token = generate_token()
        
        # 2. Generate the QR Code
        # In a real app, this would update a web page or a projector screen
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"STAMP:{token}")
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("attendance_qr.png")
        
        print(f"[{time.strftime('%H:%M:%S')}] Current Token: {token} (Saved to attendance_qr.png)")
        
        # Wait for the next window
        time.sleep(TIME_STEP)

except KeyboardInterrupt:
    print("\nSystem stopped.")