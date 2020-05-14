import pytest
from data_structures_and_algorithms.challenges.day_5.linked_list import LinkedList


@pytest.fixture
def sample_linked_list():
    ll = LinkedList()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("orange")
    return ll


# Can successfully instantiate an empty linked list
def test_empty_list():
    ll = LinkedList()
    assert ll is not None


# Can properly insert into the linked list
def test_linked_list_insert(sample_linked_list):
    sample_linked_list.insert("kiwi")
    assert sample_linked_list.includes("kiwi")


# The head property will properly point to the first node in the linked list
def test_head(sample_linked_list):
    assert sample_linked_list.includes('apple') is True


# Can properly insert multiple nodes into the linked list
def test_linked_list_multiple_insert(sample_linked_list):
    sample_linked_list.insert("kiwi")
    sample_linked_list.insert("tomato")
    sample_linked_list.insert("grapes")
    assert sample_linked_list.includes("kiwi")
    assert sample_linked_list.includes("tomato")
    assert sample_linked_list.includes("grapes")


# Will return true when finding a value within the linked list that exists
def test_includes(sample_linked_list):
    assert sample_linked_list.includes('apple') is True


# Will return false when searching for a value in the linked list that does not exist
def test_not_includes(sample_linked_list):
    assert sample_linked_list.includes('kiwi') is False


# Can properly return a collection of all the values that exist in the linked list
def test_linked_list_str(sample_linked_list):
    assert str(sample_linked_list) == "\"{ orange } -> { banana } -> { apple } -> NULL\""
