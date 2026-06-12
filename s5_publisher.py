import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke broker!")
    else:
        print(f"Gagal terhubung, kode: {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

print("Mulai mengirim semua data sensor dari semua ruangan...")
try:
    while True:
        data = {
            "smartroom/livingroom/temperature": f"Suhu: {round(random.uniform(20.0, 35.0), 2)} °C",
            "smartroom/livingroom/humidity": f"Kelembapan: {round(random.uniform(40.0, 90.0), 2)}%",
            "smartroom/livingroom/light": f"Cahaya: {round(random.uniform(100.0, 1000.0), 2)} lux",
            "smartroom/bedroom/temperature": f"Suhu: {round(random.uniform(18.0, 30.0), 2)} °C",
            "smartroom/bedroom/humidity": f"Kelembapan: {round(random.uniform(40.0, 90.0), 2)}%",
            "smartroom/bedroom/motion": random.choice(["Motion: Detected", "Motion: Not Detected"]),
            "smartroom/kitchen/temperature": f"Suhu: {round(random.uniform(25.0, 40.0), 2)} °C",
            "smartroom/kitchen/gas": f"Gas: {round(random.uniform(0.0, 100.0), 2)} ppm",
        }

        for topic, pesan in data.items():
            client.publish(topic, pesan, qos=1)
            print(f"[TERKIRIM] {topic} | {pesan}")

        print("---")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
finally:
    client.loop_stop()
    client.disconnect()