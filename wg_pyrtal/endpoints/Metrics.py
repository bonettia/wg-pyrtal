from ..utils import urlparse

class Metrics:
    def __init__(self, client):
        self.client = client

    def interface(self, identifier: str) -> dict:
        '''
        Retrieve metrics for a specific interface.
        Args:
            identifier (str): The unique identifier of the interface.
        Returns:
            Dictionary notation of the interface metrics.
        '''
        response = self.client.request("GET", f"metrics/by-interface/{urlparse(identifier)}")
        return response
    
    def peer(self, identifier: str) -> dict:
        '''
        Retrieve metrics for a specific peer.
        Args:
            identifier (str): The unique identifier of the peer.
        Returns:
            Dictionary notation of the peer metrics.
        '''
        response = self.client.request("GET", f"metrics/by-peer/{urlparse(identifier)}")
        return response

    def user(self, identifier: str) -> dict:
        '''
        Retrieve metrics for a specific user.
        Args:
            identifier (str): The unique identifier of the user.
        Returns:
            Dictionary notation of the user metrics.
        '''
        response = self.client.request("GET", f"metrics/by-user/{urlparse(identifier)}")
        return response