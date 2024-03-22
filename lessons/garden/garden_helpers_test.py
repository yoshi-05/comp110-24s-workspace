"""Test my garden functions."""

__author__ = "730671788"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind() -> None:
    """Use Case!"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    new_plant_kind: str = "flower"
    new_plant: str = "daisy"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {'flower': ['marigold', 'zinnia', 'daisy'], 'vegetable': ['carrots']}


def test_add_new_by_kind() -> None:
    """Edge Case!"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    new_plant_kind: str = "fruit"
    new_plant: str = "banana"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots'], 'fruit': ['banana']}


def test_add_by_date() -> None:
    """Use Case!"""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    month: str = "April"
    plant: str = "daisy"
    add_by_date(by_date, month, plant)
    assert by_date == {"April": ["marigold", "daisy"], "June": ["carrots"]}


def test_add_new_by_date() -> None:
    """Edge Case!"""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    month: str = "July"
    plant: str = "rose"
    add_by_date(by_date, month, plant)
    assert by_date == {"April": ["marigold"], "June": ["carrots"], "July": ["rose"]}


def test_lookup_by_kind_and_date() -> None:
    """Use case!"""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]} 
    kind: str = "vegetable"
    month: str = "June"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    expected_result: str = "vegetables to plant in June: ['carrots']"
    assert result == expected_result


def test__edge_lookup_by_kind_and_date() -> None:
    """Edge case!"""
    plants_by_kind: dict[str, list[str]] = {"flower": ["zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]} 
    kind: str = "flower"
    month: str = "April"
    result__ = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    assert result__ == f"No {kind}s to plant in {month}."