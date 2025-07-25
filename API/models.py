from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from decimal import Decimal
from enum import Enum


#-----------schemas pra entidade usuario-----------
class UsuarioBase(BaseModel):
    email: EmailStr
    tipo_usuario: str = Field(..., max_length=50)

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id_usuario: int

#-----------schemas pra entidade posição-----------
class PosicaoVolei(str, Enum):
    LEVANTADOR = "Levantador"
    OPOSTO = "Oposto"
    PONTEIRO = "Ponteiro/Passador"
    CENTRAL = "Central"
    LIBERO = "Líbero"
    
class Posicao(BaseModel):
    nome_posicao: PosicaoVolei #usado pra garantir que a posição lida seja do volei
    funcao_tatica: Optional[str] = None

#-----------schemas pra entidade Atleta-----------
class AtletaBase(BaseModel):
    nome: str = Field(..., max_length=150)
    data_nascimento: date
    nacionalidade: Optional[str] = Field(None, max_length=50)
    altura: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)
    peso: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    nivel_tecnico: Optional[int] = Field(None, ge=1, le=10)

class AtletaCreate(AtletaBase):
    pass

class Atleta(AtletaBase):
    id_atleta: int

#-----------schemas pra entidade info Jogador-----------   
class InfoJogadorBase(BaseModel):
    id_atleta: int
    data_coleta: Optional[date] = None
    media_pontos_jogo: Optional[Decimal] = Field(None, max_digits=4, decimal_places=2, ge=0)
    aproveitamento_ataque: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_passe: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_levantamento: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    alcance_ataque: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)
    alcance_block: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)

class InfoJogadorCreate(InfoJogadorBase):
    pass

class InfoJogador(InfoJogadorBase):
    id_info: int

#-----------schemas pra entidade Atleta Posição-----------
class AtletaPosicaoBase(BaseModel):
    id_atleta: int
    nome_posicao: PosicaoVolei #novamente utilizando o enum pra saber se o atleta está numa posição do volei

class AtletaPosicaoCreate(AtletaPosicaoBase):
    pass


class AtletaPosicao(AtletaPosicaoBase):
    pass

#-----------schemas pra entidade Avaliação-----------
class AvaliacaoBase(BaseModel):
    id_atleta: int
    id_usuario: int
    data: date
    comentario: Optional[str] = None
    nota_tecnica: Optional[int] = Field(None, ge=1, le=10)
    nota: Optional[int] = Field(None, ge=1, le=10)

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    id_avaliacao: int