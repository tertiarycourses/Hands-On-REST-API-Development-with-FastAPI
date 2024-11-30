# example of a shy endpoint with only a single endpoint
# this is the web layer, handling only web requests and responsibilities

from fastapi import FastAPI
import uvicorn

app = FastAPI() # top-level FastAPI object that represents the whole webapp

@app.get("/hi") # path decorator, indicates that a request for the URL "/hi" on this server should be directed to the following function
def greet(): # path function AKA main point of contact with HTTP requests and responses
    return "Hellow? World?"

# run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True) # reload=True will restart the web server if hello.py changes
