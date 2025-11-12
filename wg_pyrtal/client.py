import base64, requests, json
from .utils import urlparse
from .endpoints.Interfaces import Interfaces
from .endpoints.Metrics import Metrics
from .endpoints.Peers import Peers
from .endpoints.Users import Users
from .endpoints.Provisioning import Provisioning

class WGPortal:
    def __init__(self, server_ip, server_port, username, password):
        self.server_ip = server_ip
        self.server_port = server_port
        self.username = username
        self.password = password
        cred = base64.b64encode(f"{username}:{password}".encode())
        self.headers = {
            "Authorization": f"Basic {cred.decode()}"
            }
        
        #define endpoints
        self.interfaces = Interfaces(self)
        self.metrics = Metrics(self)
        self.peers = Peers(self)
        self.users = Users(self)
        self.provisioning = Provisioning(self)

    def request(self, method, endpoint, data=None):
        url = f"http://{self.server_ip}:{self.server_port}/api/v1/{endpoint}"
        if method == "GET":
            response = requests.get(url, headers=self.headers, verify=False, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, headers=self.headers, verify=False, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, headers=self.headers, verify=False, timeout=10)
            if response.status_code == 204:
                return True
            else:
                return False
        elif method == "PUT":
            response = requests.put(url, json=data, headers=self.headers, verify=False, timeout=10)
        else:
            raise ValueError("Unsupported HTTP method")
        return json.loads(response.content)
    
    def urlparse(self, value: str) -> str:
        return urlparse(value)
