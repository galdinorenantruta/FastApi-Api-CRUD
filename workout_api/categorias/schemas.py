from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, UUID4
from typing import Annotated


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Categoria do atleta', example='luta', max_length=15)]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='identificador da categoria')]