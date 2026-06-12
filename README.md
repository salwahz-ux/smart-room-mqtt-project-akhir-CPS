# Smart Room Monitoring - MQTT System

Sistem komunikasi berbasis MQTT untuk memantau kondisi ruangan secara real-time menggunakan Python dan Mosquitto Broker.

## Teknologi yang Digunakan
- Python 3.10+
- Library paho-mqtt
- Mosquitto Broker
- Protokol MQTT v3.1.1

## Struktur Topik
smartroom/livingroom/temperature
smartroom/livingroom/humidity
smartroom/livingroom/light
smartroom/bedroom/temperature
smartroom/bedroom/humidity
smartroom/bedroom/motion
smartroom/kitchen/temperature
smartroom/kitchen/gas

## Cara Menjalankan

### Persiapan
1. Install Python 3.10+
2. Install Mosquitto Broker dari https://mosquitto.org/download/
3. Install library paho-mqtt:
   pip install paho-mqtt

### Menjalankan Broker
Buka CMD, ketik:
   mosquitto -v
Biarkan CMD ini tetap terbuka.

### Skenario 1 - Komunikasi Dasar (QoS 0)
CMD 1:
   python s1_subscriber.py
CMD 2:
   python s1_publisher.py

### Skenario 2 - Variasi QoS (0, 1, 2)
CMD 1:
   python s2_subscriber.py
CMD 2:
   python s2_publisher.py

### Skenario 3 - Beberapa Topik
CMD 1:
   python s3_subscriber.py
CMD 2:
   python s3_publisher.py

### Skenario 4 - Wildcard +
CMD 1:
   python s4_subscriber.py
CMD 2:
   python s4_publisher.py

### Skenario 5 - Wildcard #
CMD 1:
   python s5_subscriber.py
CMD 2:
   python s5_publisher.py

## Deskripsi Skenario

| Skenario | Topik | QoS | Keterangan |
|----------|-------|-----|------------|
| 1 | smartroom/livingroom/temperature | 0 | Komunikasi dasar publisher-subscriber |
| 2 | smartroom/bedroom/humidity | 0,1,2 | Pengujian variasi QoS |
| 3 | smartroom/livingroom/* | 1 | Beberapa topik sekaligus |
| 4 | smartroom/+/temperature | 1 | Wildcard satu level |
| 5 | smartroom/# | 1 | Wildcard semua level |
