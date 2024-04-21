# QR code generator for Threema

This is a simple QR code generator for Threema. It generates a QR code that contains a Threema ID and a public key. The QR code can be scanned by the Threema app to add a contact.


## Prerequisites
install requirements file with 
```bash
pip install -r requirements.txt
```

## Usage
put threema id in _ids and public key in _public_keys and run the script
```bash
python qr.py
```

it will generate .png qr codes in the same directory