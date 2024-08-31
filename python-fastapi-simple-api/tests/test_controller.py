from fastapi.testclient import TestClient

from python_simple_api.controller import app

cake_todo = {
   "title":"Cake ingredients",
   "items":[
      {
         "title":"Flour",
         "status":1,
         "observations":"double 0 type"
      },
      {
         "title":"baking powder",
         "status":1,
         "observations":"or baking soda"
      },
      {
         "title":"Strawberry",
         "status":1,
         "observations":"the fresh ones"
      },
      {
         "title":"eggs",
         "status":1
      }
   ],
   "status":1,
   "observations":"A strawberry cake"
}

client = TestClient(app)

def test_should_return_an_empty_list():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_should_create_a_new_todo_and_its_sub_items():
    response = client.post("/todos", json=cake_todo)

    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["id"] is not None
