from fastapi import FastAPI
import uvicorn

"""
Specific routes (/items/special and /users/me) are defined before general routes (/items/{item_id} and /users/{user_id}).
"""

app = FastAPI()

# Define a specific route before a general route
@app.get("/items/special")
def read_special_item():
    return {"item_id": "special"}

# Define a general route
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Define another specific route before a general route
@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

# Define a general route
@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}

"""
1. Specific Route Before General Route:
The route /items/special is defined before /items/{item_id}.
This ensures that requests to /items/special are matched to the specific route and not mistakenly interpreted as a request to /items/{item_id} with item_id being "special".

2. General Route:
The route /items/{item_id} is defined after /items/special.
This route will match any request to /items/{item_id} where item_id is an integer, but only if no more specific route matches first.

3. Another Specific Route Before General Route:
The route /users/me is defined before /users/{user_id}.
This ensures that requests to /users/me are matched to the specific route and not mistakenly interpreted as a request to /users/{user_id} with user_id being "me".

4. General Route:
The route /users/{user_id} is defined after /users/me.
This route will match any request to /users/{user_id} where user_id is a string, but only if no more specific route matches first.

If you define the general route before the specific route and you pass in /users/me, the general route will match first. 
This is because the general route (/users/{user_id}) will capture any path that follows users, including /users/me.

Here's what would happen step-by-step:
The request to /users/me is made.
The FastAPI router checks the defined routes in the order they were added.
If the general route (/users/{user_id}) is defined first, it will match /users/me and treat me as the user_id parameter.
The read_user function will be called with user_id set to "me".
The response will be {"user_id": "me"}.
This means the specific route (/users/me) will never be reached because the general route will always match first.
"""

# Run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("item_API:app", host="0.0.0.0", port=8000, reload=True)