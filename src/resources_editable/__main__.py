import importlib.resources
import os


def test_resources():
    path = importlib.resources.files("resources_editable.resources")
    assert path is not None
    assert os.path.exists(path / "foo" / "bar.yaml")


if __name__ == '__main__':
    test_resources()
