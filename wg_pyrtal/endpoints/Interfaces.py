from enum import Enum
from typing import Literal
from ..utils import urlparse

class InterfaceModes(str,Enum):
    CLIENT = "client"
    SERVER = "server"
    ANY = "any"


class Interfaces:
    def __init__(self, client):
        '''Initialize the Interfaces endpoint with a WGPortal client.'''
        self.client = client
    
    def all(self):
        '''Retrieve all interfaces.'''
        response = self.client.request("GET", "interface/all")
        return response

    def by_id(self, identifier: str):
        '''
        Retrieve an interface by its identifier.
        Args:
            identifier (str): The unique identifier of the interface.
        '''
        response = self.client.request("GET", f"interface/by-id/{urlparse(identifier)}")
        return response
    
    def update(self, identifier: str, data: dict):
        '''
        Update an existing interface.
        Args:
            identifier (str): The unique identifier of the interface.
            data (dict): The updated data for the interface.
        '''
        response = self.client.request("PUT", f"interface/by-id/{urlparse(identifier)}", data=data)
        return response

    def delete(self, identifier: str):
        '''
        Delete an existing interface.
        Args:
            identifier (str): The unique identifier of the interface.
        '''
        response = self.client.request("DELETE", f"interface/by-id/{urlparse(identifier)}")
        return response

    def create(self, id: str, mode: InterfaceModes, privatekey=None, publickey=None, **extra):
        '''
        Create a new interface.
        Args:
            id (str): The unique identifier for the new interface.
            mode (InterfaceModes): The mode of the interface.
            privatekey (str, optional): The private key for the interface. If not provided, a new keypair will be generated.
            publickey (str, optional): The public key for the interface. If not provided, a new keypair will be generated.
            **extra: Additional parameters to include in the interface creation.
        Returns:
            Json notation of the created interface.
        '''
        #if keys are not provided, generate new keypair
        if privatekey is None and publickey is None:
            preparepeer = self.prepare().json()
            privatekey = preparepeer["PrivateKey"]
            publickey = preparepeer["PublicKey"]
        data = {
            "id": id,
            "mode": mode,
            "privatekey": privatekey,
            "publickey": publickey,
            **extra
        }
        response = self.client.request("POST", "interface/new", data=data)
        return response
    
    def prepare(self):
        '''
        Prepare a new interface without creating it for key generation.
        Returns:
            Json notation of the prepared interface.
        '''
        response = self.client.request("GET", "interface/prepare")
        return response