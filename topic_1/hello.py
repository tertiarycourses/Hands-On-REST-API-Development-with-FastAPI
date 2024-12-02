# example of a shy endpoint with only a single endpoint
# this is the web layer, handling only web requests and responsibilities

from fastapi import FastAPI
import uvicorn
import requests
import httpx
import json

app = FastAPI() # top-level FastAPI object that represents the whole webapp

@app.get("/hi") # path decorator, indicates that a request for the URL "/hi" on this server should be directed to the following function
def greet(): # path function AKA main point of contact with HTTP requests and responses
    return {"message": "Hello? World?"} # return message in a JSON format

# run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True) # reload=True will restart the web server if hello.py changes
# the argument "hello:app" tells Uvicorn to run the "app" object in the "hello" module
# alternatively you can start a server in the command line with $ uvicorn hello:app --reload

# for easy testing, just add /hi to the end of the codespace link
# like this
# https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi
