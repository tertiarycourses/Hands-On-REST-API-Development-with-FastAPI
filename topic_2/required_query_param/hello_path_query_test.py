import requests
import httpx

if __name__ == "__main__":
    token = "insert results of echo $GITHUB_TOKEN here"
    headers = {"X-GitHub-Token": token}
    base_url = "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi"

    # -----TEST USING REQUESTS-----
    # Test with path parameter and required query parameter
    r = requests.get(f"{base_url}/John", headers=headers, params={"greeting": "Hello"})
    print("OUTPUT USING REQUESTS TEST - Required Query Parameter")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello, John!"}

    # Test without required query parameter
    r = requests.get(f"{base_url}/John", headers=headers)
    print("OUTPUT USING REQUESTS TEST - Missing Required Query Parameter")
    print(r.status_code)  # Should print 422

    # -----TEST USING HTTPX-----
    # Test with path parameter and required query parameter
    r = httpx.get(f"{base_url}/John", headers=headers, params={"greeting": "Hello"})
    print("OUTPUT USING HTTPX TEST - Required Query Parameter")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"message": "Hello, John!"}

    # Test without required query parameter
    r = httpx.get(f"{base_url}/John", headers=headers)
    print("OUTPUT USING HTTPX TEST - Missing Required Query Parameter")
    print(r.status_code)  # Should print 422