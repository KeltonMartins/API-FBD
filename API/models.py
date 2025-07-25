from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from decimal import Decimal
from enum import Enum

#define as poisções do volei
class PosicaoVoleiEnum(str, Enum):
    
    LEVANTADOR = "Levantador"
    OPOSTO = "Oposto"
    PONTEIRO = "Ponteiro/Passador"
    CENTRAL = "Central"
    LIBERO = "Líbero"

#schemas do usuario
class Usuario(BaseModel):
    #leitura de um usuário
    id_usuario: int
    email: EmailStr
    tipo_usuario: str

class UsuarioCreate(BaseModel):
    #criar um novo usuário
    email: EmailStr
    tipo_usuario: str = Field(..., max_length=50)

class UsuarioUpdate(BaseModel):
    #atualizar um usuário
    email: Optional[EmailStr] = None
    tipo_usuario: Optional[str] = Field(None, max_length=50)

#schema da posição
class Posicao(BaseModel):
    #leitura de uma posição, sem criação ou update
    nome_posicao: PosicaoVoleiEnum
    funcao_tatica: Optional[str] = None

#schemas da atleta
class Atleta(BaseModel):
    #leitura de um atleta
    id_atleta: int
    nome: str
    data_nascimento: date
    nacionalidade: Optional[str] = None
    altura: Optional[Decimal] = None
    peso: Optional[Decimal] = None
    nivel_tecnico: Optional[int] = None

class AtletaCreate(BaseModel):
    #criar um novo atleta, todas as informações do atletas são obrigatorias
    nome: str = Field(..., max_length=150)
    data_nascimento: date
    nacionalidade: str = Field(..., max_length=50)
    altura: Decimal = Field(..., max_digits=3, decimal_places=2, ge=0)
    peso: Decimal = Field(..., max_digits=5, decimal_places=2, ge=0)
    nivel_tecnico: int = Field(..., ge=1, le=10)

class AtletaUpdate(BaseModel):
    #dar update no atleta
    nome: Optional[str] = Field(None, max_length=150)
    data_nascimento: Optional[date] = None
    nacionalidade: Optional[str] = Field(None, max_length=50)
    altura: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)
    peso: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    nivel_tecnico: Optional[int] = Field(None, ge=1, le=10)

#schemas infoJogador
class InfoJogador(BaseModel):
    #leitura das informações de um jogador
    id_info: int
    id_atleta: int
    data_coleta: Optional[date] = None
    media_pontos_jogo: Optional[Decimal] = None
    aproveitamento_ataque: Optional[Decimal] = None
    aproveitamento_passe: Optional[Decimal] = None
    aproveitamento_levantamento: Optional[Decimal] = None
    alcance_ataque: Optional[Decimal] = None
    alcance_block: Optional[Decimal] = None

class InfoJogadorCreate(BaseModel):
    #criar um novo registro de informações
    id_atleta: int
    data_coleta: date
    media_pontos_jogo: Optional[Decimal] = Field(None, max_digits=4, decimal_places=2, ge=0)
    aproveitamento_ataque: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_passe: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_levantamento: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    alcance_ataque: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)
    alcance_block: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)

class InfoJogadorUpdate(BaseModel):
    #atualizar as informações de um jogador
    data_coleta: Optional[date] = None
    media_pontos_jogo: Optional[Decimal] = Field(None, max_digits=4, decimal_places=2, ge=0)
    aproveitamento_ataque: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_passe: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    aproveitamento_levantamento: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2, ge=0)
    alcance_ataque: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)
    alcance_block: Optional[Decimal] = Field(None, max_digits=3, decimal_places=2, ge=0)

#schemas posição do atleta
class AtletaPosicao(BaseModel):
    #leitura da relação entre atleta e posição
    id_atleta: int
    nome_posicao: PosicaoVoleiEnum

class AtletaPosicaoCreate(BaseModel):
    #criar a junção do atleta com a posição
    id_atleta: int
    nome_posicao: PosicaoVoleiEnum

class AtletaPosicaoUpdate(BaseModel):
    #atualizar a posição de um atleta
    nome_posicao: Optional[PosicaoVoleiEnum] = None

#schemas para avaliação
class Avaliacao(BaseModel):
    #leitura de uma avaliação
    id_avaliacao: int
    id_atleta: int
    id_usuario: int
    data: date
    comentario: Optional[str] = None
    nota_tecnica: Optional[int] = None
    nota: Optional[int] = None

class AvaliacaoCreate(BaseModel):
    #criar uma nova avaliação
    id_atleta: int
    id_usuario: int
    data: date
    comentario: Optional[str] = None
    nota_tecnica: int = Field(..., ge=1, le=10)
    nota: int = Field(..., ge=1, le=10)
    
class AvaliacaoUpdate(BaseModel):
    #atualizar uma avaliação existente
    data: Optional[date] = None
    comentario: Optional[str] = None
    nota_tecnica: Optional[int] = Field(None, ge=1, le=10)
    nota: Optional[int] = Field(None, ge=1, le=10)