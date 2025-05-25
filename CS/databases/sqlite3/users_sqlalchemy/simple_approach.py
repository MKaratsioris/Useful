import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:", echo=True)
connection = engine.connect()

metadata = sa.MetaData()

user_table = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String),
    sa.Column('email', sa.String),
)

def insert_user(username: str, email: str) -> None:
    query = user_table.insert().values(username=username, email=email)
    connection.execute(query)

def select_user(username: str) -> sa.engine.Result:
    query = user_table.select().where(user_table.c.username == username)
    return connection.execute(query).fetchone()

def main() -> None:
    metadata.create_all(engine)
    insert_user(username="Michalis", email="mk@email.com")
    insert_user(username="Tina", email="t@email.com")
    insert_user(username="Ale", email="a@email.com")
    insert_user(username="Shiushin", email="s@email.com")
    print(select_user(username="Michalis"))
    print(select_user(username="Ale"))
    connection.close()

if __name__ == '__main__':
    main()