from pro_filer.actions.main_actions import show_details  # NOQA
import datetime
import os

# Req4


def test_inexistent_show_details(capsys):  # Terceiro ponto
    context = {"base_path": "inochi.jpg"}

    show_details(context)

    assert (
        capsys.readouterr().out.strip() == "File 'inochi.jpg' does not exist"
    )


def test_existing_show_details(capsys, tmp_path):  # Quinto ponto
    mafuko_file = tmp_path / "mafuko.txt"

    mafuko_file.touch()

    context = {"base_path": str(mafuko_file)}

    show_details(context)

    mafuko_file_size = os.path.getsize(mafuko_file)
    ready_date = datetime.datetime.fromtimestamp(
        os.path.getmtime(mafuko_file)
    ).strftime("%Y-%m-%d")
    correct_data = (
        "File name: mafuko.txt\n"
        f"File size in bytes: {mafuko_file_size}\n"
        "File type: file\n"
        "File extension: .txt\n"
        f"Last modified date: {ready_date}\n"
    )

    assert capsys.readouterr().out == correct_data


def test_existing_no_ext_show_details(capsys, tmp_path):  # Quarto ponto
    soraruko_file = tmp_path / "soraruko"

    soraruko_file.touch()

    context = {"base_path": str(soraruko_file)}

    show_details(context)

    soraruko_file_size = os.path.getsize(soraruko_file)
    ready_date = datetime.datetime.fromtimestamp(
        os.path.getmtime(soraruko_file)
    ).strftime("%Y-%m-%d")
    correct_data = (
        "File name: soraruko\n"
        f"File size in bytes: {soraruko_file_size}\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {ready_date}\n"
    )

    assert capsys.readouterr().out == correct_data
