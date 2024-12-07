import requests
import httpx

if __name__ == "__main__":
    token = "ghu_dbzLzgzJ9IITk90RD5Os3Q6htjmJZT2btkDy"
    headers = {"X-GitHub-Token": token}
    base_url = "https://fuzzy-space-eureka-p6ppx676xg6f7jrp.github.dev/hi"

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