class Users:
    def __init__(self, client):
        self.client = client

    def all(self) -> dict:
        '''
        Retrieve all users.
        '''
        return self.client.request("GET", "user/all")

    def by_id(self, user_id) -> dict:
        '''
        Retrieve a user by their ID.
        Args:
            user_id (str): The unique identifier of the user.
        '''
        return self.client.request("GET", f"user/by-id/{self.client.urlparse(user_id)}")

    def create(self, id: str, **extra: dict) -> dict:
        '''
        Create a new user.
        Args:
            id (str): The unique identifier of the user.
            **extra: Additional user attributes.
        '''
        data = {"id": id, **extra}
        return self.client.request("POST", "user/new", data=data)

    def update(self, id: str, **extra) -> dict:
        '''
        Update an existing user.
        Args:
            id (str): The unique identifier of the user.
            **extra: Additional user attributes to update.
        '''
        data = {"id": id, **extra}
        return self.client.request("PUT", f"user/by-id/{self.client.urlparse(id)}", data=data)

    def delete(self, id: str) -> bool:
        '''
        Delete a user by their ID.
        Args:
            id (str): The unique identifier of the user.
        '''
        return self.client.request("DELETE", f"user/by-id/{self.client.urlparse(id)}")