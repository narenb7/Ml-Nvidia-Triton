from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/

app = FastAPI()

@app.get("/", tags=["Health Check"])
async def root():


     r1 = requests.get("http://ec2-54-157-42-29.compute-1.amazonaws.com:8001/")
     r2 = requests.get("http://ec2-54-157-42-29.compute-1.amazonaws.com:8002/")
     return r1.text, r2.text


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
