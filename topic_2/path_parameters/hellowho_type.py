# example of a shy endpoint with only a single endpoint
# this is the web layer, handling only web requests and responsibilities

from fastapi import FastAPI, Body
import uvicorn
import requests
import httpx
import json

app = FastAPI() # top-level FastAPI object that represents the whole webapp

@app.get("/hi") # path decorator, indicates that a request for the URL "/hi" on this server should be directed to the following function
def greet(who:str = Body(embed=True)): # path function AKA main point of contact with HTTP requests and responses
    return {"message": f"Hello? {who}"} # return message in a JSON format


"""
 The Body(embed=True) is needed to tell FastAPI that, this time, we
 get the value of who from the JSON-formatted request body. The
 embed part means that it should look like {"who": "Mom"} rather
 than just "Mom"
 
 The who:str in the path paremeters means that the function expects a single parameter which is a string. 
 
 The Body function then returns a params.Body object with all the provided parameters.
 This object is used by FastAPI to generate the appropriate request body schema and validation rules.
"""

# run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("hellowo_type:app", reload=True) # reload=True will restart the web server if hello.py changes
# the argument "hello:app" tells Uvicorn to run the "app" object in the "hello" module
# alternatively you can start a server in the command line with $ uvicorn hello:app --reload

# for easy testing, just add /hi to the end of the codespace link
# like this
# https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi
