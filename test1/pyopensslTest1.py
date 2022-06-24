import OpenSSL

def getpubkey(filePath):
    pemFile = open(filePath,"rb")
    buffer = pemFile.read()

    pemCert = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, buffer)
    pubKey = OpenSSL.crypto.dump_publickey(
        OpenSSL.crypto.FILETYPE_PEM, pemCert.get_pubkey())
    return  pubKey

def getCert(filePath):
    pemFile = open(filePath,"rb")
    buffer = pemFile.read()

    pemCert = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, buffer)
    return  pemCert

certFile = "/home/user01/Programming/openssl/test1/server.crt"

# X509
pubKey = getpubkey(certFile)
print(pubKey)

cert = getCert(certFile)
