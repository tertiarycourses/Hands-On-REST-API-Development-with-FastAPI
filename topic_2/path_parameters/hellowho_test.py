import requests
import httpx

if __name__ == "__main__":
    token = "insert results of echo $GITHUB_TOKEN here"
    headers = {"X-GitHub-Token": token}
    
    # -----TEST USING REQUESTS-----
    r = requests.get(
        "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi/Mom",
        headers=headers,
    )
    print("OUTPUT USING REQUESTS TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? Mom?"}

    # -----TEST USING HTTPX-----
    r = httpx.get(
        "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi/Mom",
        headers=headers,
    )
    print("OUTPUT USING HTTPX TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? Mom?"}

    """
    In each case, the string "Mom" is passed as part of the URL, passed to the greet() path
    function as the who variable, and returned as part of the response.
    The response in each case is the JSON string (with single or double quotes, 
    depending on which test client you used) is "Hello? Mom?"
    """