from database import conn
from framah import Framah

app = Framah()


@app.route("^/$", template="list.template.html")
def index():
    posts = get_posts_from_database()
    return {"post_list": posts}

@app.route(r"^/(?P<id>\d{1,})$", template="post.template.html")
def post_detail(id):
    posts = get_posts_from_database(post_id=id)[0]
    return {"post": posts}

@app.route("^/new$", template="form.template.html")
def new_post_form():
    return {}

@app.route("^/new$", method="POST")
def new_post_add(form):
    post = {item.name: item.value for intem in form.list}
    posts = add_new_post(post)
    return "New post created with success!!!", "201 Creatde", "text/plain"


def get_posts_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]

def add_new_post(post):
    cursor = conn.cursor()
    cursor.execute(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        post,
    )
    conn.commit()


if __name__ == "__main__":
    app.run()