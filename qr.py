# To generate Threema QR codes

import qrcode


def generate_qr_code(_id, _public_key):
    img = qrcode.make(f'3mid:{_id},{_public_key}')
    img.save(f"Threema_{_id}.png")


if __name__ == '__main__':
    _ids = [
        "EXAMPLE_ID_1",
    ]
    _public_keys = [
        "EXAMPLE_PUBLIC_KEY_1",
    ]
    for _id, _public_key in zip(_ids, _public_keys):
        print(f"Generating QR code for {_id}")
        generate_qr_code(_id, _public_key)

    print("Done!")
