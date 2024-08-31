from typing import Union, Annotated

from fastapi import FastAPI
from pydantic import BaseModel

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from python_simple_api.models import Status, Todo

app = FastAPI()

todos_list = list()

class TodoRequest(BaseModel):
    title: str
    items: Union[list['TodoRequest'], None] = None
    status: Status = Status.TODO
    observations: Union[str, None] = None

    def to_model(self):
        sub_items = [item.to_model() for item in self.items or []]
        return Todo(self.title, sub_items, self.status, self.observations)

@app.get("/todos")
async def todos():
    return [todo.to_dict() for todo in todos_list]

@app.post("/todos")
async def todos(new_todo: TodoRequest):
    todo = new_todo.to_model()

    todos_list.append(todo)

    return todo.to_dict()

FastAPIInstrumentor.instrument_app(app)