from wg_pyrtal.client import WGPortal


def test_interfaces_endpoint():
    client = WGPortal("127.0.0.1", 8000, "user", "pass")
    interfaces = client.interfaces
    interfaces.create(
        id="test-interface",
        mode="client")