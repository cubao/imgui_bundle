import random
from imgui_bundle import imgui, hello_imgui, imgui_md, immapp


@immapp.static(idx_fortune=0, was_populated=False)
def demo_gui():
    static = demo_gui
    fortunes = [
        "If at first you don't succeed, skydiving is not for you.",
        "You will be a winner today. Pick a fight.",
        "The world may be your oyster, but it doesn't mean you'll get its pearl.",
        "Borrow money from a pessimist, they don't expect it back.",
        "You will be hungry again in an hour.",
        "A closed mouth gathers no foot.",
        "Today, you will invent the wheel...again.",
        "If you can't convince them, confuse them.",
        "The journey of a thousand miles begins with a single step, or a really good map.",
        "You will find a pot of gold at the end of a rainbow, but it'll be someone else's.",
        "Opportunities will knock on your door, but don't worry, they'll be gone by the time you get up to answer.",
        "You will have a long and healthy life...and a very boring one.",
        "A wise man once said nothing.",
        "You will have a great day...tomorrow.",
        "The only thing constant in life is change, except for death and taxes, those are pretty constant too.",
    ]

    def add_log():
        log_level = random.choice([
            hello_imgui.LogLevel.debug, hello_imgui.LogLevel.info, hello_imgui.LogLevel.warning, hello_imgui.LogLevel.error])
        hello_imgui.log(log_level, fortunes[static.idx_fortune])
        static.idx_fortune += 1
        if static.idx_fortune >= len(fortunes):
            static.idx_fortune = 0

    if not static.was_populated:
        for _ in range(50):
            add_log()
        static.was_populated = True

    imgui_md.render_unindented(
        """
        # Graphical logger for ImGui
        This logger is adapted from [ImGuiAl](https://github.com/leiradel/ImGuiAl)
        """
    )
    if imgui.button("Add log"):
        add_log()

    imgui.separator()
    hello_imgui.log_gui()


def main():
    immapp.run(demo_gui, "Log")


if __name__ == "__main__":
    main()
