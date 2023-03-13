import hashlib
print("md5算法".center(40,'-'))
hash = hashlib.md5()
print(hash)
print(hash.update('liuyao199539'.encode('utf-8')))
print(hash.hexdigest())

print("sha256算法".center(40,'-'))
sha_256 = hashlib.sha256()
print(sha_256.update('liuyao'.encode('utf-8')))
print(sha_256.hexdigest())

print("sha384算法".center(40,'-'))
sha_384 = hashlib.sha384()
print(sha_384.update('liuyao'.encode('utf-8')))
print(sha_384.hexdigest())

print("sha512算法".center(40,'-'))
sha_512 = hashlib.sha512()
print(sha_512.update('liuyao'.encode('utf-8')))
print(sha_512.hexdigest())

print("对加密算法中添加自定义key再来做加密，防止被撞库破解".center(40,'-'))
md5_key = hashlib.md5('jwhfjsdjbwehjfgb'.encode('utf--8'))
print(md5_key.update('liuyao'.encode('utf-8')))
print(md5_key.hexdigest())

print("import hmac(Keyed-Hashing for Message Authentication)".center(40,'-'))
import hmac
key = b'secretk-key'
#key2 = 'secretk-key'.encode('utf-8')
#hm2 = hmac.new(key,message, digestmod='MD5')
hm = hmac.new(key)
hm.update('被加密数据'.encode('utf-8'))
print(hm.hexdigest())



print("Struct解码".center(60,"="))
import struct
try:
    with open('test.bmp', 'rb') as testbmp:
        databmp = testbmp.read()
        infor = struct.unpack('<ccIIIIIIHH', databmp[0:30])
        print(infor)
finally:
    if testbmp:
        testbmp.close()
    