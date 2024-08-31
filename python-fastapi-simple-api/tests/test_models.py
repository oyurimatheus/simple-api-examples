from python_simple_api.models import Todo


def test_should_complete_a_todo_item():
    todo = Todo('Buy milk')
    todo.complete()

    assert todo.is_completed is True


def test_should_not_complete_a_todo_item_when_its_subitems_are_not_all_completed():
    milk = Todo('Buy milk')
    eggs = Todo('Buy eggs')

    groceries = Todo('Buy groceries', items=[milk, eggs])
    groceries.complete(milk.id)

    assert groceries.is_completed is False


def test_should_complete_a_todo_item_when_its_subitems_are_all_completes():
    milk = Todo('Buy milk')
    eggs = Todo('Buy eggs')

    groceries = Todo('Buy groceries', items=[milk, eggs])
    groceries.complete(milk.id)
    groceries.complete(eggs.id)

    assert groceries.is_completed is True


def test_should_not_create_a_task_without_any():
    milk = Todo('Buy milk')
    eggs = Todo('Buy eggs')

    groceries = Todo('Buy groceries', items=[milk, eggs])
    groceries.complete(milk.id)
    groceries.complete(eggs.id)

    assert groceries.is_completed is True
