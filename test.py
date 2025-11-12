from wg_pyrtal.client import WGPortal



client = WGPortal("10.94.112.10", 8080, "test@example.com", "8a17c22a-dc2c-4d4d-91d1-fcae36ef93ba")
response = client.interfaces.by_id("wg0")
print(response)
print("\n\n\n")
response = client.interfaces.create("wg3", "any")
print(response)
print("\n\n\n")
response = client.interfaces.update("wg3", "server", response["PrivateKey"], response["PublicKey"], ListenPort=51822)
print(response)
print("\n\n\n")
response = client.interfaces.all()
print(response)
print("\n\n\n")
response = client.interfaces.delete("wg3")
print(response)
print("\n\n\n")
response = client.interfaces.prepare()
print(response)
