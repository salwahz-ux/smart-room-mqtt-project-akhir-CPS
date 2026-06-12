import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/bedroom/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke broker!")
    else:
        print(f"Gagal terhubung, kode: {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

print("Mulai mengirim data kelembapan kamar tidur...")
try:
    for qos in [0, 1, 2]:
        print(f"\n--- Mengirim dengan QoS {qos} ---")
        for i in range(3):
            kelembapan = round(random.uniform(40.0, 90.0), 2)
            pesan = f"Kelembapan: {kelembapan}% | QoS: {qos}"
            client.publish(TOPIC, pesan, qos=qos)
            print(f"[TERKIRIM] {pesan}")
            time.sleep(2)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
finally:
    client.loop_stop()
    client.disconnect()