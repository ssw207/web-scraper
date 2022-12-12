list = ["http://a", "http://b", "c"]

for val in list:
    if not val.startswith("http"):
        web = f"https://{val}"
        print(web)
    else:
        print(val)

