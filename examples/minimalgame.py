from core.unit import Unit
from core.realm import Realm
from core.action import Action
from core.engine import Engine

def pode_dormir(ctx):
    return True

def dormir(ctx):
    print("Você dorme e recupera forças.")

personagem = Unit(
    nome="Personagem",
    tipo="Unidade",
    pv=10
)

campo = Realm(
    nome="Campo",
    descricao="Um campo silencioso."
)

acao_dormir = Action(
    nome="Dormir",
    condicao=pode_dormir,
    efeito=dormir
)

campo.adicionar_unidade(personagem)
campo.adicionar_acao(acao_dormir)

engine = Engine(campo)
engine.loop()
