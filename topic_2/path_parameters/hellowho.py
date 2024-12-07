# example of a shy endpoint with only a single endpoint
# this is the web layer, handling only web requests and responsibilities

from fastapi import FastAPI
import uvicorn
import requests
import httpx
import json

app = FastAPI() # top-level FastAPI object that represents the whole webapp

@app.get("/hi/{who}") # path decorator, indicates that a request for the URL "/hi" on this server should be directed to the following function
def greet(who): # path function AKA main point of contact with HTTP requests and responses
    return {"message": f"Hello? {who}"} # return message in a JSON format


"""
 Adding that {who} in the URL (after @app.get) tells FastAPI to expect a variable
 named `who` at that position in the URL. FastAPI then assigns it to the who argument in
 the following greet() function. This shows coordination between the path decorator
 and the path function.
 
 Do not use a Python f-string for the amended URL string ("/hi/
 {who}") here. The curly brackets are used by FastAPI itself to
 match URL pieces as path parameters

 In essence:
 @app.get("/hi/{who}"): This decorator indicates that the function greet should handle GET requests to the URL path /hi/{who}.
 who: This is the path parameter. When a request is made to a URL like /hi/John, the value John will be captured and passed to the greet function as the who argument.

"""

# run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("hellowho:app", reload=True) # reload=True will restart the web server if hello.py changes
# the argument "hello:app" tells Uvicorn to run the "app" object in the "hello" module
# alternatively you can start a server in the command line with $ uvicorn hello:app --reload

# for easy testing, just add /hi to the end of the codespace link
# like this
# https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi
