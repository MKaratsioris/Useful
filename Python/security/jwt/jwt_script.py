from jwcrypto.jwk import JWK
from jwt import JWT, jwk_from_dict
from typing import Tuple, Dict
from pprint import pprint

jwt = JWT()

def generate_keys() -> Tuple[Dict[str, str]]:
    jwk = JWK.generate(
        kty="RSA", # key type
        size=2048,
        alg="RS256",
        use="sig", # sig = sign key
        kid="420" # key id = any number will do
    )
    return jwk.export_private(as_dict=True), jwk.export_public(as_dict=True)

def encode(data: dict, key: dict[str, str]) -> str:
    jwk = jwk_from_dict(key)
    return jwt.encode(data, jwk, alg="RS256", optional_headers={"typ": "JWT"})

def decode(token: str, key: dict[str, str]) -> Dict[str, str | int]:
    jwk = jwk_from_dict(key)
    return jwt.decode(token, jwk)

if __name__ == "__main__":
    data = {
        "sub": "1234567890",
        "name": "Julian Dirac",
        "admin": True,
        "iat": 1516239022 # 'iat' = Issued AT and it is the UNIX time stamp in seconds, starting count from 1970 (?)
    } # the keys in this dict are called 'Claims' and there are Registered Claim Names
    
    private_key, public_key = generate_keys()
    """print("\n---------------------PRIVATE KEY---------------------\n")
    pprint(private_key)
    print("\n---------------------PUBLIC KEY---------------------\n")
    pprint(public_key)
    print()"""
    
    token = encode(data, private_key)
    pprint(token)
    
    """
    eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.
    eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lI
    jogIkp1bGlhbiBEaXJhYyIsICJhZG1pbiI6IH
    RydWUsICJpYXQiOiAxNTE2MjM5MDIyfQ.
    cLufcUNvAMJb-Ffblc7ufoQOPQhG8oTyzjqYA
    uJ7Yten6qqf2DbJ2N1YkBa-3paF15m4kJkZpU
    -ueNAK3uONoWG_IYVhv5Q_CXnZp_xXm3h68Xw
    duqAQBGYeI1DwjjlI17OFnZspgIoXbCYIBOUB
    d77cdqSglSW3gyVBvS8Lu7WBRmpErpImXogbL
    6D9e-S7oUZ-XDhF8q1CqbHCrVl5oQ1RlpIGK8
    D-35rKmuvL4C3el_3IT36SmpIq7JSR4l7TCIZ
    6aFAebrxyoLtQ3fdkfKEOgMfsdJ6Zz5Xh418t
    BYWb50u3mWysKKIJnAs0eX8r3TdlVrWRVt3-n
    4zJBykJyQ
    """
    
    payload = decode(token, public_key)
    pprint(payload)
    
    # Example with 'exp' claim set to 100. This should raise an error during decoding phase:
    # jwt.exceptions.JWTDecodeError: JWT Expired
    
    data = {
        "sub": "1234567890",
        "name": "Julian Dirac",
        "admin": True,
        "iat": 1516239022,
        "exp": 100
    }
    private_key, public_key = generate_keys()
    token = encode(data, private_key)
    payload = decode(token, public_key)
    
    """
    In Google's case, maybe it is an OpenID connect specification, 
    the 'exp' claim is set to the value of 'iat' + 3_600
    """
