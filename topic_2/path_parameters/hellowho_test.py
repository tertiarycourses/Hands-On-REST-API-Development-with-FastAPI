import requests
import httpx

if __name__ == "__main__":
    token = "ghu_dbzLzgzJ9IITk90RD5Os3Q6htjmJZT2btkDy"
    headers = {"X-GitHub-Token": token}
    
    # -----TEST USING REQUESTS-----
    r = requests.get(
        "https://fuzzy-space-eureka-p6ppx676xg6f7jrp.github.dev/hi/Mom",
        headers=headers,
    )
    print("OUTPUT USING REQUESTS TEST")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello? Mom?"}

    # -----TEST USING HTTPX-----
    r = httpx.get(
        "https://fuzzy-space-eureka-p6ppx676xg6f7jrp.github.dev/hi/Mom",
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