from sqlite3 import connect
# - conectar com o banco de dados
conn = connect("blog.db")
cursor = conn.cursor()

# - Definir e criar a table caso ela não exista

conn.execute(
    """\
        CREATE TABLE IF NOT EXISTS post(
            id integer PRIMARY KEY AUTOINCREMENT,
            title varchar UNIQUE NOT NULL,
            content varchar NOT NULL,
            author varchar NOT NULL
        );
    """
)

posts = [
        {
            "title": "Python é eleita a linguagem mais popular",
            "content": """\
            A linguem Python foi eleita a linguagem mais popular pela revista
            tech masters e segue dominando o mundo.
            """,
            "author": "Satoshi Namamoto",
        },
        {
            "title": "Como criar um blog utilizando Python",
            "content": """\
            Neste tutorial você aprenderá como criar um blog utilizando Python.
            <pre> import make_a_blog </pre>
            """,
            "author": "Guido Van Rossum",
        },

    ]

    # - Inserir os posts no banco de dados caso ele esteja vazio

count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
            """\
            INSERT INTO post (title, content, author)
            VALUES (:title, :content, :author)
            """,
            posts,
        )
    conn.commit()

