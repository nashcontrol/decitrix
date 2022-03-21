
import binascii,sys

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# based on https://dozer.nz/posts/citrix-decrypt/, follow instructions if you have -kek flag in your Netscaler config file

def decrypt(ciphertext):
    aeskey = "351CBE38F041320F22D990AD8365889C7DE2FCCCAE5A1A8707E21E4ADCCD4AD9"
    cipher = AES.new(binascii.unhexlify(aeskey), AES.MODE_CBC)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def main():

    
    ciphertext = binascii.unhexlify(sys.argv[1])
    if (len(ciphertext) % 16 != 0):
        print("ciphertext must be padded to AES CBC block size(16)")
        sys.exit()
    
    decoded = decrypt(ciphertext)
    
    print('Decryption using hardcoded AES-CBC key with empty IV')
    print(decoded[16:].decode('UTF-8'))

if __name__ == "__main__":
    if len(sys.argv)==2:
        main()
    else:
        print("Usage: decitrix.py ciphertext")