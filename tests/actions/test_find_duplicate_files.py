import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_unique_find_duplicate_files(tmp_path):
    ado = tmp_path / "ado.txt"
    ivudot = tmp_path / "ivudot.txt"

    ado.write_text("Ado")
    ivudot.write_text("Ivudot")

    context = {"all_files": [str(ado), str(ivudot)]}

    outcome = find_duplicate_files(context)

    assert len(outcome) == 0


def test_inexistent_find_duplicate_files(tmp_path):
    uratanuki = tmp_path / "uratanuki.txt"
    non_utaite = tmp_path / "non_utaite.txt"

    uratanuki.write_text("Uratanuki")

    context = {"all_files": [str(uratanuki), str(non_utaite)]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)


def test_two_duplicate_files(tmp_path):
    manunchan_one = tmp_path / "manunchan1.txt"
    manunchan_two = tmp_path / "manunchan2.txt"

    manunchan_one.write_text("Manunchan")
    manunchan_two.write_text("Manunchan")

    context = {"all_files": [str(manunchan_two), str(manunchan_one)]}
    outcome = find_duplicate_files(context)

    assert outcome == [(str(manunchan_two), str(manunchan_one))]


def test_several_find_duplicate_files(tmp_path):
    ahonosakata = tmp_path / "ahonosakata.txt"
    senra = tmp_path / "senra.txt"
    shima = tmp_path / "shima.txt"

    ahonosakata.write_text("USSS")
    senra.write_text("USSS")
    shima.write_text("USSS")

    context = {"all_files": [str(ahonosakata), str(senra), str(shima)]}
    outcome = find_duplicate_files(context)

    assert len(outcome) == 3
    assert (ahonosakata, senra) in outcome
    assert (ahonosakata, shima) in outcome
    assert (senra, shima) in outcome
