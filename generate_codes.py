import hashlib

# def generateQuad():
#     return ''.join(random.choice('0123456789ABCDEF') for i in range(4))
#
# import random
# for i in range(150):
#     S = generateQuad() + '-' + generateQuad() + '-' + generateQuad() + '-' + generateQuad()
#     print(S)

for line in open('raw_codes.txt', 'r'):
    ans = line.strip().encode()
    print(hashlib.sha256(ans).hexdigest())
