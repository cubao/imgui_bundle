#pragma once
#include "hello_imgui/hello_imgui.h"
#include "imgui-node-editor/imgui_node_editor.h"
#include "imgui_md/imgui_md_wrapper.h"

#include <optional>

namespace ImGuiBundle
{
    using NodeEditorConfig = ax::NodeEditor::Config;

    //Helper to run a hello_imgui app for imgui_bundle:
    //
    //- if `with_markdown` or `with_markdown_options` is specified, then  the markdown context will be initialized
    //    (i.e. required fonts will be loaded)
    //- if `with_implot` is True, then a context for implot will be created/destroyed automatically
    //- if `with_node_editor` or with_node_editor_config` is specified, then a context for imgui_node_editor
    //    will be created automatically.
    // - `fpsIdle` enables to set the app FPS when it is idle (set it to 0 for maximum FPS).
    void Run(
        HelloImGui::RunnerParams& runner_params,
        bool with_implot = false,
        bool with_node_editor = false,
        const std::optional<NodeEditorConfig>& with_node_editor_config = std::nullopt,
        bool with_markdown = false,
        const std::optional<ImGuiMd::MarkdownOptions> & with_markdown_options = std::nullopt,
        float fpsIdle = 4.f,
        bool restoreLastWindowPosition=false
    );

    //Helper to run a hello_imgui app for imgui_bundle:
    //
    //- if `with_markdown` or `with_markdown_options` is specified, then  the markdown context will be initialized
    //    (i.e. required fonts will be loaded)
    //- if `with_implot` is True, then a context for implot will be created/destroyed automatically
    //- if `with_node_editor` or with_node_editor_config` is specified, then a context for imgui_node_editor
    //    will be created automatically.
    // - `fpsIdle` enables to set the app FPS when it is idle (set it to 0 for maximum FPS).
    void Run(
        const HelloImGui::VoidFunction& gui_function,
        const std::optional<ImVec2>& window_size = std::nullopt,
        const std::optional<std::string>& window_title = std::nullopt,
        bool with_implot = false,
        bool with_node_editor = false,
        const std::optional<NodeEditorConfig>& with_node_editor_config = std::nullopt,
        bool with_markdown = false,
        const std::optional<ImGuiMd::MarkdownOptions> & with_markdown_options = std::nullopt,
        float fpsIdle = 4.f,
        bool restoreLastWindowPosition=false
    );


    double ClockSeconds();

    ax::NodeEditor::EditorContext* CurrentNodeEditorContext();
}
