#include "ImGuizmoPure/ImGradientPure.h"

#include <vector>

namespace ImGradient
{
    size_t DelegateStl::GetPointCount()
    {
        return GetPointsList().size();
    }

    ImVec4* DelegateStl::GetPoints()
    {
        return GetPointsList().data();
    }

    Editable<int> EditPure(DelegateStl& delegate, const ImVec2& size)
   {
        int selection;
        bool edited = Edit(delegate, size, selection);
        return Editable(selection, edited);
   }
}
