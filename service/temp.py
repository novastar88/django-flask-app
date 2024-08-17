import os

a = os.path.abspath(os.path.join(__file__, os.pardir))
print(os.path.abspath(os.path.join(a, os.pardir)))