from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hi")
def greet(who):
    return {"message": "{who}"}

"""
The endpoint function is defined as greet(who) again, but {who} isn't in the URL on
the previous decorator line this time, so FastAPI now assumes that who is a query parameter.
"""

# run the webapp in a web server with Uvicorn
if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True) # reload=True will restart the web server if hello.py changes
# the argument "hello:app" tells Uvicorn to run the "app" object in the "hello" module
# alternatively you can start a server in the command line with $ uvicorn hello:app --reload

# for easy testing, just add /hi to the end of the codespace link
# like this
# https://solid-acorn-9vwvj9q9gqwfgwq-8000.app.github.dev/hi
