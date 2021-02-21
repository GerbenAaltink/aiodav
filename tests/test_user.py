import pathlib

from aiodav.user import User


def test_user_with_constructor():
    my_user = User(username="user 1", password="user 2", root="/tmp")
    assert my_user.username == "user 1"
    assert my_user.password == "user 2"
    assert my_user.root == "/tmp"
    assert my_user.path == pathlib.Path("/tmp")
    assert my_user.base64 == "dXNlciAxOnVzZXIgMg=="
    assert str(my_user) == "user 1:user 2"


def test_user_without_constructor():
    my_user = User(username="another user", password="another password")
    my_user.username = "another user"
    my_user.password = "another password"
    my_user.root = "/home"

    assert my_user.username == "another user"
    assert my_user.password == "another password"
    assert my_user.root == "/home"

    assert my_user.path == pathlib.Path("/home")
    assert my_user.base64 == "YW5vdGhlciB1c2VyOmFub3RoZXIgcGFzc3dvcmQ="
    assert str(my_user) == "another user:another password"
