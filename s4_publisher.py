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

print("Mulai mengirim data suhu dari semua ruangan...")
try:
    while True:
        ruangan = {
            "smartroom/livingroom/temperature": round(random.uniform(20.0, 35.0), 2),
            "smartroom/bedroom/temperature": round(random.uniform(18.0, 30.0), 2),
            "smartroom/kitchen/temperature": round(random.uniform(25.0, 40.0), 2),
        }

        for topic, suhu in ruangan.items():
            client.publish(topic, f"Suhu: {suhu} °C", qos=1)
            print(f"[TERKIRIM] {topic} | Suhu: {suhu} °C")

        print("---")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
finally:
    client.loop_stop()
    client.disconnect()