import argparse
import hashlib

parser = argparse.ArgumentParser(description="hashing given password")
parser.add_argument("password", help="please provide the password you want hashed")
parser.add_argument("-t", "--type", default='sha256',choices=['sha256', 'sha512', 'md5'])
args = parser.parse_args()


password = args.password
hashtype = args.type

m = getattr(hashlib,hashtype)()
m.update(password.encode())

# output
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())