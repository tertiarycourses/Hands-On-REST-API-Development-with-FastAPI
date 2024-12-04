from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/hi/{name}")
def greet(name: str, greeting: str = Query(...)):
    return {"message": f"{greeting}, {name}!"}

"""
The greet function is decorated with @app.get("/hi/{name}"), indicating that it handles GET requests to the /hi/{name} endpoint.
The name parameter is a path parameter, which means it is part of the URL path.
The greeting parameter is a required query parameter, indicated by Query(...).
If the query parameter greeting is not provided in the request, FastAPI will return a 422 Unprocessable Entity error.
The function returns a JSON response with a message that includes the values of name and greeting.

Examples:
localhost:8000/hi/John?greeting=Hello returns {"message": "Hello, John!"}
localhost:8000/hi/John without the greeting query parameter will return a 422 error.
"""

if __name__ == "__main__":
    uvicorn.run("hello_path_query:app", host="0.0.0.0", port=8000, reload=True)