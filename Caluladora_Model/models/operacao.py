from datetime import datetime, timezone
from . import db

class Operacao(db.Model):
    __tablename__ = 'operacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=False)
    operacao = db.Column(db.String(50), nullable=False)
    etapas = db.Column(db.Text, nullable=False)
    resultado = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
        )
        registro.adicionar()
        registro.commit()
        return registro

    def adicionar(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f'<Operacao {self.id}: {self.etapas}>'
