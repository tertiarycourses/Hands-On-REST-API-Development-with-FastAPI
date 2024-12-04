from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hi")
def greet(who: str = "World"):
    return {"message": f"Hello? {who}?"}

"""
The greet function is decorated with @app.get("/hi"), indicating that it handles GET requests to the /hi endpoint.
The who parameter is defined with a default value of "World". 
If the query parameter who is not provided in the request, the default value "World" will be used.
The function returns a JSON response with a message that includes the value of who.

Parameters:
localhost:8000/hi returns Hello? World?
localhost:8000/hi?who=FastAPI returns Hello? FastAPI?

"""

if __name__ == "__main__":
    uvicorn.run("hello_query:app", host="0.0.0.0", port=8000, reload=True)