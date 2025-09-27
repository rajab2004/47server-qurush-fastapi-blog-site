from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is my first demo post.",
        "author": "Alice"
    },
    {
        "id": 2,
        "title": "FastAPI Tutorial",
        "content": "Learning how to build APIs with FastAPI.",
        "author": "Bob"
    },
    {
        "id": 3,
        "title": "Python Tips",
        "content": "Use list comprehensions for cleaner code.",
        "author": "Charlie"
    },
    {
        "id": 4,
        "title": "Database Design",
        "content": "Always normalize your database schema.",
        "author": "Diana"
    },
    {
        "id": 5,
        "title": "Travel Blog",
        "content": "I just visited Paris, it was amazing!",
        "author": "Eve"
    },
    {
        "id": 6,
        "title": "Cooking Recipe",
        "content": "Best pasta recipe with homemade sauce.",
        "author": "Frank"
    },
    {
        "id": 7,
        "title": "Book Review",
        "content": "1984 by George Orwell is a must-read.",
        "author": "Grace"
    },
    {
        "id": 8,
        "title": "Tech News",
        "content": "OpenAI just released a new AI model.",
        "author": "Henry"
    },
    {
        "id": 9,
        "title": "Sports Update",
        "content": "Real Madrid won their last game 3-1.",
        "author": "Ivy"
    },
    {
        "id": 10,
        "title": "Daily Motivation",
        "content": "Stay consistent, success will follow.",
        "author": "Jack"
    }
]


@app.get("/posts")
def get_posts(
    search: str | None = None,
    author: str | None = None,
    sort_by: str | None = None,
    page: int = 1,
    limit: int = 5
):
    result = posts


    if search:
        result = [
            post for post in result
            if search.lower() in post["title"].lower()
            or search.lower() in post["content"].lower()
        ]

    if author:
        result = [post for post in result if post["author"].lower() == author.lower()]

  
    if sort_by == "title":
        result = sorted(result, key=lambda x: x["title"])
    elif sort_by == "id":
        result = sorted(result, key=lambda x: x["id"])

    start = (page - 1) * limit
    end = start + limit
    result = result[start:end]

    return result


@app.get("/posts/{post_id}")
def get_one_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}


@app.post("/posts")
def create_post(post: dict):

    new_id = max(p["id"] for p in posts) + 1
    post["id"] = new_id
    posts.append(post)
    return {"message": "Post created", "post": post}


@app.put("/posts/{post_id}")
def update_post(post_id: int, new_post_data: dict):
    for post in posts:
        if post["id"] == post_id:
            post.update(new_post_data)
            return {"message": "Post updated", "post": post}
    return {"error": "Post not found"}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            return {"message": f"Post {post_id} deleted"}
    return {"error": "Post not found"}
        