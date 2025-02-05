#pragma once
#include "imgui.h"
#include "ImGuizmo/ImGradient.h"
#include "ImGuizmoPure/Editable.h"

#include <vector>
#include <tuple>

namespace ImGradient
{
    struct DelegateStl: public Delegate
    {
        size_t GetPointCount() override;
        ImVec4* GetPoints() override;

        virtual std::vector<ImVec4>& GetPointsList() = 0;

        virtual ~DelegateStl() = default;
    };

    Editable<int> EditPure(DelegateStl& delegate, const ImVec2& size);
}
