import pytest

from university.database import get_session
from university import tables


@pytest.fixture
def create_fake_group():
    session = get_session().__next__()
    fake_data = {
        "number": 777
    }
    group = tables.Group(**fake_data)
    session.add(group)
    session.commit()
    yield group
    session = get_session().__next__()
    test_group = session.query(tables.Group).filter_by(id=group.id).first()
    session.delete(test_group)
    session.commit()


@pytest.fixture
def create_fake_lecture(create_fake_group):
    session = get_session().__next__()
    fake_dict = {
        "date": "2021-11-01",
        "lesson": "biology",
        "group_id": create_fake_group.id,
    }
    lecture = tables.Lecture(**fake_dict)
    session.add(lecture)
    session.commit()
    yield lecture
    session = get_session().__next__()
    test_lecture = session.query(tables.Lecture).filter_by(id=lecture.id).first()
    session.delete(test_lecture)
    session.commit()
