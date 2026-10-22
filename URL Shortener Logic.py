import random
import string

urls = {}

url = input("Enter a URL: ")

code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

urls[code] = url

print("Short Code:", code)
print("Short URL: https://short.ly/" + code)

print("\nURL Lookup")
search = input("Enter short code: ")

if search in urls:
    print("Original URL:", urls[search])
else:
    print("URL not found")