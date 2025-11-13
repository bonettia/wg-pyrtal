class Peers:
    def __init__(self, client):
        self.client = client
    
    def by_interface(self, interface_id: str) -> list[dict]:
        '''
        Retrieve all peers associated with a specific interface.
        Args:
            interface_id (str): The unique identifier of the interface.
        Returns:
            List of Dictionary notation of all peers associated with the interface.
        '''
        response = self.client.request("GET", f"peer/by-interface/{self.client.urlparse(interface_id)}")
        return response
    
    def by_id(self, identifier: str) -> dict:
        '''
        Retrieve a peer by its identifier.
        Args:
            identifier (str): The unique identifier of the peer (its public key).
        Returns:
            Dictionary notation of the peer.
        '''
        response = self.client.request("GET", f"peer/by-id/{self.client.urlparse(identifier)}")
        return response
    
    def by_user(self, user_id: str) -> list[dict]:
        '''
        Retrieve all peers associated with a specific user.
        Args:
            user_id (str): The unique identifier of the user.
        Returns:
            List of Dictionary notation of all peers associated with the user.
        '''
        response = self.client.request("GET", f"peer/by-user/{self.client.urlparse(user_id)}")
        return response
    
    def prepare(self, interface_id: str) -> dict:
        '''
        Prepare a new peer for a specific interface without creating it.
        Args:
            interface_id (str): The unique identifier of the interface.
        Returns:
            Dictionary notation of the prepared peer.
        '''
        response = self.client.request("GET", f"peer/prepare/{self.client.urlparse(interface_id)}")
        return response

    def create(self, interface_id: str, peerPrivKey: str=None, peerPubKey: str=None,**extra: dict) -> dict:
        '''
        Create a new peer.
        Args:
            peerPrivKey (str): The private key of the peer. If not provided, a new keypair will be generated.
            peerPubKey (str, optional): The public key of the peer. If not provided, a new keypair will be generated.
            interface_id (str): The unique identifier of the interface to which the peer will be added.
            **extra (dict): Additional parameters to include in the peer creation.
        Returns:
            Dictionary notation of the created peer.            
        '''
        if peerPrivKey is None and peerPubKey is None:
            preparepeer = self.prepare(interface_id)
            peerPrivKey = preparepeer["PrivateKey"]
            peerPubKey = preparepeer["PublicKey"]
        data={
            "PrivateKey": peerPrivKey,
            "InterfaceIdentifier": interface_id,
            "PublicKey": peerPubKey,
            "Identifier": peerPubKey,
            **extra
        }
        response = self.client.request("POST", "peer/new", data=data)
        return response
    
    def update(self, peerPrivKey: str, pubkey: str, interface_id: str, **extra: dict) -> dict:
        '''
        Update a peer.
        Args:
            peerPrivKey (str): The private key of the peer.
            interface_id (str): The unique identifier of the interface to which the peer will be added.
            pubkey (str, optional): The public key of the peer.
            **extra (dict): Additional parameters to include in the peer update.
        Returns:
            Dictionary notation of the updated peer.
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
        Returns:
            Boolean indicating the success of the deletion.
        '''
        response = self.client.request("DELETE", f"peer/by-id/{self.client.urlparse(identifier)}")
        return response
        