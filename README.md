# urlsecrets
Encode &amp; Decode Hidden Data within URLs
```
# Checkout customTextEncoder.py __main__ for more example usage
```
### + Added Open Redirects & Eval
```
# Checkout app.py, open.html, run.html
```
### + new %XX hex url obfuscation
```
from obfuscate import obfuscate_url, reveal_url

url = 'https://www.google.com/url?q=http://xn--vnx.io&source=gmail&ust=1707493827421000&usg=AOvVaw23x5jRb3D6jX_KKSFUdzBB'

obf = obfuscate_url(url,0, start=".com/")

print(obf)
print(":::::::::::")
print(reveal_url(obf)) # to convert it back

```

for example:<br>
https://www.google.com/url?q=http://akeyo.io/tami/projects/&source=gmail&ust=1707507885025000&usg=AOvVaw0SAMmHWB342iNiyumBmyQ2

will turn to: <br>
https://www.google.com/%75%72%6c?%71=%68%74%74%70://%61%6b%65%79%6f.%69%6f/%74%61%6d%69/%70%72%6f%6a%65%63%74%73/&%73%6f%75%72%63%65=%67%6d%61%69%6c&%75%73%74=%31%37%30%37%35%30%37%38%38%35%30%32%35%30%30%30&%75%73%67=%41%4f%76%56%61%77%30%53%41%4d%6d%48%57%42%33%34%32%69%4e%69%79%75%6d%42%6d%79%51%32&

Both should work equally
