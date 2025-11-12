class Provisioning:
    def __init__(self, client):
        self.client = client

    def peer_config(self, peer_public_key: str) -> dict:
        '''
        Retrieve the configuration for a specific peer.
        Args:
            peer_public_key (str): The public key of the peer.
        '''
        response = self.client.request("GET", f"provisioning/data/peer-config?PeerId={self.client.urlparse(peer_public_key)}")
        return response
    
    def peer_qr(self, peer_public_key: str) -> dict:
        '''
        Retrieve the QR code for a specific peer's configuration.
        Args:
            peer_public_key (str): The public key of the peer.
        '''
        response = self.client.request("GET", f"provisioning/data/peer-qr?PeerId={self.client.urlparse(peer_public_key)}")
        return response

    def user_info(self, user_id: str=None, email: str=None) -> dict:
        '''
        Retrieve provisioning information for a specific user.
        Args:
            user_id (str) (Optional): The user identifier that should be queried. If not set, the authenticated user is used.
            email (str) (Optional): The email address that should be queried. If UserId is set, this is ignored.
        '''
        response = self.client.request("GET", f"provisioning/data/user-info?UserId={self.client.urlparse(user_id)}&Email={self.client.urlparse(email)}")
        return response

    def new_peer(self, interface_id: str, preshared_key: str=None, PublicKey: str=None, UserId: str=None) -> dict:
        '''
        Generate a new peer configuration for the authenticated user.
        Args:
            interface_id (str): The unique identifier of the interface to which the peer will be added.
            preshared_key (str) (Optional): The preshared key for the new peer. If not provided, a new key is generated.
            PublicKey (str) (Optional): The public key for the new peer. If not provided, a new keypair will be generated.
            UserId (str) (Optional): The user identifier for whom the peer is being created. If not provided, the authenticated user will be used.
        '''
        data = {
            "InterfaceIdentifier": interface_id,
            "PresharedKey": preshared_key,
            "PublicKey": PublicKey,
            "UserId": UserId
        }
        response = self.client.request("POST", "provisioning/new/peer", json=data)
        return response