# decitrix
Decrypt LDAP encrypted values found in Citrix Netscaler config file.\
Clone of https://dozer.nz/posts/citrix-decrypt/

## Installation
The script was tested on Python3.8, Running on macOS Big Sur.

Clone repo and install packages:

```sh
git clone https://github.com/nashcontrol/decitrix.git
cd decitrix

pip3 install -r requirements.txt --user
```

## Usage
```
python3 decitrix.py b65f2142d01fe706083173b064c04cfc6b81ab2417d39d63d2b3216176d0e638b89cbca0f1c4294db56b66668f94ff0f

Decryption using hardcoded AES-CBC key with empty IV
test12345678secretldappassword
```
