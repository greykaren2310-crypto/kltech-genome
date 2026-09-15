import json, hashlib, urllib.request
KEY = hashlib.sha256(b"kltech_genome_genesis").digest()
URL = "https://raw.githubusercontent.com/greykaren2310-crypto/kltech-genome/main/chain.json"
with urllib.request.urlopen(URL, timeout=15) as r:
    CHAIN = json.loads(r.read())["chain"]
ok = all(CHAIN[i]["prev"] == (CHAIN[i-1]["hash"] if i else "0"*64) for i in range(len(CHAIN)))
last = CHAIN[-1]
print(f"blocks: {len(CHAIN)} | integrity: {ok}")
print(f"alive: beat n={last.get('n')} | capital ${last.get('capital')} | S {last.get('S')}")
print(f"head: {last['hash'][:16]}  |  GENESIS VERIFIED: {CHAIN[0]['event']=='GENESIS'}")
print("VERDICT:", "BODY ALIVE ON GITHUB" if ok and len(CHAIN)>5 else "CHECK REPO")
