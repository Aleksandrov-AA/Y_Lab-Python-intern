def domain_name(url):
    if '//' in url:
        result = url.split('//')[1]
    else:
        result = url
    result = result.split('.')
    if result[0] == 'www':
        return result[1]
    else:
        return result[0]
  

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
