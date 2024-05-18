from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description= 'nome do atleta', example='Joao', max_lengh=50)]
    cpf: Annotated[str, Field(description= 'cpf do atleta', example='18917845634', max_lengh=11)]
    idade: Annotated[int, Field(description= 'idade do atleta', example='18', max_lengh=3)]
    peso: Annotated[PositiveFloat, Field(description= 'peso do atleta', example='65.6', max_lengh=3)]
    altura: Annotated[PositiveFloat, Field(description= 'altura do atleta', example='1.78', max_lengh=3)]
    sexo: Annotated[str, Field(description= 'sexo do atleta', example='F', max_lengh=1)]
    
    
class AtletaIn(Atleta):
        pass

class AtletaOut(Atleta, OutMixin):
        pass