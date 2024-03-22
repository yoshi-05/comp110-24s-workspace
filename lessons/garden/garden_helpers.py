"""Some functions for my garden plan!"""

__author__ = "730671788"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind."""
    if new_plant_kind in by_kind:
        by_kind[new_plant_kind].append(new_plant)
    else:
        by_kind[new_plant_kind] = [new_plant]


def add_by_date(by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds!"""
    if month in by_date:
        by_date[month].append(plant)
    else:
        by_date[month] = [plant]


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return String with Lists of Plants of a specific kind to plant in a specific month!"""
    assert kind in plants_by_kind
    assert month in plants_by_date
    kind_list: list[str] = plants_by_kind[kind]
    month_list: list[str] = plants_by_date[month]
    combined__list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant: 
                combined__list.append(plant)
    if len(combined__list) > 0:
        return f"{kind}s to plant in {month}: {combined__list}"
    else:
        return f"No {kind}s to plant in {month}."