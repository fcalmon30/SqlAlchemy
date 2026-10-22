from sqlalchemy import create_engine, text 
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
#Configuracoes
engine = create_engine('mysql+pymysql://root:1234@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable= False)

    def __repr__(self):
        return f"Filme (titulo={self.titulo}, ano={self.ano})"

#SQL

#INSERT
data_insert= Filmes(titulo="Guerra ao Terror", genero="Acao", ano=2005)
session.add(data_insert)
session.commit()

#DELETE
session.query(Filmes).filter(Filmes.titulo=="Nsei").delete()
session.commit()   

#UPDATE
session.query(Filmes).filter(Filmes.genero=="Drama").update({'ano': 2000})
session.commit()

#SELECT
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()