from urllib import request
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from dbConnect import delete_one, insert_many, show_all,insert_one, delete_all, softDeleteAll_db, update_one

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

# impliments view inventory
@app.get("/checkinv")
async def testmyapi():
    data = show_all()
    return str(data)

# impliments singele addition
@app.post("/addinv")
async def testpostapi(inp: Request):
    rq= await inp.json()
    insert_one(rq)
    return str(rq)

# impliments update
@app.put("/updateinv")
async def testputapi(inp: Request):
    rq= await inp.json()
    update_one(rq)
    return str(rq)

# impliments soft delete
@app.put("/sDelete")
async def testputapi(inp: Request):
    rq= await inp.json()
    delete_one(rq)
    return str(rq)

# impliments soft deletea ll
@app.put("/sDeleteAll")
async def testputapi(inp: Request):
    rq= await inp.json()
    softDeleteAll_db(rq)
    return str(rq)

# impliment hard delete all
@app.get("/deleteall")
def testmyapi():
    delete_all()

# impliment insert many
@app.put("/addMultiInv")
async def testputapi(inp:Request):
    request_data=await inp.json()
    insert_many(request_data)
    return str("200")

# impliment clean messaging for all api type request