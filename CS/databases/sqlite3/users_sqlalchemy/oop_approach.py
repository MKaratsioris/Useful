import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=db)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[str]
    email: Mapped[str]
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

def main() -> None:
    Base.metadata.create_all(db)
    first_user = User(username="Michalis Karatsioris", email="mk@email.com")
    second_user = User(username="Moraki", email="moraki@email.com")
    with Session() as session:
        session.add(first_user)
        session.add(second_user)
        session.commit()
        print(session.query(User).all())

if __name__ == '__main__':
    main()