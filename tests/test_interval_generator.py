from pytest import mark
from src.interval_generator.interval_generator import (
    is_flat,
    is_sharp,
    interval_number_from_c4,
    interval_number_between,
    harmonic_distance_from_c4,
    harmonic_distance_between,
    interval_between,
)


@mark.parametrize(
    "test_note,expected",
    [("af", True), ("a", False), ("b", False), ("bf", True), ("bs", False)],
)
def test_is_flat(test_note, expected):
    assert is_flat(test_note) == expected


@mark.parametrize(
    "test_note,expected",
    [("af", False), ("a", False), ("b", False), ("bf", False), ("bs", True)],
)
def test_is_sharp(test_note, expected):
    assert is_sharp(test_note) == expected


@mark.parametrize(
    "test_note,expected",
    [
        ("c", 1),
        ("d", 2),
        ("ef", 3),
        ("fs", 4),
        ("g", 5),
        ("af", 6),
        ("bs", 7),
        ("c'", 8),
        ("d'", 9),
        ("fb'", 11),
        ("as'", 13),
        ("c''", 15),
    ],
)
def test_interval_number_from_c4(test_note, expected):
    assert interval_number_from_c4(test_note) == expected


@mark.parametrize(
    "test_note1,test_note2,expected",
    [
        ("cf", "cs", 1),
        ("c", "c", 1),
        ("c", "c'", 8),
        ("c", "c''", 15),
        ("d", "d", 1),
        ("ef", "c'", 6),
        ("c'", "ef", -6),
        ("d", "c", -2),
    ],
)
def test_interval_number_between(test_note1, test_note2, expected):
    assert interval_number_between(test_note1, test_note2) == expected


@mark.parametrize(
    "test_note,expected",
    [
        ("c", 0),
        ("d", 2),
        ("e", 4),
        ("f", 5),
        ("fs", 6),
        ("ff", 4),
        ("c'", 12),
        ("c'''", 36),
        ("d'''", 38),
    ],
)
def test_harmonic_distance_from_c4(test_note, expected):
    assert harmonic_distance_from_c4(test_note) == expected


@mark.parametrize(
    "test_note1,test_note2,expected",
    [
        ("c", "c", 0),
        ("c", "d", 2),
        ("d", "d'", 12),
        ("d'", "d", -12),
        ("e", "f", 1),
        ("d", "c", -2),
    ],
)
def test_harmonic_distance_between(test_note1, test_note2, expected):
    assert harmonic_distance_between(test_note1, test_note2) == expected


@mark.parametrize(
    "test_note1,test_note2,expected",
    [
        ("c", "c", "P1"),
        ("c", "d", "M2"),
        ("c", "df", "m2"),
        ("cs", "d", "m2"),
        ("c'", "c''", "P8"),
        ("c'", "c''", "P8"),
        ("c", "d'", "M9"),
        ("cf", "d'", "A9"),
        ("d'", "cf", "-A9"),
        ("d", "c", "-M2"),
    ],
)
def test_interval_between(test_note1, test_note2, expected):
    assert interval_between(test_note1, test_note2) == expected
