from fastapi import FastAPI, HTTPException


app = FastAPI()

trick_list = []

TRICK_ALREADY_EXIST = HTTPException(status_code=400, detail="Trick already exists")
TRICK_NOT_FOUND = HTTPException(status_code=404, detail="Trick not found")
@app.get("/tricks")
def get_tricks():
    return trick_list

@app.post("/add_trick")
def add_trick(trick: str):
    if trick in trick_list:
        raise TRICK_ALREADY_EXIST
    trick_list.append(trick)
    return {"message": f"Trick '{trick}' added successfully"}

@app.delete("/delete_trick/")
def delete_trick(trick: str):
    if trick not in trick_list:
        raise TRICK_NOT_FOUND
    trick_list.remove(trick)
    return {"message": f"Trick '{trick}' deleted successfully"}