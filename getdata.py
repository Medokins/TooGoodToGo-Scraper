from tgtg import TgtgClient

client = TgtgClient(email="your email here")
credentials = client.get_credentials()
print(credentials)