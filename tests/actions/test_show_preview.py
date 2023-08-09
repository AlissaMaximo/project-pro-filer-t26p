from pro_filer.actions.main_actions import show_preview  # NOQA


def test_empty_show_preview(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context)

    output = capsys.readouterr().out.strip("\n")

    assert output == "Found 0 files and 0 directories"


def test_under_five_show_preview(capsys):
    context = {
        "all_files": ["mafumafu.txt", "kuroneko.txt"],
        "all_dirs": ["utaite"],
    }

    show_preview(context)

    output = capsys.readouterr().out.strip("\n")

    correct = (
        "Found 2 files and 1 directories\n"
        "First 5 files: ['mafumafu.txt', 'kuroneko.txt']\n"
        "First 5 directories: ['utaite']"
    )

    assert output == correct


def test_over_five_show_preview(capsys):
    context = {
        "all_files": [
            "ado.txt",
            "soraru.txt",
            "amatsuki.txt",
            "lon.txt",
            "uratanuki.txt",
            "nanawoakari.txt",
        ],
        "all_dirs": ["utaites", "songs", "mvs", "audios", "illusts", "merch"],
    }

    show_preview(context)

    output = capsys.readouterr().out.strip("\n")

    correct = (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['ado.txt', 'soraru.txt', 'amatsuki.txt', "
        "'lon.txt', 'uratanuki.txt', 'nanawoakari.txt', ]\n"
        "First 5 directories: ['utaites', 'songs', 'mvs', "
        "'audios', 'illusts', 'merch']"
    )

    assert output == correct
