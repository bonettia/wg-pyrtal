import base64, requests
from .endpoints.Interfaces import Interfaces
class WGPortal:
    interfaces: "Interfaces"
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

    def request(self, method, endpoint, data=None):
        url = f"http://{self.server_ip}:{self.server_port}/api/v1/{endpoint}"
        if method == "GET":
            response = requests.get(url, headers=self.headers, verify=False, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, headers=self.headers, verify=False, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, headers=self.headers, verify=False, timeout=10)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=self.headers, verify=False, timeout=10)
        else:
            raise ValueError("Unsupported HTTP method")
        return response