1. Connect bulbs to WiFi with Kasa mobile app
2. Connect PixieBoard to the same WiFi
3. Go to demo root where manage.py is located
4. Copy you IP address with command ip addr
5. Edit lightController/setting.py ALLOWED_HOST["<IP>"]
6. Execute sudo python manage.py runserver 0.0.0.0:8000
7. In your browser put the IP address with port
8. Demo has started :)

