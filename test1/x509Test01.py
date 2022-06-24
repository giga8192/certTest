from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat


def getCert(certFilePath):
    with open(certFilePath ,"rb") as fin:
        pem_data = fin.read()
        return x509.load_pem_x509_certificate(pem_data)

# テスト用
certFilePath = "/home/user01/Programming/openssl/test1/server.crt"
cert = getCert(certFilePath)
print(cert)
print(cert.public_key())
pubKey = cert.public_key() # RSAPublicKey

# (e,n)の出力
#print(pubKey.public_numbers())
print(pubKey.public_numbers().e) # e
print("{0:x}".format(pubKey.public_numbers().n)) # n


# エンコード形式とフォーマットを指定して書き出し
print(pubKey.public_bytes(Encoding.PEM,PublicFormat.SubjectPublicKeyInfo))

#####################################
modStr= "00:f1:14:d8:ae:f5:81:f0:d3:7f:88:67:d2:cb:a3:e1:71:ff:db:84:1a:d0:66:92:1e:38:4c:cb:c6:a3:2e:0e:91:b3:b9:dc:97:41:35:d9:82:ce:79:88:c2:92:f9:3b:d4:3d:23:76:1e:94:37:ae:63:6f:6e:75:a4:71:77:c8:e7:2f:67:72:c0:a6:e2:38:8a:9e:f9:62:69:43:98:32:ef:48:5c:59:da:b0:7a:cf:aa:29:20:3d:1c:3c:0d:74:c4:28:88:b1:73:fd:a2:4d:36:f6:28:1b:84:db:d5:ba:6e:88:4d:b9:dc:64:3f:35:a0:59:d5:84:ff:c1:75:6b:c0:0e:20:5b:36:ac:a6:2e:c0:39:44:c8:d3:56:3b:28:36:85:53:d7:65:42:41:51:74:eb:c7:81:52:f3:b0:39:4d:3f:16:dc:ae:3b:69:9a:1b:95:02:0a:dd:6a:ee:00:7b:da:63:06:34:37:3c:5f:0b:5c:ab:54:5c:7f:e2:35:37:a2:fb:9d:0c:c0:1f:36:58:a1:45:69:42:a9:ca:5a:e6:b7:9c:93:4c:7f:32:4f:de:3e:67:9b:62:9e:6f:d5:32:03:93:df:f5:bd:8f:ff:9f:50:fb:71:4f:ec:61:be:15:8d:d7:72:8a:d3:d1:24:24:ef:9d:82:b8:5f:51:42:97"
myN = int("".join(modStr.split(":")),16)
print("手動で出したn: {0:x}".format(myN))

if pubKey.public_numbers().n == myN:
    print("一致")
else:
    print("不一致")
