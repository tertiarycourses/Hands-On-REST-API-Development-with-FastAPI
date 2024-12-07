import requests
import httpx
"""
For security, as Github Codespaces exposes the URL through a public link, for requests made to our server (which is hosted by GitHub by virtue of the machine that is currently running this Codespace)
we will have to include our Session Token in here.
You can find your session token using this command in the terminal:

```
echo $GITHUB_TOKEN
```
The token always starts with ghu_
We can then use curl to access it with the token:
```
curl ADDRESS -H "X-Github-Token: TOKEN"
```
"""

if __name__ == "__main__":
    token = "ghu_rI3gjCjubAtQWoj5YRzRE6NRS8HB470ARNFF"
    headers = {"X-GitHub-Token": token}
    # -----TEST USING REQUESTS-----
    r = requests.get(
        "https://fuzzy-space-eureka-p6ppx676xg6f7jrp.github.dev/hi",
        headers=headers,
    )
    print("OUTPUT USING REQUESTS TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? World?"}

    # -----TEST USING HTTPX-----
    r = httpx.get(
        "https://fuzzy-space-eureka-p6ppx676xg6f7jrp.github.dev/hi",
        headers=headers,
    )
    print("OUTPUT USING HTTPX TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? World?"}