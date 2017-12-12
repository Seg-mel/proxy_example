## Proxy example
Simple proxy server for VK

#### Installing
- Install Python >=3.6
- Clone the project `git clone https://github.com/Seg-mel/proxy_example.git`
- Move to the project directory `cd proxy_example`
- Install pip requirements `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (if Python 3 is not the main version in your system)

#### Start the project
- `python ./server.py` or `python3 ./server.py` (if Python 3 is not the main version in your system)

#### Simple test
- First example from official docs `curl -v 'http://127.0.0.1:8080/method/users.get?user_ids=210700286&fields=bdate&v=5.69'`
- Second example `curl -v 'http://127.0.0.1:8080/method/friends.get?user_id=6&fields=nickname,city,status'`
