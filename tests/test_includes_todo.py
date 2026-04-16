from lib.includes_todo import *

def test_includes_todo_returns_true():
    result = includes_todo('hello world #TODO')
    assert result == True

def test_includes_todo_returns_false():
    result = includes_todo('hello world')
    assert result == False