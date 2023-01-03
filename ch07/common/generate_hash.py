from base64 import urlsafe_b64encode

h = urlsafe_b64encode(b"root:root")
print(h)
# cm9vdDpyb290
