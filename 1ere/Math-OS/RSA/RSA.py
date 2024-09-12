def code_ou_decode(clef: int, commun: int, message: int) -> int: return (message ** clef) % commun
# test

public_key = 83
private_key = 35
intersection = 299

message = 12

print(code_ou_decode(private_key, intersection, code_ou_decode(public_key, intersection, message)))