# from bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


engine = create_engine('sqlite:///nome.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Consultas(Base):
    __tablename__ = 'TAB_CONSULTA'
    idConsulta = Column(Integer, primary_key=True)
    data1 = Column(String, nullable=False)
    hora1 = Column(Integer, nullable=False)
    minuto = Column(Integer, nullable=False)
    motivo_id1 = Column(Integer, ForeignKey('TAB_MOTIVO.id_motivo'), nullable=False)
    idAnimal1 = Column(Integer, ForeignKey('TAB_ANIMAL.id_animal'), nullable=False)
    idVeterinario1 = Column(Integer, ForeignKey('TAB_VETERINARIO.id_vet1'), nullable=False)


    def save(self):
        db_session.add(self)
        db_session.commit()

    # função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()


    def serialize_consulta(self):
        dados_consulta = {
            "idConsulta": self.idConsulta,
            "motivo_id1": self.motivo_id1,
            "data1": self.data1,
            "hora1": self.hora1,
            "minuto": self.minuto,
            "idAimal": self.idAnimal1,
            "idVeterinario": self.idVeterinario1
        }

        return dados_consulta



class Motivo(Base):
    __tablename__ = 'TAB_MOTIVO'
    id_motivo = Column(Integer, primary_key=True)
    nome_motivo = Column(String, nullable=False)
    motivo_categoria = Column(String)
    valor_motivo = Column(Float, nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_motivo(self):
        dados_motivo = {
            "id_motivo": self.id_motivo,
            "nome_motivo": self.nome_motivo,
            "motivo_categoria": self.motivo_categoria,
            "valor_motivo": self.valor_motivo

        }

        return dados_motivo



class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True)
    Nome1 = Column(String, nullable=False)
    CPF = Column(String, nullable=False, unique=True)
    telefone = Column(Integer, nullable=False)
    Area1 = Column(String, nullable=False)
    Profissão1 = Column(String, nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_cliente(self):
        dados_cliente = {
            "id_cliente": self.id_cliente,
            "Nome1": self.Nome1,
            "CPF": self.CPF,
            "telefone": self.telefone,
            "Area1": self.Area1,
            "Profissão1": self.Profissão1

        }

        return dados_cliente



class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id_animal = Column(Integer, primary_key=True)
    nome_animal = Column(String, nullable=False)
    raca1 = Column(String,nullable=False)
    anoNasci1 = Column(Integer, nullable=False)
    idCliente1 = Column(Integer, ForeignKey('TAB_CLIENTE.id_cliente'), nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_animal(self):
        dados_animal = {
            "id_Animal": self.id_animal,
            "nome_animal": self.nome_animal,
            "raca1": self.raca1,
            "anoNasci1": self.anoNasci1,
            "idCliente1": self.idCliente1

        }

        return dados_animal

def init_db():
    Base.metadata.create_all(bind=engine)


# metodo de segurança
if __name__ == '__main__':
    init_db()
