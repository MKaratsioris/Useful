from data_structures.single_linked_list import SingleLinkedList
import pytest

@pytest.fixture
def linked_list():
    return SingleLinkedList()

