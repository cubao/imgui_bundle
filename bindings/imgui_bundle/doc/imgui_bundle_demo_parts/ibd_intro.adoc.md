# Introduction

## About ImGui Bundle

[ImGui Bundle](https://github.com/pthom/imgui_bundle) is a bundle for [Dear ImGui](https://github.com/ocornut/imgui), including various powerful libraries from its ecosystem. It enables to easily create ImGui applications in C++ and Python, under Windows, macOS, and Linux. It is aimed at application developers, researchers, and beginner developers who want to quickly get started.

## Batteries included

ImGui Bundle includes the following libraries:

-   [imgui](https://github.com/ocornut/imgui.git) : Dear ImGui, bloat-free Graphical User interface for C++ with minimal dependencies

-   [implot](https://github.com/epezent/implot): Immediate Mode Plotting

-   [Hello ImGui](https://github.com/pthom/hello_imgui.git): cross-platform Gui apps with the simplicity of a \"Hello World\" app

-   [ImGuizmo](https://github.com/CedricGuillemet/ImGuizmo.git): Immediate mode 3D gizmo for scene editing and other controls based on Dear ImGui

-   [ImGuiColorTextEdit](https://github.com/BalazsJako/ImGuiColorTextEdit): Colorizing text editor for ImGui

-   [imgui-node-editor](https://github.com/thedmd/imgui-node-editor): Node Editor built using Dear ImGui

-   [imgui-knobs](https://github.com/altschuler/imgui-knobs): Knobs widgets for ImGui

-   [ImFileDialog](https://github.com/pthom/ImFileDialog.git): A file dialog library for Dear ImGui

-   [portable-file-dialogs](https://github.com/samhocevar/portable-file-dialogs) Portable GUI dialogs library (C++11, single-header)

-   [imgui_md](https://github.com/mekhontsev/imgui_md.git): Markdown renderer for Dear ImGui using MD4C parser

-   [imspinner](https://github.com/dalerank/imspinner): Set of nice spinners for imgui

-   [imgui_toggle](https://github.com/cmdwtf/imgui_toggle): A toggle switch widget for Dear ImGui.

-   [ImmVision](https://github.com/pthom/immvision.git): Immediate image debugger and insights

-   [imgui_tex_inspect](https://github.com/andyborrell/imgui_tex_inspect): A texture inspector tool for Dear ImGui

-   [imgui-command-palette](https://github.com/hnOsmium0001/imgui-command-palette.git): A Sublime Text or VSCode style command palette in ImGui

A big thank you to their authors for their awesome work! === Easily port your code between python and C++

The python bindings closely mirror the original C++ API, with fully typed bindings. The original code documentation is meticulously kept inside the python stubs. See for example the documentation for [imgui](https://github.com/pthom/imgui_bundle/blob/main/bindings/imgui_bundle/imgui/__init__.pyi) , [implot](https://github.com/pthom/imgui_bundle/blob/main/bindings/imgui_bundle/implot.pyi), and [hello imgui](https://github.com/pthom/imgui_bundle/blob/main/bindings/imgui_bundle/hello_imgui.pyi)

Thanks to this, code completion in your favorite python IDE works like a charm, and porting code between Python and C++ becomes easy.
