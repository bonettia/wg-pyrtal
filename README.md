# wg-pyrtal
Wrapper for wg-portal API



### Installation

Clone the repo and use it locally:

```bash
git clone <repository_link>
cd wg-pyrtal
pip install .
```

## Usage

from wg_pyrtal.client import WGPortal

client = WGPortal(<server-ip-address>, 8080, "user@example.com", "API_KEY")

### List all interfaces
interfaces = client.interfaces.all()\
print(interfaces)

### Create a new peer
peer = client.peers.create("wg1")\
print(peer["PublicKey"])

## Supported Endpoints

- Interfaces
- Metrics
- Peers
- Users
- Provisioning

All endpoints have corresponding methods in the wrapper with proper error handling.

---


## Contributing

This is a community wrapper. Feel free to open issues or PRs to improve functionality.

## License

MIT License