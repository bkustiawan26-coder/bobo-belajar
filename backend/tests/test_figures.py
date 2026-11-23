import pytest

from app.seed.full import figures, fig, load_grade


def test_every_lesson_has_figure_and_activity():
    for n in range(1, 10):
        pics = figures(n)
        for s in load_grade(n).SUBJECTS:
            for c in s.chapters:
                for t in c.topics:
                    pic = pics[(s.code, t.title)]
                    act = fig.activity(pic)
                    assert act["type"] == "activity" and act["ask"]


def test_activity_modes_follow_figure():
    assert fig.activity(fig.parse("flow 🌊 Laut > ☀️ Menguap > ☁️ Awan"))["mode"] == "order"
    assert fig.activity(fig.parse("compare A = satu ; dua || B = tiga"))["mode"] == "sort"
    assert fig.activity(fig.parse("table Kata | Arti ;; cat | kucing ;; dog | anjing"))["mode"] == "match"
    assert fig.activity(fig.parse("frac 3/8"))["mode"] == "color"
    assert fig.activity(fig.parse("place 4682"))["mode"] == "build"
    point = fig.activity(fig.parse("line 0..12 step 1 ; jump 2>4>6"))
    assert point["mode"] == "point" and point["target"] == 6
    pick = fig.activity(fig.parse("count 3 🍎 + 2 🍎 = 5 🍎"))
    assert pick["mode"] == "pick" and pick["options"][pick["answer"]] == "5" and len(set(pick["options"])) == len(pick["options"])
    solve = fig.activity(fig.parse("balance 2x + 3 | 11 | x = 4"))
    assert solve["options"][0] == "x = 4"


@pytest.mark.parametrize("bad", ["zzz 1", "line 0..10 step 3 ; mark 4", "frac 1/0", "venn A = 1 || B = 2", "flow satu", "icons apel ; jeruk"])
def test_invalid_figures_are_rejected(bad):
    with pytest.raises((fig.FigError, ValueError, ZeroDivisionError)):
        fig.parse(bad)
