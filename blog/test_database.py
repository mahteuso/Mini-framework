import pytest
from .database import conn

cursor = conn.cursor()

def test_database():


    # - Criar os primeiros posts iniciais para abastecer o banco de dados

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

    # - testando se os dados foram inseridos
    result = cursor.execute("SELECT * FROM post;").fetchall()[0]

    assert result[1] == posts[0]["title"]
    assert result[2] == posts[0]["content"]
    assert result[3] == posts[0]["author"]
   