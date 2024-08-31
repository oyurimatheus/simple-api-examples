from uuid import uuid4
from enum import Enum
from pydantic import BaseModel

class Status(Enum):
    TODO = 1
    DOING = 2
    DONE = 3


class Todo:
    def __init__(self, title, items=(), status=Status.TODO, observations=None):
        self.id = uuid4()
        self.__title = title
        self.__items = items
        self.__status = status
        self.__observations = observations

    @property
    def is_completed(self) -> bool:
        if len(self.__items) > 0:
            return all([todo.is_completed for todo in self.__items])

        return self.__status == Status.DONE

    def complete(self, item_id=None):
        if item_id is None:
            self.__status = Status.DONE
            for item in self.__items:
                item.__status = Status.DONE
            return

        if len(self.__items) == 0:
            self.__status = Status.DONE

        for item in self.__items:
            if item.id == item_id:
                item.__status = Status.DONE

    def __str__(self):
        return f'<class Todo>: id: {self.id}, title: {self.__title}'

    def __repr__(self):
        return f'<class Todo>: id: {self.id}, title: {self.__title}'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.__title,
            'status': self.__status,
            'observations': self.__observations,
            'items': [item.to_dict() for item in self.__items or []]
        }

