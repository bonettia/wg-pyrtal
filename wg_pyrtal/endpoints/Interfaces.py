from typing import Literal
class Interfaces:
    def __init__(self, client):
        self.client = client

    def all(self) ->  list[dict]:
        '''
        Retrieve all interfaces.
        Returns:
            List of dictionary notation of all interfaces.
        '''
        response = self.client.request("GET", "interface/all")
        return response

    def by_id(self, identifier: str) -> dict:
        '''
        Retrieve an interface by its identifier.
        Args:
            identifier (str): The unique identifier of the interface.
        Returns:
            Dictionary notation of the interface.
        '''
        response = self.client.request("GET", f"interface/by-id/{self.client.urlparse(identifier)}")
        return response

    def update(self, id: str, mode: Literal["client", "server", "any"], privatekey: str, publickey: str, **extra: dict) -> dict:
        '''
        This endpoint updates an existing interface with the provided data. All required fields must be filled (e.g. name, private key, public key, ...).
        Args:
            id (str): The unique identifier for the interface.
            mode (InterfaceModes): The mode of the interface.
            privatekey (str): The private key for the interface. If not provided, a new keypair will be generated.
            publickey (str): The public key for the interface. If not provided, a new keypair will be generated.
            **extra: Additional parameters to include in the interface creation.
        Returns:
            Dictionary notation of the updated interface.
        '''
        if mode not in ["client", "server", "any"]:
            raise ValueError("mode must be one of 'client', 'server', or 'any'")
        data = {
            "Identifier": id,
            "Mode": mode,
            "PrivateKey": privatekey,
            "PublicKey": publickey,
            **extra
        }
        response = self.client.request("PUT", f"interface/by-id/{self.client.urlparse(id)}", data=data)
        return response

    def delete(self, identifier: str) -> bool:
        '''
        Delete an existing interface.
        Args:
            identifier (str): The unique identifier of the interface.
        Returns:
            Boolean indicating whether the deletion was successful.
        '''
        response = self.client.request("DELETE", f"interface/by-id/{self.client.urlparse(identifier)}")
        return response

    def create(self, id: str, mode: Literal["client", "server", "any"], privatekey: str=None, publickey: str=None, **extra: dict) -> dict:
        '''
        This endpoint creates a new interface with the provided data. All required fields must be filled (e.g. name, private key, public key, ...).
        Args:
            id (str): The unique identifier for the new interface.
            mode (InterfaceModes): The mode of the interface.
            privatekey (str, optional): The private key for the interface. If not provided, a new keypair will be generated.
            publickey (str, optional): The public key for the interface. If not provided, a new keypair will be generated.
            **extra: Additional parameters to include in the interface creation.
        Returns:
            Dictionary notation of the created interface.
        '''
        if mode not in ["client", "server", "any"]:
            raise ValueError("mode must be one of 'client', 'server', or 'any'")
        #if keys are not provided, generate new keypair
        if privatekey is None and publickey is None:
            prepareinterface = self.prepare()
            privatekey = prepareinterface["PrivateKey"]
            publickey = prepareinterface["PublicKey"]
        data = {
            "Identifier": id,
            "Mode": mode,
            "PrivateKey": privatekey,
            "PublicKey": publickey,
            **extra
        }
        response = self.client.request("POST", "interface/new", data=data)
        return response

    def prepare(self) -> dict:
        '''
        Prepare a new interface without creating it for key generation.
        Returns:
            Dictionary notation of the prepared interface.
        '''
        response = self.client.request("GET", "interface/prepare")
        return response