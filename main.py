from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Label
import feedparser


def entry_text(entry: dict):
    return (
        f"{entry.title}\n"
        f"By: {entry.author}"
    )


data = feedparser.parse("./dummy.xml")
first_entry = data.entries[0]

for i in data.entries:
    print(i.title)


class CombiningLayoutsExample(App):
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="entry-list"):
                for entry in data.entries:
                    yield Label(entry_text(entry))


if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
