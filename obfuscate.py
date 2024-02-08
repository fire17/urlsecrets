#obfuscate.py

# Turn a url into an obfuscated url with hexidecimal encoding lambda function
obfuscate_url = lambda url, n=2, start="?q=": (url.split(start)[0]+start+"://".join([ "%"+"%".join([text.encode().hex()[i:i+2] for i in range(0, len(text.encode().hex()), 2)]) for text in start.join(("&".join(url.split("&")[:-n]) if n>0 else url).split(start)[1:]).split("://") ]) + "&"+"&".join( url.split("&")[-n:] if n>0 else [] )).replace("%26","&").replace("%2e",".").replace("%3d","=").replace("%3f","?")

if __name__ = "__main__":
	url = 'https://www.google.com/url?q=http://xn--vnx.io&source=gmail&ust=1707493827421000&usg=AOvVaw23x5jRb3D6jX_KKSFUdzBB'
	obf = obfuscate_url(url, 0, start=".com/")
	print(obf)

'''
# To use:
from obfuscate import obfuscate_url
# using an existing url
hidden_url = obfuscate_url(url) # params (url,n,start) n: how many &elements to keep clear from the end, start: the string from which it will start the obfuscation
'''
