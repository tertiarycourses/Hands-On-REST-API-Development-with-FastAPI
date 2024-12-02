import requests
import httpx
"""
For security, as Github Codespaces exposes the URL through a public link, for requests made to our server (which is hosted by GitHub by virtue of the machine that is currently running this Codespace)
we will have to include our Session Token in here.
You can find your session token using this command in the terminal:

```
echo $GITHUB_TOKEN
```
The tolen always starts with ghu_
We can then use curl to access it with the token:
```
curl ADDRESS -H "X-Github-Token: TOKEN"
```
"""

if __name__ == "__main__":
    token = "insert results of echo $GITHUB_TOKEN here"
    headers = {"X-GitHub-Token": token}
    # -----TEST USING REQUESTS-----
    r = requests.get(
        "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi",
        headers=headers,
    )
    print("OUTPUT USING REQUESTS TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? World?"}

    # -----TEST USING HTTPX-----
    r = httpx.get(
        "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi",
        headers=headers,
    )
    print("OUTPUT USING HTTPX TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? World?"}