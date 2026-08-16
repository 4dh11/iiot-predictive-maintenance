from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "UP",
        "service": "IIoT Predictive Maintenance Gateway"
    })

@app.route('/api/v1/telemetry', methods=['GET'])
def get_telemetry():
    # Simulate IIoT industrial sensor values
    vibration_g = round(random.uniform(0.5, 4.8), 2)   # Threshold > 4.0g
    temp_celsius = round(random.uniform(40.0, 95.0), 1) # Threshold > 85.0°C
    pressure_psi = round(random.uniform(90.0, 150.0), 1)
    
    # Simple predictive fault trigger
    fault_detected = vibration_g > 4.0 or temp_celsius > 85.0

    return jsonify({
        "machine_id": "PUMP_MOTOR_UNIT_01",
        "timestamp": int(time.time()),
        "telemetry": {
            "vibration_g": vibration_g,
            "temperature_c": temp_celsius,
            "pressure_psi": pressure_psi
        },
        "status": "ALERT_TRIGGERED" if fault_detected else "OPERATIONAL"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)