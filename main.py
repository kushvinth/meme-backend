from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Posts
from datetime import datetime
import platform


app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allows request from all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#we store our posts here
posts = [
    Posts(
        id=1,
        title="nov theory",
        description="nov born kids exist cuz of valentines day!",
        timestamp=datetime.utcnow(),
    )
]

@app.get("/")
async def greet():
    return {"pickup_line_1":"Are you lightning? Cuz I wanna make you McQueen", "pickup_line_2":"I would never take you to an art museum cuz what if they keep you there? *winks*"}

@app.get("/feed")
async def feed():
    return posts

@app.post("/create")
async def create(post: Posts):
    # set timestamp if missing
    if post.timestamp is None:
        post.timestamp = datetime.utcnow()
    posts.append(post)
    return {"message": "Post created", "post": post}

@app.put("/edit/{id}")
async def edit_post(id: int, post: Posts):
    # Find the post by id and replace it. Return 404 if not found.
    for idx, existing in enumerate(posts):
        if existing.id == id:
            # preserve timestamp if not provided in the update
            if post.timestamp is None:
                post.timestamp = existing.timestamp
            posts[idx] = post
            return {"message": "Post updated", "post": post}
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/delete/{id}")
async def delete_post(id:int,post:Posts):
    for idx,existing in enumerate(posts):
        if existing.id == id:
            posts.remove(existing) #deleting by passing value
            return {"message": "Post deleted", "post":existing}
    raise HTTPException(status_code=404,detail="Post Not Found")


@app.get("/alive")
async def alive():
    osname = platform.system()
    return {"message": f"I am alive, running on {{{osname}}}"}