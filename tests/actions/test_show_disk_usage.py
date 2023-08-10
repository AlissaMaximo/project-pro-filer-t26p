from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_hundred_show_disk_usage(capsys, tmp_path):
    aranarumey = tmp_path / "aranarumey.txt"
    non_utaite = tmp_path / "non_utaite.txt"

    aranarumey.write_text("araki nqrse meychan")
    aranarumey.touch()
    non_utaite.touch()

    context = {"all_files": [str(aranarumey), str(non_utaite)]}

    show_disk_usage(context)

    correct = (
        f"'{_get_printable_file_path(str(aranarumey))}':".ljust(70)
        + " 19 (100%)\n"
        f"'{_get_printable_file_path(str(non_utaite))}':".ljust(70)
        + "        0 (0%)\n"
        "Total size: 19"
    )

    assert capsys.readouterr().out.strip() == correct


def test_zero_show_disk_usage(capsys):
    context = {"all_files": []}

    show_disk_usage(context)

    assert "Total size: 0" == capsys.readouterr().out.strip()
