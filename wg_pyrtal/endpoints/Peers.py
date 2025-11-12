class Peers:
    def __init__(self, client):
        self.client = client
    
    def by_interface(self, interface_id: str) -> dict:
        '''
        Retrieve all peers associated with a specific interface.
        Args:
            interface_id (str): The unique identifier of the interface.
        '''
        response = self.client.request("GET", f"peer/by-interface/{self.client.urlparse(interface_id)}")
        return response
    
    def by_id(self, identifier: str) -> dict:
        '''
        Retrieve a peer by its identifier.
        Args:
            identifier (str): The unique identifier of the peer (its public key).
        '''
        response = self.client.request("GET", f"peer/by-id/{self.client.urlparse(identifier)}")
        return response
    
    def by_user(self, user_id: str) -> dict:
        '''
        Retrieve all peers associated with a specific user.
        Args:
            user_id (str): The unique identifier of the user.
        '''
        response = self.client.request("GET", f"peer/by-user/{self.client.urlparse(user_id)}")
        return response
    
    def prepare(self, interface_id: str) -> dict:
        '''
        Prepare a new peer for a specific interface without creating it.
        Args:
            interface_id (str): The unique identifier of the interface.
        '''
        response = self.client.request("POST", f"peer/prepare/{self.client.urlparse(interface_id)}")
        return response

    def create(self, peerPrivKey: str, pubkey: str, interface_id: str, **extra: dict) -> dict:
        '''
        Create a new peer.
        Args:
            peerPrivKey (str): The private key of the peer.
            interface_id (str): The unique identifier of the interface to which the peer will be added.
            pubkey (str, optional): The public key of the peer.
        '''
        data={
            "PrivateKey": peerPrivKey,
            "InterfaceIdentifier": interface_id,
            "PublicKey": pubkey,
            "Identifier": pubkey,
            **extra
        }
        response = self.client.request("POST", "peer/new", data=data)
        return response
    
    def update(self, peerPrivKey: str, pubkey: str, interface_id: str, **extra) -> dict:
        '''
        Update a peer.
        Args:
            peerPrivKey (str): The private key of the peer.
            interface_id (str): The unique identifier of the interface to which the peer will be added.
            pubkey (str, optional): The public key of the peer.
        '''
        data={
            "PrivateKey": peerPrivKey,
            "InterfaceIdentifier": interface_id,
            "PublicKey": pubkey,
            "Identifier": pubkey,
            **extra
        }
        response = self.client.request("PUT", f"peer/by-id/{self.client.urlparse(pubkey)}", data=data)
        return response
    
    def delete(self, identifier: str) -> bool:
        '''
        Delete a peer by its identifier.
        Args:
            identifier (str): The unique identifier of the peer (its public key).
        '''
        response = self.client.request("DELETE", f"peer/by-id/{self.client.urlparse(identifier)}")
        return response
        