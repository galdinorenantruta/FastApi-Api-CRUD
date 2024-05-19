from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, UUID4
from typing import Annotated


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Centro de Treinamento do atleta', example='graice barra', max_length=25)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='av airton senna, 516, barra da tijuca / RJ', max_length=80)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Roice graice', max_length=30)]
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='nome do centro de treinamento', example= 'graice barra', max_length=30)]    
    
    
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]