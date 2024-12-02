import requests
import httpx

"""
Tests both specific and general routes to show how they are matched

Testing Specific Routes:
The tests for /items/special and /users/me ensure that these specific routes are matched correctly and return the expected responses.
If these routes were defined after the general routes, they might not be matched correctly.

Testing General Routes:
The tests for /items/123 and /users/john ensure that the general routes are matched correctly and return the expected responses.
These routes should match any valid path parameters that do not match the specific routes.
"""

if __name__ == "__main__":
    token = "insert results of echo $GITHUB_TOKEN here"
    headers = {"X-GitHub-Token": token}
    base_url = "https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev"

    # -----TEST USING REQUESTS-----
    # Test specific route
    r = requests.get(f"{base_url}/items/special", headers=headers)
    print("OUTPUT USING REQUESTS TEST - /items/special")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"item_id": "special"}

    # Test general route
    r = requests.get(f"{base_url}/items/123", headers=headers)
    print("OUTPUT USING REQUESTS TEST - /items/123")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"item_id": 123}

    # Test specific route
    r = requests.get(f"{base_url}/users/me", headers=headers)
    print("OUTPUT USING REQUESTS TEST - /users/me")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"user_id": "the current user"}

    # Test general route
    r = requests.get(f"{base_url}/users/john", headers=headers)
    print("OUTPUT USING REQUESTS TEST - /users/john")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"user_id": "john"}

    # -----TEST USING HTTPX-----
    # Test specific route
    r = httpx.get(f"{base_url}/items/special", headers=headers)
    print("OUTPUT USING HTTPX TEST - /items/special")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"item_id": "special"}

    # Test general route
    r = httpx.get(f"{base_url}/items/123", headers=headers)
    print("OUTPUT USING HTTPX TEST - /items/123")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"item_id": 123}

    # Test specific route
    r = httpx.get(f"{base_url}/users/me", headers=headers)
    print("OUTPUT USING HTTPX TEST - /users/me")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"user_id": "the current user"}

    # Test general route
    r = httpx.get(f"{base_url}/users/john", headers=headers)
    print("OUTPUT USING HTTPX TEST - /users/john")
    print(r.status_code)  # Should print 200
    print(r.json())       # Should print {"user_id": "john"}