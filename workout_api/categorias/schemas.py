from workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Categoria do atleta', example='luta', max_length=15)]