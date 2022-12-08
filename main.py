from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
async def send_messages_all_active_lists():
    return {"message": "hello!"}
