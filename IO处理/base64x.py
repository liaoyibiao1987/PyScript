import base64  
  
text = "MoreWindows - http://blog.csdn.net/morewindows?viewmode=contents ~!@#$%"  
  
# encodestring(string) and decodestring(string)
print("------------------------------------")
print("origin text: ")
print(text)

base64_text0 = base64.encodestring(bytes(text, 'utf-8')) 
#x = b'我们不一样'
#base64_text1 = base64.encodestring(x) 
#base64_text = base64.encodestring(text)  
print("encode: ")
print(base64_text0)
  
print("decode: ")
print(base64.decodestring(base64_text0))
print("------------------------------------")
  
  
# urlsafe_b64encode(string) and urlsafe_b64decode(string)
print("------------------------------------")
print("origin text: ")
print(text)
  
urlsafe_base64_text = base64.urlsafe_b64encode(text)  
print("url safe encode: ")
print(urlsafe_base64_text)
  
print("url safe decode: ")
print(base64.urlsafe_b64decode(urlsafe_base64_text))
print("------------------------------------")