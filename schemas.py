from pydantic import BaseModel, Field


class ExampleSchema(BaseModel):
    _id: int = Field(
        title="идентификатор пользователей ТГ бота",
        example=1
    )
    first_name: str | None = Field(
        title='Имя',
        example='Иван',
        default="не указано"
    )
