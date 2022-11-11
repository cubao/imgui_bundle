"""ImPlot: Immediate Mode Plotting for ImGui
Python bindings for https://github.com/epezent/implot
"""

# type: ignore
from typing import Any, Optional, Tuple
import numpy as np
import enum


from imgui_bundle.imgui import (
    ImVec2, ImVec4,
    ImGuiMouseButton,
    ImGuiModFlags,
    ImU32,
    ImDrawList,
)

ImGuiContext = Any


##################################################
#    Manually inserted code (typedefs, etc.)
##################################################

"""
//-----------------------------------------------------------------------------
// [SECTION] Enums and Types
//-----------------------------------------------------------------------------

// Forward declarations
struct ImPlotContext;             // ImPlot context (opaque struct, see implot_internal.h)

// Enums/Flags
typedef int ImAxis;                   // -> enum ImAxis_
typedef int ImPlotFlags;              // -> enum ImPlotFlags_
typedef int ImPlotAxisFlags;          // -> enum ImPlotAxisFlags_
typedef int ImPlotSubplotFlags;       // -> enum ImPlotSubplotFlags_
typedef int ImPlotLegendFlags;        // -> enum ImPlotLegendFlags_
typedef int ImPlotMouseTextFlags;     // -> enum ImPlotMouseTextFlags_
typedef int ImPlotDragToolFlags;      // -> ImPlotDragToolFlags_
typedef int ImPlotColormapScaleFlags; // -> ImPlotColormapScaleFlags_

typedef int ImPlotItemFlags;          // -> ImPlotItemFlags_
typedef int ImPlotLineFlags;          // -> ImPlotLineFlags_
typedef int ImPlotScatterFlags;       // -> ImPlotScatterFlags
typedef int ImPlotStairsFlags;        // -> ImPlotStairsFlags_
typedef int ImPlotShadedFlags;        // -> ImPlotShadedFlags_
typedef int ImPlotBarsFlags;          // -> ImPlotBarsFlags_
typedef int ImPlotBarGroupsFlags;     // -> ImPlotBarGroupsFlags_
typedef int ImPlotErrorBarsFlags;     // -> ImPlotErrorBarsFlags_
typedef int ImPlotStemsFlags;         // -> ImPlotStemsFlags_
typedef int ImPlotInfLinesFlags;      // -> ImPlotInfLinesFlags_
typedef int ImPlotPieChartFlags;      // -> ImPlotPieChartFlags_
typedef int ImPlotHeatmapFlags;       // -> ImPlotHeatmapFlags_
typedef int ImPlotHistogramFlags;     // -> ImPlotHistogramFlags_
typedef int ImPlotDigitalFlags;       // -> ImPlotDigitalFlags_
typedef int ImPlotImageFlags;         // -> ImPlotImageFlags_
typedef int ImPlotTextFlags;          // -> ImPlotTextFlags_
typedef int ImPlotDummyFlags;         // -> ImPlotDummyFlags_

typedef int ImPlotCond;               // -> enum ImPlotCond_
typedef int ImPlotCol;                // -> enum ImPlotCol_
typedef int ImPlotStyleVar;           // -> enum ImPlotStyleVar_
typedef int ImPlotScale;              // -> enum ImPlotScale_
typedef int ImPlotMarker;             // -> enum ImPlotMarker_
typedef int ImPlotColormap;           // -> enum ImPlotColormap_
typedef int ImPlotLocation;           // -> enum ImPlotLocation_
typedef int ImPlotBin;                // -> enum ImPlotBin_
"""
ImAxis = int  # -> enum ImAxis_
ImPlotFlags = int  # -> enum ImPlotFlags_
ImPlotAxisFlags = int  # -> enum ImPlotAxisFlags_
ImPlotSubplotFlags = int  # -> enum ImPlotSubplotFlags_
ImPlotLegendFlags = int  # -> enum ImPlotLegendFlags_
ImPlotMouseTextFlags = int  # -> enum ImPlotMouseTextFlags_
ImPlotDragToolFlags = int  # -> ImPlotDragToolFlags_
ImPlotColormapScaleFlags = int  # -> ImPlotColormapScaleFlags_

ImPlotItemFlags = int  # -> ImPlotItemFlags_
ImPlotLineFlags = int  # -> ImPlotLineFlags_
ImPlotScatterFlags = int  # -> ImPlotScatterFlags
ImPlotStairsFlags = int  # -> ImPlotStairsFlags_
ImPlotShadedFlags = int  # -> ImPlotShadedFlags_
ImPlotBarsFlags = int  # -> ImPlotBarsFlags_
ImPlotBarGroupsFlags = int  # -> ImPlotBarGroupsFlags_
ImPlotErrorBarsFlags = int  # -> ImPlotErrorBarsFlags_
ImPlotStemsFlags = int  # -> ImPlotStemsFlags_
ImPlotInfLinesFlags = int  # -> ImPlotInfLinesFlags_
ImPlotPieChartFlags = int  # -> ImPlotPieChartFlags_
ImPlotHeatmapFlags = int  # -> ImPlotHeatmapFlags_
ImPlotHistogramFlags = int  # -> ImPlotHistogramFlags_
ImPlotDigitalFlags = int  # -> ImPlotDigitalFlags_
ImPlotImageFlags = int  # -> ImPlotImageFlags_
ImPlotTextFlags = int  # -> ImPlotTextFlags_
ImPlotDummyFlags = int  # -> ImPlotDummyFlags_

ImPlotCond = int  # -> enum ImPlotCond_
ImPlotCol = int  # -> enum ImPlotCol_
ImPlotStyleVar = int  # -> enum ImPlotStyleVar_
ImPlotScale = int  # -> enum ImPlotScale_
ImPlotMarker = int  # -> enum ImPlotMarker_
ImPlotColormap = int  # -> enum ImPlotColormap_
ImPlotLocation = int  # -> enum ImPlotLocation_
ImPlotBin = int  # -> enum ImPlotBin_

# ImPlotContext is an opaque structure
ImPlotContext = Any
#
IMPLOT_AUTO = -1
IMPLOT_AUTO_COL = ImVec4(0, 0, 0, -1)
#
VoidPtr = Any
ImTextureID = VoidPtr


from imgui_bundle.imgui import (
    ImVec2,
    ImVec4,
    ImGuiMouseButton,
    ImGuiModFlags,
    ImU32,
    ImGuiDragDropFlags,
    ImDrawList,
    ImGuiCond_,
)

ImGuiCond_None = ImGuiCond_.none
ImGuiCond_Always = ImGuiCond_.always
ImGuiCond_Once = ImGuiCond_.once

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:implot.h>    ####################
# MIT License

# Copyright (c) 2022 Evan Pezent

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ImPlot v0.14

# Table of Contents:
#
# [SECTION] Macros and Defines
# [SECTION] Enums and Types
# [SECTION] Callbacks
# [SECTION] Contexts
# [SECTION] Begin/End Plot
# [SECTION] Begin/End Subplot
# [SECTION] Setup
# [SECTION] SetNext
# [SECTION] Plot Items
# [SECTION] Plot Tools
# [SECTION] Plot Utils
# [SECTION] Legend Utils
# [SECTION] Drag and Drop
# [SECTION] Styling
# [SECTION] Colormaps
# [SECTION] Input Mapping
# [SECTION] Miscellaneous
# [SECTION] Demo
# [SECTION] Obsolete API


#-----------------------------------------------------------------------------
# [SECTION] Macros and Defines
#-----------------------------------------------------------------------------

# Define attributes of all API symbols declarations (e.g. for DLL under Windows)
# Using ImPlot via a shared library is not recommended, because we don't guarantee
# backward nor forward ABI compatibility and also function call overhead. If you
# do use ImPlot as a DLL, be sure to call SetImGuiContext (see Miscellanous section).


#-----------------------------------------------------------------------------
# [SECTION] Enums and Types
#-----------------------------------------------------------------------------

# Forward declarations

# Enums/Flags



class ImAxis_(enum.Enum):    # implot.h:116
    """ Axis indices. The values assigned may change; NEVER hardcode these."""
    # horizontal axes
    # ImAxis_X1 = 0,     /* original C++ signature */
    x1 = enum.auto()    # (= 0)  # enabled by default
    # ImAxis_X2,         /* original C++ signature */
    x2 = enum.auto()    # (= 1)  # disabled by default
    # ImAxis_X3,         /* original C++ signature */
    x3 = enum.auto()    # (= 2)  # disabled by default
    # vertical axes
    # ImAxis_Y1,         /* original C++ signature */
    y1 = enum.auto()    # (= 3)  # enabled by default
    # ImAxis_Y2,         /* original C++ signature */
    y2 = enum.auto()    # (= 4)  # disabled by default
    # ImAxis_Y3,         /* original C++ signature */
    y3 = enum.auto()    # (= 5)  # disabled by default
    # ImAxis_COUNT    /* original C++ signature */
    # }
    # bookeeping
    count = enum.auto() # (= 6)

class ImPlotFlags_(enum.Enum):    # implot.h:130
    """ Options for plots (see BeginPlot)."""
    # ImPlotFlags_None          = 0,           /* original C++ signature */
    none = enum.auto()          # (= 0)  # default
    # ImPlotFlags_NoTitle       = 1 << 0,      /* original C++ signature */
    no_title = enum.auto()      # (= 1 << 0)  # the plot title will not be displayed (titles are also hidden if preceeded by double hashes, e.g. "##MyPlot")
    # ImPlotFlags_NoLegend      = 1 << 1,      /* original C++ signature */
    no_legend = enum.auto()     # (= 1 << 1)  # the legend will not be displayed
    # ImPlotFlags_NoMouseText   = 1 << 2,      /* original C++ signature */
    no_mouse_text = enum.auto() # (= 1 << 2)  # the mouse position, in plot coordinates, will not be displayed inside of the plot
    # ImPlotFlags_NoInputs      = 1 << 3,      /* original C++ signature */
    no_inputs = enum.auto()     # (= 1 << 3)  # the user will not be able to interact with the plot
    # ImPlotFlags_NoMenus       = 1 << 4,      /* original C++ signature */
    no_menus = enum.auto()      # (= 1 << 4)  # the user will not be able to open context menus
    # ImPlotFlags_NoBoxSelect   = 1 << 5,      /* original C++ signature */
    no_box_select = enum.auto() # (= 1 << 5)  # the user will not be able to box-select
    # ImPlotFlags_NoChild       = 1 << 6,      /* original C++ signature */
    no_child = enum.auto()      # (= 1 << 6)  # a child window region will not be used to capture mouse scroll (can boost performance for single ImGui window applications)
    # ImPlotFlags_NoFrame       = 1 << 7,      /* original C++ signature */
    no_frame = enum.auto()      # (= 1 << 7)  # the ImGui frame will not be rendered
    # ImPlotFlags_Equal         = 1 << 8,      /* original C++ signature */
    equal = enum.auto()         # (= 1 << 8)  # x and y axes pairs will be constrained to have the same units/pixel
    # ImPlotFlags_Crosshairs    = 1 << 9,      /* original C++ signature */
    crosshairs = enum.auto()    # (= 1 << 9)  # the default mouse cursor will be replaced with a crosshair when hovered
    # ImPlotFlags_CanvasOnly    = ImPlotFlags_NoTitle | ImPlotFlags_NoLegend | ImPlotFlags_NoMenus | ImPlotFlags_NoBoxSelect | ImPlotFlags_NoMouseText    /* original C++ signature */
    # }
    canvas_only = enum.auto()   # (= ImPlotFlags_.no_title | ImPlotFlags_.no_legend | ImPlotFlags_.no_menus | ImPlotFlags_.no_box_select | ImPlotFlags_.no_mouse_text)

class ImPlotAxisFlags_(enum.Enum):    # implot.h:146
    """ Options for plot axes (see SetupAxis)."""
    # ImPlotAxisFlags_None          = 0,           /* original C++ signature */
    none = enum.auto()           # (= 0)  # default
    # ImPlotAxisFlags_NoLabel       = 1 << 0,      /* original C++ signature */
    no_label = enum.auto()       # (= 1 << 0)  # the axis label will not be displayed (axis labels are also hidden if the supplied string name is None)
    # ImPlotAxisFlags_NoGridLines   = 1 << 1,      /* original C++ signature */
    no_grid_lines = enum.auto()  # (= 1 << 1)  # no grid lines will be displayed
    # ImPlotAxisFlags_NoTickMarks   = 1 << 2,      /* original C++ signature */
    no_tick_marks = enum.auto()  # (= 1 << 2)  # no tick marks will be displayed
    # ImPlotAxisFlags_NoTickLabels  = 1 << 3,      /* original C++ signature */
    no_tick_labels = enum.auto() # (= 1 << 3)  # no text labels will be displayed
    # ImPlotAxisFlags_NoInitialFit  = 1 << 4,      /* original C++ signature */
    no_initial_fit = enum.auto() # (= 1 << 4)  # axis will not be initially fit to data extents on the first rendered frame
    # ImPlotAxisFlags_NoMenus       = 1 << 5,      /* original C++ signature */
    no_menus = enum.auto()       # (= 1 << 5)  # the user will not be able to open context menus with right-click
    # ImPlotAxisFlags_NoSideSwitch  = 1 << 6,      /* original C++ signature */
    no_side_switch = enum.auto() # (= 1 << 6)  # the user will not be able to switch the axis side by dragging it
    # ImPlotAxisFlags_NoHighlight   = 1 << 7,      /* original C++ signature */
    no_highlight = enum.auto()   # (= 1 << 7)  # the axis will not have its background highlighted when hovered or held
    # ImPlotAxisFlags_Opposite      = 1 << 8,      /* original C++ signature */
    opposite = enum.auto()       # (= 1 << 8)  # axis ticks and labels will be rendered on the conventionally opposite side (i.e, right or top)
    # ImPlotAxisFlags_Foreground    = 1 << 9,      /* original C++ signature */
    foreground = enum.auto()     # (= 1 << 9)  # grid lines will be displayed in the foreground (i.e. on top of data) instead of the background
    # ImPlotAxisFlags_Invert        = 1 << 10,     /* original C++ signature */
    invert = enum.auto()         # (= 1 << 10)  # the axis will be inverted
    # ImPlotAxisFlags_AutoFit       = 1 << 11,     /* original C++ signature */
    auto_fit = enum.auto()       # (= 1 << 11)  # axis will be auto-fitting to data extents
    # ImPlotAxisFlags_RangeFit      = 1 << 12,     /* original C++ signature */
    range_fit = enum.auto()      # (= 1 << 12)  # axis will only fit points if the point is in the visible range of the **orthogonal** axis
    # ImPlotAxisFlags_PanStretch    = 1 << 13,     /* original C++ signature */
    pan_stretch = enum.auto()    # (= 1 << 13)  # panning in a locked or constrained state will cause the axis to stretch if possible
    # ImPlotAxisFlags_LockMin       = 1 << 14,     /* original C++ signature */
    lock_min = enum.auto()       # (= 1 << 14)  # the axis minimum value will be locked when panning/zooming
    # ImPlotAxisFlags_LockMax       = 1 << 15,     /* original C++ signature */
    lock_max = enum.auto()       # (= 1 << 15)  # the axis maximum value will be locked when panning/zooming
    # ImPlotAxisFlags_Lock          = ImPlotAxisFlags_LockMin | ImPlotAxisFlags_LockMax,    /* original C++ signature */
    lock = enum.auto()           # (= ImPlotAxisFlags_.lock_min | ImPlotAxisFlags_.lock_max)
    # ImPlotAxisFlags_NoDecorations = ImPlotAxisFlags_NoLabel | ImPlotAxisFlags_NoGridLines | ImPlotAxisFlags_NoTickMarks | ImPlotAxisFlags_NoTickLabels,    /* original C++ signature */
    no_decorations = enum.auto() # (= ImPlotAxisFlags_.no_label | ImPlotAxisFlags_.no_grid_lines | ImPlotAxisFlags_.no_tick_marks | ImPlotAxisFlags_.no_tick_labels)
    # ImPlotAxisFlags_AuxDefault    = ImPlotAxisFlags_NoGridLines | ImPlotAxisFlags_Opposite    /* original C++ signature */
    # }
    aux_default = enum.auto()    # (= ImPlotAxisFlags_.no_grid_lines | ImPlotAxisFlags_.opposite)

class ImPlotSubplotFlags_(enum.Enum):    # implot.h:170
    """ Options for subplots (see BeginSubplot)"""
    # ImPlotSubplotFlags_None        = 0,           /* original C++ signature */
    none = enum.auto()        # (= 0)  # default
    # ImPlotSubplotFlags_NoTitle     = 1 << 0,      /* original C++ signature */
    no_title = enum.auto()    # (= 1 << 0)  # the subplot title will not be displayed (titles are also hidden if preceeded by double hashes, e.g. "##MySubplot")
    # ImPlotSubplotFlags_NoLegend    = 1 << 1,      /* original C++ signature */
    no_legend = enum.auto()   # (= 1 << 1)  # the legend will not be displayed (only applicable if ImPlotSubplotFlags_ShareItems is enabled)
    # ImPlotSubplotFlags_NoMenus     = 1 << 2,      /* original C++ signature */
    no_menus = enum.auto()    # (= 1 << 2)  # the user will not be able to open context menus with right-click
    # ImPlotSubplotFlags_NoResize    = 1 << 3,      /* original C++ signature */
    no_resize = enum.auto()   # (= 1 << 3)  # resize splitters between subplot cells will be not be provided
    # ImPlotSubplotFlags_NoAlign     = 1 << 4,      /* original C++ signature */
    no_align = enum.auto()    # (= 1 << 4)  # subplot edges will not be aligned vertically or horizontally
    # ImPlotSubplotFlags_ShareItems  = 1 << 5,      /* original C++ signature */
    share_items = enum.auto() # (= 1 << 5)  # items across all subplots will be shared and rendered into a single legend entry
    # ImPlotSubplotFlags_LinkRows    = 1 << 6,      /* original C++ signature */
    link_rows = enum.auto()   # (= 1 << 6)  # link the y-axis limits of all plots in each row (does not apply to auxiliary axes)
    # ImPlotSubplotFlags_LinkCols    = 1 << 7,      /* original C++ signature */
    link_cols = enum.auto()   # (= 1 << 7)  # link the x-axis limits of all plots in each column (does not apply to auxiliary axes)
    # ImPlotSubplotFlags_LinkAllX    = 1 << 8,      /* original C++ signature */
    link_all_x = enum.auto()  # (= 1 << 8)  # link the x-axis limits in every plot in the subplot (does not apply to auxiliary axes)
    # ImPlotSubplotFlags_LinkAllY    = 1 << 9,      /* original C++ signature */
    link_all_y = enum.auto()  # (= 1 << 9)  # link the y-axis limits in every plot in the subplot (does not apply to auxiliary axes)
    # ImPlotSubplotFlags_ColMajor    = 1 << 10      /* original C++ signature */
    col_major = enum.auto()   # (= 1 << 10)  # subplots are added in column major order instead of the default row major order

class ImPlotLegendFlags_(enum.Enum):    # implot.h:186
    """ Options for legends (see SetupLegend)"""
    # ImPlotLegendFlags_None            = 0,          /* original C++ signature */
    none = enum.auto()              # (= 0)  # default
    # ImPlotLegendFlags_NoButtons       = 1 << 0,     /* original C++ signature */
    no_buttons = enum.auto()        # (= 1 << 0)  # legend icons will not function as hide/show buttons
    # ImPlotLegendFlags_NoHighlightItem = 1 << 1,     /* original C++ signature */
    no_highlight_item = enum.auto() # (= 1 << 1)  # plot items will not be highlighted when their legend entry is hovered
    # ImPlotLegendFlags_NoHighlightAxis = 1 << 2,     /* original C++ signature */
    no_highlight_axis = enum.auto() # (= 1 << 2)  # axes will not be highlighted when legend entries are hovered (only relevant if x/y-axis count > 1)
    # ImPlotLegendFlags_NoMenus         = 1 << 3,     /* original C++ signature */
    no_menus = enum.auto()          # (= 1 << 3)  # the user will not be able to open context menus with right-click
    # ImPlotLegendFlags_Outside         = 1 << 4,     /* original C++ signature */
    outside = enum.auto()           # (= 1 << 4)  # legend will be rendered outside of the plot area
    # ImPlotLegendFlags_Horizontal      = 1 << 5,     /* original C++ signature */
    horizontal = enum.auto()        # (= 1 << 5)  # legend entries will be displayed horizontally

class ImPlotMouseTextFlags_(enum.Enum):    # implot.h:197
    """ Options for mouse hover text (see SetupMouseText)"""
    # ImPlotMouseTextFlags_None        = 0,          /* original C++ signature */
    none = enum.auto()        # (= 0)  # default
    # ImPlotMouseTextFlags_NoAuxAxes   = 1 << 0,     /* original C++ signature */
    no_aux_axes = enum.auto() # (= 1 << 0)  # only show the mouse position for primary axes
    # ImPlotMouseTextFlags_NoFormat    = 1 << 1,     /* original C++ signature */
    no_format = enum.auto()   # (= 1 << 1)  # axes label formatters won't be used to render text
    # ImPlotMouseTextFlags_ShowAlways  = 1 << 2,     /* original C++ signature */
    show_always = enum.auto() # (= 1 << 2)  # always display mouse position even if plot not hovered

class ImPlotDragToolFlags_(enum.Enum):    # implot.h:205
    """ Options for DragPoint, DragLine, DragRect"""
    # ImPlotDragToolFlags_None      = 0,          /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotDragToolFlags_NoCursors = 1 << 0,     /* original C++ signature */
    no_cursors = enum.auto() # (= 1 << 0)  # drag tools won't change cursor icons when hovered or held
    # ImPlotDragToolFlags_NoFit     = 1 << 1,     /* original C++ signature */
    no_fit = enum.auto()     # (= 1 << 1)  # the drag tool won't be considered for plot fits
    # ImPlotDragToolFlags_NoInputs  = 1 << 2,     /* original C++ signature */
    no_inputs = enum.auto()  # (= 1 << 2)  # lock the tool from user inputs
    # ImPlotDragToolFlags_Delayed   = 1 << 3,     /* original C++ signature */
    delayed = enum.auto()    # (= 1 << 3)  # tool rendering will be delayed one frame; useful when applying position-constraints

class ImPlotColormapScaleFlags_(enum.Enum):    # implot.h:214
    """ Flags for ColormapScale"""
    # ImPlotColormapScaleFlags_None     = 0,          /* original C++ signature */
    none = enum.auto()     # (= 0)  # default
    # ImPlotColormapScaleFlags_NoLabel  = 1 << 0,     /* original C++ signature */
    no_label = enum.auto() # (= 1 << 0)  # the colormap axis label will not be displayed
    # ImPlotColormapScaleFlags_Opposite = 1 << 1,     /* original C++ signature */
    opposite = enum.auto() # (= 1 << 1)  # render the colormap label and tick labels on the opposite side
    # ImPlotColormapScaleFlags_Invert   = 1 << 2,     /* original C++ signature */
    invert = enum.auto()   # (= 1 << 2)  # invert the colormap bar and axis scale (this only affects rendering; if you only want to reverse the scale mapping, make scale_min > scale_max)

class ImPlotItemFlags_(enum.Enum):    # implot.h:222
    """ Flags for ANY PlotX function"""
    # ImPlotItemFlags_None     = 0,    /* original C++ signature */
    none = enum.auto()      # (= 0)
    # ImPlotItemFlags_NoLegend = 1 << 0,     /* original C++ signature */
    no_legend = enum.auto() # (= 1 << 0)  # the item won't have a legend entry displayed
    # ImPlotItemFlags_NoFit    = 1 << 1,     /* original C++ signature */
    no_fit = enum.auto()    # (= 1 << 1)  # the item won't be considered for plot fits

class ImPlotLineFlags_(enum.Enum):    # implot.h:229
    """ Flags for PlotLine"""
    # ImPlotLineFlags_None        = 0,           /* original C++ signature */
    none = enum.auto()      # (= 0)  # default
    # ImPlotLineFlags_Segments    = 1 << 10,     /* original C++ signature */
    segments = enum.auto()  # (= 1 << 10)  # a line segment will be rendered from every two consecutive points
    # ImPlotLineFlags_Loop        = 1 << 11,     /* original C++ signature */
    loop = enum.auto()      # (= 1 << 11)  # the last and first point will be connected to form a closed loop
    # ImPlotLineFlags_SkipNaN     = 1 << 12,     /* original C++ signature */
    skip_na_n = enum.auto() # (= 1 << 12)  # NaNs values will be skipped instead of rendered as missing data
    # ImPlotLineFlags_NoClip      = 1 << 13,     /* original C++ signature */
    no_clip = enum.auto()   # (= 1 << 13)  # markers (if displayed) on the edge of a plot will not be clipped
    # ImPlotLineFlags_Shaded      = 1 << 14,     /* original C++ signature */
    shaded = enum.auto()    # (= 1 << 14)  # a filled region between the line and horizontal origin will be rendered; use PlotShaded for more advanced cases

class ImPlotScatterFlags_(enum.Enum):    # implot.h:239
    """ Flags for PlotScatter"""
    # ImPlotScatterFlags_None   = 0,           /* original C++ signature */
    none = enum.auto()    # (= 0)  # default
    # ImPlotScatterFlags_NoClip = 1 << 10,     /* original C++ signature */
    no_clip = enum.auto() # (= 1 << 10)  # markers on the edge of a plot will not be clipped

class ImPlotStairsFlags_(enum.Enum):    # implot.h:245
    """ Flags for PlotStairs"""
    # ImPlotStairsFlags_None     = 0,           /* original C++ signature */
    none = enum.auto()     # (= 0)  # default
    # ImPlotStairsFlags_PreStep  = 1 << 10,     /* original C++ signature */
    pre_step = enum.auto() # (= 1 << 10)  # the y value is continued constantly to the left from every x position, i.e. the interval (x[i-1], x[i]] has the value y[i]
    # ImPlotStairsFlags_Shaded   = 1 << 11      /* original C++ signature */
    shaded = enum.auto()   # (= 1 << 11)  # a filled region between the stairs and horizontal origin will be rendered; use PlotShaded for more advanced cases

class ImPlotShadedFlags_(enum.Enum):    # implot.h:252
    """ Flags for PlotShaded (placeholder)"""
    # ImPlotShadedFlags_None  = 0     /* original C++ signature */
    none = enum.auto() # (= 0)  # default

class ImPlotBarsFlags_(enum.Enum):    # implot.h:257
    """ Flags for PlotBars"""
    # ImPlotBarsFlags_None         = 0,           /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotBarsFlags_Horizontal   = 1 << 10,     /* original C++ signature */
    horizontal = enum.auto() # (= 1 << 10)  # bars will be rendered horizontally on the current y-axis

class ImPlotBarGroupsFlags_(enum.Enum):    # implot.h:263
    """ Flags for PlotBarGroups"""
    # ImPlotBarGroupsFlags_None        = 0,           /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotBarGroupsFlags_Horizontal  = 1 << 10,     /* original C++ signature */
    horizontal = enum.auto() # (= 1 << 10)  # bar groups will be rendered horizontally on the current y-axis
    # ImPlotBarGroupsFlags_Stacked     = 1 << 11,     /* original C++ signature */
    stacked = enum.auto()    # (= 1 << 11)  # items in a group will be stacked on top of each other

class ImPlotErrorBarsFlags_(enum.Enum):    # implot.h:270
    """ Flags for PlotErrorBars"""
    # ImPlotErrorBarsFlags_None       = 0,           /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotErrorBarsFlags_Horizontal = 1 << 10,     /* original C++ signature */
    horizontal = enum.auto() # (= 1 << 10)  # error bars will be rendered horizontally on the current y-axis

class ImPlotStemsFlags_(enum.Enum):    # implot.h:276
    """ Flags for PlotStems"""
    # ImPlotStemsFlags_None       = 0,           /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotStemsFlags_Horizontal = 1 << 10,     /* original C++ signature */
    horizontal = enum.auto() # (= 1 << 10)  # stems will be rendered horizontally on the current y-axis

class ImPlotInfLinesFlags_(enum.Enum):    # implot.h:282
    """ Flags for PlotInfLines"""
    # ImPlotInfLinesFlags_None       = 0,          /* original C++ signature */
    none = enum.auto()       # (= 0)  # default
    # ImPlotInfLinesFlags_Horizontal = 1 << 10     /* original C++ signature */
    horizontal = enum.auto() # (= 1 << 10)  # lines will be rendered horizontally on the current y-axis

class ImPlotPieChartFlags_(enum.Enum):    # implot.h:288
    """ Flags for PlotPieChart"""
    # ImPlotPieChartFlags_None      = 0,          /* original C++ signature */
    none = enum.auto()      # (= 0)  # default
    # ImPlotPieChartFlags_Normalize = 1 << 10     /* original C++ signature */
    normalize = enum.auto() # (= 1 << 10)  # force normalization of pie chart values (i.e. always make a full circle if sum < 0)

class ImPlotHeatmapFlags_(enum.Enum):    # implot.h:294
    """ Flags for PlotHeatmap"""
    # ImPlotHeatmapFlags_None     = 0,           /* original C++ signature */
    none = enum.auto()      # (= 0)  # default
    # ImPlotHeatmapFlags_ColMajor = 1 << 10,     /* original C++ signature */
    col_major = enum.auto() # (= 1 << 10)  # data will be read in column major order

class ImPlotHistogramFlags_(enum.Enum):    # implot.h:300
    """ Flags for PlotHistogram and PlotHistogram2D"""
    # ImPlotHistogramFlags_None       = 0,           /* original C++ signature */
    none = enum.auto()        # (= 0)  # default
    # ImPlotHistogramFlags_Horizontal = 1 << 10,     /* original C++ signature */
    horizontal = enum.auto()  # (= 1 << 10)  # histogram bars will be rendered horizontally (not supported by PlotHistogram2D)
    # ImPlotHistogramFlags_Cumulative = 1 << 11,     /* original C++ signature */
    cumulative = enum.auto()  # (= 1 << 11)  # each bin will contain its count plus the counts of all previous bins (not supported by PlotHistogram2D)
    # ImPlotHistogramFlags_Density    = 1 << 12,     /* original C++ signature */
    density = enum.auto()     # (= 1 << 12)  # counts will be normalized, i.e. the PDF will be visualized, or the CDF will be visualized if Cumulative is also set
    # ImPlotHistogramFlags_NoOutliers = 1 << 13,     /* original C++ signature */
    no_outliers = enum.auto() # (= 1 << 13)  # exclude values outside the specifed histogram range from the count toward normalizing and cumulative counts
    # ImPlotHistogramFlags_ColMajor   = 1 << 14      /* original C++ signature */
    col_major = enum.auto()   # (= 1 << 14)  # data will be read in column major order (not supported by PlotHistogram)

class ImPlotDigitalFlags_(enum.Enum):    # implot.h:310
    """ Flags for PlotDigital (placeholder)"""
    # ImPlotDigitalFlags_None = 0     /* original C++ signature */
    none = enum.auto() # (= 0)  # default

class ImPlotImageFlags_(enum.Enum):    # implot.h:315
    """ Flags for PlotImage (placeholder)"""
    # ImPlotImageFlags_None = 0     /* original C++ signature */
    none = enum.auto() # (= 0)  # default

class ImPlotTextFlags_(enum.Enum):    # implot.h:320
    """ Flags for PlotText"""
    # ImPlotTextFlags_None     = 0,           /* original C++ signature */
    none = enum.auto()     # (= 0)  # default
    # ImPlotTextFlags_Vertical = 1 << 10      /* original C++ signature */
    vertical = enum.auto() # (= 1 << 10)  # text will be rendered vertically

class ImPlotDummyFlags_(enum.Enum):    # implot.h:326
    """ Flags for PlotDummy (placeholder)"""
    # ImPlotDummyFlags_None = 0     /* original C++ signature */
    none = enum.auto() # (= 0)  # default

class ImPlotCond_(enum.Enum):    # implot.h:331
    """ Represents a condition for SetupAxisLimits etc. (same as ImGuiCond, but we only support a subset of those enums)"""
    # ImPlotCond_None   = ImGuiCond_None,        /* original C++ signature */
    none = enum.auto()   # (= ImGuiCond_None)  # No condition (always set the variable), same as _Always
    # ImPlotCond_Always = ImGuiCond_Always,      /* original C++ signature */
    always = enum.auto() # (= ImGuiCond_Always)  # No condition (always set the variable)
    # ImPlotCond_Once   = ImGuiCond_Once,        /* original C++ signature */
    once = enum.auto()   # (= ImGuiCond_Once)  # Set the variable once per runtime session (only the first call will succeed)

class ImPlotCol_(enum.Enum):    # implot.h:339
    """ Plot styling colors."""
    # item styling colors
    # ImPlotCol_Line,              /* original C++ signature */
    line = enum.auto()            # (= 0)  # plot line/outline color (defaults to next unused color in current colormap)
    # ImPlotCol_Fill,              /* original C++ signature */
    fill = enum.auto()            # (= 1)  # plot fill color for bars (defaults to the current line color)
    # ImPlotCol_MarkerOutline,     /* original C++ signature */
    marker_outline = enum.auto()  # (= 2)  # marker outline color (defaults to the current line color)
    # ImPlotCol_MarkerFill,        /* original C++ signature */
    marker_fill = enum.auto()     # (= 3)  # marker fill color (defaults to the current line color)
    # ImPlotCol_ErrorBar,          /* original C++ signature */
    error_bar = enum.auto()       # (= 4)  # error bar color (defaults to ImGuiCol_Text)
    # plot styling colors
    # ImPlotCol_FrameBg,           /* original C++ signature */
    frame_bg = enum.auto()        # (= 5)  # plot frame background color (defaults to ImGuiCol_FrameBg)
    # ImPlotCol_PlotBg,            /* original C++ signature */
    plot_bg = enum.auto()         # (= 6)  # plot area background color (defaults to ImGuiCol_WindowBg)
    # ImPlotCol_PlotBorder,        /* original C++ signature */
    plot_border = enum.auto()     # (= 7)  # plot area border color (defaults to ImGuiCol_Border)
    # ImPlotCol_LegendBg,          /* original C++ signature */
    legend_bg = enum.auto()       # (= 8)  # legend background color (defaults to ImGuiCol_PopupBg)
    # ImPlotCol_LegendBorder,      /* original C++ signature */
    legend_border = enum.auto()   # (= 9)  # legend border color (defaults to ImPlotCol_PlotBorder)
    # ImPlotCol_LegendText,        /* original C++ signature */
    legend_text = enum.auto()     # (= 10)  # legend text color (defaults to ImPlotCol_InlayText)
    # ImPlotCol_TitleText,         /* original C++ signature */
    title_text = enum.auto()      # (= 11)  # plot title text color (defaults to ImGuiCol_Text)
    # ImPlotCol_InlayText,         /* original C++ signature */
    inlay_text = enum.auto()      # (= 12)  # color of text appearing inside of plots (defaults to ImGuiCol_Text)
    # ImPlotCol_AxisText,          /* original C++ signature */
    axis_text = enum.auto()       # (= 13)  # axis label and tick lables color (defaults to ImGuiCol_Text)
    # ImPlotCol_AxisGrid,          /* original C++ signature */
    axis_grid = enum.auto()       # (= 14)  # axis grid color (defaults to 25% ImPlotCol_AxisText)
    # ImPlotCol_AxisTick,          /* original C++ signature */
    axis_tick = enum.auto()       # (= 15)  # axis tick color (defaults to AxisGrid)
    # ImPlotCol_AxisBg,            /* original C++ signature */
    axis_bg = enum.auto()         # (= 16)  # background color of axis hover region (defaults to transparent)
    # ImPlotCol_AxisBgHovered,     /* original C++ signature */
    axis_bg_hovered = enum.auto() # (= 17)  # axis hover color (defaults to ImGuiCol_ButtonHovered)
    # ImPlotCol_AxisBgActive,      /* original C++ signature */
    axis_bg_active = enum.auto()  # (= 18)  # axis active color (defaults to ImGuiCol_ButtonActive)
    # ImPlotCol_Selection,         /* original C++ signature */
    selection = enum.auto()       # (= 19)  # box-selection color (defaults to yellow)
    # ImPlotCol_Crosshairs,        /* original C++ signature */
    crosshairs = enum.auto()      # (= 20)  # crosshairs color (defaults to ImPlotCol_PlotBorder)
    # ImPlotCol_COUNT    /* original C++ signature */
    # }
    count = enum.auto()           # (= 21)

class ImPlotStyleVar_(enum.Enum):    # implot.h:367
    """ Plot styling variables."""
    # item styling variables
    # ImPlotStyleVar_LineWeight,             /* original C++ signature */
    line_weight = enum.auto()          # (= 0)  # float,  plot item line weight in pixels
    # ImPlotStyleVar_Marker,                 /* original C++ signature */
    marker = enum.auto()               # (= 1)  # int,    marker specification
    # ImPlotStyleVar_MarkerSize,             /* original C++ signature */
    marker_size = enum.auto()          # (= 2)  # float,  marker size in pixels (roughly the marker's "radius")
    # ImPlotStyleVar_MarkerWeight,           /* original C++ signature */
    marker_weight = enum.auto()        # (= 3)  # float,  plot outline weight of markers in pixels
    # ImPlotStyleVar_FillAlpha,              /* original C++ signature */
    fill_alpha = enum.auto()           # (= 4)  # float,  alpha modifier applied to all plot item fills
    # ImPlotStyleVar_ErrorBarSize,           /* original C++ signature */
    error_bar_size = enum.auto()       # (= 5)  # float,  error bar whisker width in pixels
    # ImPlotStyleVar_ErrorBarWeight,         /* original C++ signature */
    error_bar_weight = enum.auto()     # (= 6)  # float,  error bar whisker weight in pixels
    # ImPlotStyleVar_DigitalBitHeight,       /* original C++ signature */
    digital_bit_height = enum.auto()   # (= 7)  # float,  digital channels bit height (at 1) in pixels
    # ImPlotStyleVar_DigitalBitGap,          /* original C++ signature */
    digital_bit_gap = enum.auto()      # (= 8)  # float,  digital channels bit padding gap in pixels
    # plot styling variables
    # ImPlotStyleVar_PlotBorderSize,         /* original C++ signature */
    plot_border_size = enum.auto()     # (= 9)  # float,  thickness of border around plot area
    # ImPlotStyleVar_MinorAlpha,             /* original C++ signature */
    minor_alpha = enum.auto()          # (= 10)  # float,  alpha multiplier applied to minor axis grid lines
    # ImPlotStyleVar_MajorTickLen,           /* original C++ signature */
    major_tick_len = enum.auto()       # (= 11)  # ImVec2, major tick lengths for X and Y axes
    # ImPlotStyleVar_MinorTickLen,           /* original C++ signature */
    minor_tick_len = enum.auto()       # (= 12)  # ImVec2, minor tick lengths for X and Y axes
    # ImPlotStyleVar_MajorTickSize,          /* original C++ signature */
    major_tick_size = enum.auto()      # (= 13)  # ImVec2, line thickness of major ticks
    # ImPlotStyleVar_MinorTickSize,          /* original C++ signature */
    minor_tick_size = enum.auto()      # (= 14)  # ImVec2, line thickness of minor ticks
    # ImPlotStyleVar_MajorGridSize,          /* original C++ signature */
    major_grid_size = enum.auto()      # (= 15)  # ImVec2, line thickness of major grid lines
    # ImPlotStyleVar_MinorGridSize,          /* original C++ signature */
    minor_grid_size = enum.auto()      # (= 16)  # ImVec2, line thickness of minor grid lines
    # ImPlotStyleVar_PlotPadding,            /* original C++ signature */
    plot_padding = enum.auto()         # (= 17)  # ImVec2, padding between widget frame and plot area, labels, or outside legends (i.e. main padding)
    # ImPlotStyleVar_LabelPadding,           /* original C++ signature */
    label_padding = enum.auto()        # (= 18)  # ImVec2, padding between axes labels, tick labels, and plot edge
    # ImPlotStyleVar_LegendPadding,          /* original C++ signature */
    legend_padding = enum.auto()       # (= 19)  # ImVec2, legend padding from plot edges
    # ImPlotStyleVar_LegendInnerPadding,     /* original C++ signature */
    legend_inner_padding = enum.auto() # (= 20)  # ImVec2, legend inner padding from legend edges
    # ImPlotStyleVar_LegendSpacing,          /* original C++ signature */
    legend_spacing = enum.auto()       # (= 21)  # ImVec2, spacing between legend entries
    # ImPlotStyleVar_MousePosPadding,        /* original C++ signature */
    mouse_pos_padding = enum.auto()    # (= 22)  # ImVec2, padding between plot edge and interior info text
    # ImPlotStyleVar_AnnotationPadding,      /* original C++ signature */
    annotation_padding = enum.auto()   # (= 23)  # ImVec2, text padding around annotation labels
    # ImPlotStyleVar_FitPadding,             /* original C++ signature */
    fit_padding = enum.auto()          # (= 24)  # ImVec2, additional fit padding as a percentage of the fit extents (e.g. ImVec2(0.1,0.1) adds 10% to the fit extents of X and Y)
    # ImPlotStyleVar_PlotDefaultSize,        /* original C++ signature */
    plot_default_size = enum.auto()    # (= 25)  # ImVec2, default size used when ImVec2(0,0) is passed to BeginPlot
    # ImPlotStyleVar_PlotMinSize,            /* original C++ signature */
    plot_min_size = enum.auto()        # (= 26)  # ImVec2, minimum size plot frame can be when shrunk
    # ImPlotStyleVar_COUNT    /* original C++ signature */
    # }
    count = enum.auto()                # (= 27)

class ImPlotScale_(enum.Enum):    # implot.h:401
    """ Axis scale"""
    # ImPlotScale_Linear = 0,     /* original C++ signature */
    linear = enum.auto()  # (= 0)  # default linear scale
    # ImPlotScale_Time,           /* original C++ signature */
    time = enum.auto()    # (= 1)  # date/time scale
    # ImPlotScale_Log10,          /* original C++ signature */
    log10 = enum.auto()   # (= 2)  # base 10 logartithmic scale
    # ImPlotScale_SymLog,         /* original C++ signature */
    sym_log = enum.auto() # (= 3)  # symmetric log scale

class ImPlotMarker_(enum.Enum):    # implot.h:409
    """ Marker specifications."""
    # ImPlotMarker_None = -1,     /* original C++ signature */
    none = enum.auto()     # (= -1)  # no marker
    # ImPlotMarker_Circle,        /* original C++ signature */
    circle = enum.auto()   # (= 0)  # a circle marker (default)
    # ImPlotMarker_Square,        /* original C++ signature */
    square = enum.auto()   # (= 1)  # a square maker
    # ImPlotMarker_Diamond,       /* original C++ signature */
    diamond = enum.auto()  # (= 2)  # a diamond marker
    # ImPlotMarker_Up,            /* original C++ signature */
    up = enum.auto()       # (= 3)  # an upward-pointing triangle marker
    # ImPlotMarker_Down,          /* original C++ signature */
    down = enum.auto()     # (= 4)  # an downward-pointing triangle marker
    # ImPlotMarker_Left,          /* original C++ signature */
    left = enum.auto()     # (= 5)  # an leftward-pointing triangle marker
    # ImPlotMarker_Right,         /* original C++ signature */
    right = enum.auto()    # (= 6)  # an rightward-pointing triangle marker
    # ImPlotMarker_Cross,         /* original C++ signature */
    cross = enum.auto()    # (= 7)  # a cross marker (not fillable)
    # ImPlotMarker_Plus,          /* original C++ signature */
    plus = enum.auto()     # (= 8)  # a plus marker (not fillable)
    # ImPlotMarker_Asterisk,      /* original C++ signature */
    asterisk = enum.auto() # (= 9)  # a asterisk marker (not fillable)
    # ImPlotMarker_COUNT    /* original C++ signature */
    # }
    count = enum.auto()    # (= 10)

class ImPlotColormap_(enum.Enum):    # implot.h:425
    """ Built-in colormaps"""
    # ImPlotColormap_Deep     = 0,       /* original C++ signature */
    deep = enum.auto()     # (= 0)  # a.k.a. seaborn deep             (qual=True,  n=10) (default)
    # ImPlotColormap_Dark     = 1,       /* original C++ signature */
    dark = enum.auto()     # (= 1)  # a.k.a. matplotlib "Set1"        (qual=True,  n=9 )
    # ImPlotColormap_Pastel   = 2,       /* original C++ signature */
    pastel = enum.auto()   # (= 2)  # a.k.a. matplotlib "Pastel1"     (qual=True,  n=9 )
    # ImPlotColormap_Paired   = 3,       /* original C++ signature */
    paired = enum.auto()   # (= 3)  # a.k.a. matplotlib "Paired"      (qual=True,  n=12)
    # ImPlotColormap_Viridis  = 4,       /* original C++ signature */
    viridis = enum.auto()  # (= 4)  # a.k.a. matplotlib "viridis"     (qual=False, n=11)
    # ImPlotColormap_Plasma   = 5,       /* original C++ signature */
    plasma = enum.auto()   # (= 5)  # a.k.a. matplotlib "plasma"      (qual=False, n=11)
    # ImPlotColormap_Hot      = 6,       /* original C++ signature */
    hot = enum.auto()      # (= 6)  # a.k.a. matplotlib/MATLAB "hot"  (qual=False, n=11)
    # ImPlotColormap_Cool     = 7,       /* original C++ signature */
    cool = enum.auto()     # (= 7)  # a.k.a. matplotlib/MATLAB "cool" (qual=False, n=11)
    # ImPlotColormap_Pink     = 8,       /* original C++ signature */
    pink = enum.auto()     # (= 8)  # a.k.a. matplotlib/MATLAB "pink" (qual=False, n=11)
    # ImPlotColormap_Jet      = 9,       /* original C++ signature */
    jet = enum.auto()      # (= 9)  # a.k.a. MATLAB "jet"             (qual=False, n=11)
    # ImPlotColormap_Twilight = 10,      /* original C++ signature */
    twilight = enum.auto() # (= 10)  # a.k.a. matplotlib "twilight"    (qual=False, n=11)
    # ImPlotColormap_RdBu     = 11,      /* original C++ signature */
    rd_bu = enum.auto()    # (= 11)  # red/blue, Color Brewer          (qual=False, n=11)
    # ImPlotColormap_BrBG     = 12,      /* original C++ signature */
    br_bg = enum.auto()    # (= 12)  # brown/blue-green, Color Brewer  (qual=False, n=11)
    # ImPlotColormap_PiYG     = 13,      /* original C++ signature */
    pi_yg = enum.auto()    # (= 13)  # pink/yellow-green, Color Brewer (qual=False, n=11)
    # ImPlotColormap_Spectral = 14,      /* original C++ signature */
    spectral = enum.auto() # (= 14)  # color spectrum, Color Brewer    (qual=False, n=11)
    # ImPlotColormap_Greys    = 15,      /* original C++ signature */
    greys = enum.auto()    # (= 15)  # white/black                     (qual=False, n=2 )

class ImPlotLocation_(enum.Enum):    # implot.h:445
    """ Used to position items on a plot (e.g. legends, labels, etc.)"""
    # ImPlotLocation_Center    = 0,                                              /* original C++ signature */
    center = enum.auto()     # (= 0)  # center-center
    # ImPlotLocation_North     = 1 << 0,                                         /* original C++ signature */
    north = enum.auto()      # (= 1 << 0)  # top-center
    # ImPlotLocation_South     = 1 << 1,                                         /* original C++ signature */
    south = enum.auto()      # (= 1 << 1)  # bottom-center
    # ImPlotLocation_West      = 1 << 2,                                         /* original C++ signature */
    west = enum.auto()       # (= 1 << 2)  # center-left
    # ImPlotLocation_East      = 1 << 3,                                         /* original C++ signature */
    east = enum.auto()       # (= 1 << 3)  # center-right
    # ImPlotLocation_NorthWest = ImPlotLocation_North | ImPlotLocation_West,     /* original C++ signature */
    north_west = enum.auto() # (= ImPlotLocation_.north | ImPlotLocation_.west)  # top-left
    # ImPlotLocation_NorthEast = ImPlotLocation_North | ImPlotLocation_East,     /* original C++ signature */
    north_east = enum.auto() # (= ImPlotLocation_.north | ImPlotLocation_.east)  # top-right
    # ImPlotLocation_SouthWest = ImPlotLocation_South | ImPlotLocation_West,     /* original C++ signature */
    south_west = enum.auto() # (= ImPlotLocation_.south | ImPlotLocation_.west)  # bottom-left
    # ImPlotLocation_SouthEast = ImPlotLocation_South | ImPlotLocation_East      /* original C++ signature */
    south_east = enum.auto() # (= ImPlotLocation_.south | ImPlotLocation_.east)  # bottom-right

class ImPlotBin_(enum.Enum):    # implot.h:458
    """ Enums for different automatic histogram binning methods (k = bin count or w = bin width)"""
    # ImPlotBin_Sqrt    = -1,     /* original C++ signature */
    sqrt = enum.auto()    # (= -1)  # k = sqrt(n)
    # ImPlotBin_Sturges = -2,     /* original C++ signature */
    sturges = enum.auto() # (= -2)  # k = 1 + log2(n)
    # ImPlotBin_Rice    = -3,     /* original C++ signature */
    rice = enum.auto()    # (= -3)  # k = 2 * cbrt(n)
    # ImPlotBin_Scott   = -4,     /* original C++ signature */
    scott = enum.auto()   # (= -4)  # w = 3.49 * sigma / cbrt(n)

class ImPlotPoint:    # implot.h:466
    """ Double precision version of ImVec2 used by ImPlot. Extensible by end users."""
    # double x,     /* original C++ signature */
    x: float                                             # implot.h:467
    # y;    /* original C++ signature */
    y: float                                             # implot.h:467
    # ImPlotPoint()                         { x = y = 0.0;      }    /* original C++ signature */
    def __init__(self) -> None:                          # implot.h:468
        pass
    # ImPlotPoint(double _x, double _y)     { x = _x; y = _y;   }    /* original C++ signature */
    def __init__(self, _x: float, _y: float) -> None:    # implot.h:469
        pass
    # ImPlotPoint(const ImVec2& p)          { x = p.x; y = p.y; }    /* original C++ signature */
    def __init__(self, p: ImVec2) -> None:               # implot.h:470
        pass

class ImPlotRange:    # implot.h:480
    """ Range defined by a min/max value."""
    # double Min,     /* original C++ signature */
    min: float                                               # implot.h:481
    # Max;    /* original C++ signature */
    max: float                                               # implot.h:481
    # ImPlotRange()                         { Min = 0; Max = 0;                                         }    /* original C++ signature */
    def __init__(self) -> None:                              # implot.h:482
        pass
    # ImPlotRange(double _min, double _max) { Min = _min; Max = _max;                                   }    /* original C++ signature */
    def __init__(self, _min: float, _max: float) -> None:    # implot.h:483
        pass

class ImPlotRect:    # implot.h:490
    """ Combination of two range limits for X and Y axes. Also an AABB defined by Min()/Max()."""
    # ImPlotRange X,     /* original C++ signature */
    x: ImPlotRange                                                                         # implot.h:491
    # Y;    /* original C++ signature */
    y: ImPlotRange                                                                         # implot.h:491
    # ImPlotRect()                                                       {                                                               }    /* original C++ signature */
    def __init__(self) -> None:                                                            # implot.h:492
        pass
    # ImPlotRect(double x_min, double x_max, double y_min, double y_max) { X.Min = x_min; X.Max = x_max; Y.Min = y_min; Y.Max = y_max;   }    /* original C++ signature */
    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float) -> None:    # implot.h:493
        pass

class ImPlotStyle:    # implot.h:504
    """ Plot style structure"""
    # item styling variables
    # float   LineWeight;    /* original C++ signature */
    line_weight: float             # = 1,      item line weight in pixels    # implot.h:506
    # int     Marker;    /* original C++ signature */
    marker: int                    # = ImPlotMarker_None, marker specification    # implot.h:507
    # float   MarkerSize;    /* original C++ signature */
    marker_size: float             # = 4,      marker size in pixels (roughly the marker's "radius")    # implot.h:508
    # float   MarkerWeight;    /* original C++ signature */
    marker_weight: float           # = 1,      outline weight of markers in pixels    # implot.h:509
    # float   FillAlpha;    /* original C++ signature */
    fill_alpha: float              # = 1,      alpha modifier applied to plot fills    # implot.h:510
    # float   ErrorBarSize;    /* original C++ signature */
    error_bar_size: float          # = 5,      error bar whisker width in pixels    # implot.h:511
    # float   ErrorBarWeight;    /* original C++ signature */
    error_bar_weight: float        # = 1.5,    error bar whisker weight in pixels    # implot.h:512
    # float   DigitalBitHeight;    /* original C++ signature */
    digital_bit_height: float      # = 8,      digital channels bit height (at y = 1.0) in pixels    # implot.h:513
    # float   DigitalBitGap;    /* original C++ signature */
    digital_bit_gap: float         # = 4,      digital channels bit padding gap in pixels    # implot.h:514
    # plot styling variables
    # float   PlotBorderSize;    /* original C++ signature */
    plot_border_size: float        # = 1,      line thickness of border around plot area    # implot.h:516
    # float   MinorAlpha;    /* original C++ signature */
    minor_alpha: float             # = 0.25    alpha multiplier applied to minor axis grid lines    # implot.h:517
    # ImVec2  MajorTickLen;    /* original C++ signature */
    major_tick_len: ImVec2         # = 10,10   major tick lengths for X and Y axes    # implot.h:518
    # ImVec2  MinorTickLen;    /* original C++ signature */
    minor_tick_len: ImVec2         # = 5,5     minor tick lengths for X and Y axes    # implot.h:519
    # ImVec2  MajorTickSize;    /* original C++ signature */
    major_tick_size: ImVec2        # = 1,1     line thickness of major ticks    # implot.h:520
    # ImVec2  MinorTickSize;    /* original C++ signature */
    minor_tick_size: ImVec2        # = 1,1     line thickness of minor ticks    # implot.h:521
    # ImVec2  MajorGridSize;    /* original C++ signature */
    major_grid_size: ImVec2        # = 1,1     line thickness of major grid lines    # implot.h:522
    # ImVec2  MinorGridSize;    /* original C++ signature */
    minor_grid_size: ImVec2        # = 1,1     line thickness of minor grid lines    # implot.h:523
    # ImVec2  PlotPadding;    /* original C++ signature */
    plot_padding: ImVec2           # = 10,10   padding between widget frame and plot area, labels, or outside legends (i.e. main padding)    # implot.h:524
    # ImVec2  LabelPadding;    /* original C++ signature */
    label_padding: ImVec2          # = 5,5     padding between axes labels, tick labels, and plot edge    # implot.h:525
    # ImVec2  LegendPadding;    /* original C++ signature */
    legend_padding: ImVec2         # = 10,10   legend padding from plot edges    # implot.h:526
    # ImVec2  LegendInnerPadding;    /* original C++ signature */
    legend_inner_padding: ImVec2   # = 5,5     legend inner padding from legend edges    # implot.h:527
    # ImVec2  LegendSpacing;    /* original C++ signature */
    legend_spacing: ImVec2         # = 5,0     spacing between legend entries    # implot.h:528
    # ImVec2  MousePosPadding;    /* original C++ signature */
    mouse_pos_padding: ImVec2      # = 10,10   padding between plot edge and interior mouse location text    # implot.h:529
    # ImVec2  AnnotationPadding;    /* original C++ signature */
    annotation_padding: ImVec2     # = 2,2     text padding around annotation labels    # implot.h:530
    # ImVec2  FitPadding;    /* original C++ signature */
    fit_padding: ImVec2            # = 0,0     additional fit padding as a percentage of the fit extents (e.g. ImVec2(0.1,0.1) adds 10% to the fit extents of X and Y)    # implot.h:531
    # ImVec2  PlotDefaultSize;    /* original C++ signature */
    plot_default_size: ImVec2      # = 400,300 default size used when ImVec2(0,0) is passed to BeginPlot    # implot.h:532
    # ImVec2  PlotMinSize;    /* original C++ signature */
    plot_min_size: ImVec2          # = 200,150 minimum size plot frame can be when shrunk    # implot.h:533
    # style colors
    # colormap
    # ImPlotColormap Colormap;    /* original C++ signature */
    colormap: ImPlotColormap       # The current colormap. Set this to either an ImPlotColormap_ enum or an index returned by AddColormap.    # implot.h:537
    # settings/flags
    # bool    UseLocalTime;    /* original C++ signature */
    use_local_time: bool           # = False,  axis labels will be formatted for your timezone when ImPlotAxisFlag_Time is enabled    # implot.h:539
    # bool    UseISO8601;    /* original C++ signature */
    use_iso8601: bool              # = False,  dates will be formatted according to ISO 8601 where applicable (e.g. YYYY-MM-DD, YYYY-MM, --MM-DD, etc.)    # implot.h:540
    # bool    Use24HourClock;    /* original C++ signature */
    use24_hour_clock: bool         # = False,  times will be formatted using a 24 hour clock    # implot.h:541
    # IMPLOT_API ImPlotStyle();    /* original C++ signature */
    def __init__(self) -> None:    # implot.h:542
        pass


class ImPlotInputMap:    # implot.h:555
    """ Input mapping structure. Default values listed. See also MapInputDefault, MapInputReverse."""
    # ImGuiMouseButton Pan;    /* original C++ signature */
    pan: ImGuiMouseButton            # LMB    enables panning when held,    # implot.h:556
    # ImGuiModFlags    PanMod;    /* original C++ signature */
    pan_mod: ImGuiModFlags           # none   optional modifier that must be held for panning/fitting    # implot.h:557
    # ImGuiMouseButton Fit;    /* original C++ signature */
    fit: ImGuiMouseButton            # LMB    initiates fit when double clicked    # implot.h:558
    # ImGuiMouseButton Select;    /* original C++ signature */
    select: ImGuiMouseButton         # RMB    begins box selection when pressed and confirms selection when released    # implot.h:559
    # ImGuiMouseButton SelectCancel;    /* original C++ signature */
    select_cancel: ImGuiMouseButton  # LMB    cancels active box selection when pressed; cannot be same as Select    # implot.h:560
    # ImGuiModFlags    SelectMod;    /* original C++ signature */
    select_mod: ImGuiModFlags        # none   optional modifier that must be held for box selection    # implot.h:561
    # ImGuiModFlags    SelectHorzMod;    /* original C++ signature */
    select_horz_mod: ImGuiModFlags   # Alt    expands active box selection horizontally to plot edge when held    # implot.h:562
    # ImGuiModFlags    SelectVertMod;    /* original C++ signature */
    select_vert_mod: ImGuiModFlags   # Shift  expands active box selection vertically to plot edge when held    # implot.h:563
    # ImGuiMouseButton Menu;    /* original C++ signature */
    menu: ImGuiMouseButton           # RMB    opens context menus (if enabled) when clicked    # implot.h:564
    # ImGuiModFlags    OverrideMod;    /* original C++ signature */
    override_mod: ImGuiModFlags      # Ctrl   when held, all input is ignored; used to enable axis/plots as DND sources    # implot.h:565
    # ImGuiModFlags    ZoomMod;    /* original C++ signature */
    zoom_mod: ImGuiModFlags          # none   optional modifier that must be held for scroll wheel zooming    # implot.h:566
    # float            ZoomRate;    /* original C++ signature */
    zoom_rate: float                 # 0.1   zoom rate for scroll (e.g. 0.1 = 10% plot range every scroll click); make negative to invert    # implot.h:567
    # IMPLOT_API ImPlotInputMap();    /* original C++ signature */
    def __init__(self) -> None:      # implot.h:568
        pass

#-----------------------------------------------------------------------------
# [SECTION] Callbacks
#-----------------------------------------------------------------------------





#-----------------------------------------------------------------------------
# [SECTION] Contexts
#-----------------------------------------------------------------------------

# IMPLOT_API ImPlotContext* CreateContext();    /* original C++ signature */
def create_context() -> ImPlotContext:    # implot.h:591
    """ Creates a new ImPlot context. Call this after ImGui::CreateContext."""
    pass
# IMPLOT_API void DestroyContext(ImPlotContext* ctx = NULL);    /* original C++ signature */
def destroy_context(ctx: ImPlotContext = None) -> None:    # implot.h:593
    """ Destroys an ImPlot context. Call this before ImGui::DestroyContext. None = destroy current context."""
    pass
# IMPLOT_API ImPlotContext* GetCurrentContext();    /* original C++ signature */
def get_current_context() -> ImPlotContext:    # implot.h:595
    """ Returns the current ImPlot context. None if no context has ben set."""
    pass
# IMPLOT_API void SetCurrentContext(ImPlotContext* ctx);    /* original C++ signature */
def set_current_context(ctx: ImPlotContext) -> None:    # implot.h:597
    """ Sets the current ImPlot context."""
    pass

# IMPLOT_API void SetImGuiContext(ImGuiContext* ctx);    /* original C++ signature */
def set_im_gui_context(ctx: ImGuiContext) -> None:    # implot.h:603
    """ Sets the current **ImGui** context. This is ONLY necessary if you are compiling
     ImPlot as a DLL (not recommended) separate from your ImGui compilation. It
     sets the global variable GImGui, which is not shared across DLL boundaries.
     See GImGui documentation in imgui.cpp for more details.
    """
    pass

#-----------------------------------------------------------------------------
# [SECTION] Begin/End Plot
#-----------------------------------------------------------------------------

# IMPLOT_API bool BeginPlot(const char* title_id, const ImVec2& size=ImVec2(-1,0), ImPlotFlags flags=0);    /* original C++ signature */
def begin_plot(title_id: str, size: ImVec2 = ImVec2(-1,0), flags: ImPlotFlags = 0) -> bool:    # implot.h:625
    """ Starts a 2D plotting context. If this function returns True, EndPlot() MUST
     be called! You are encouraged to use the following convention:

     if (BeginPlot(...)) {
         PlotLine(...);
         ...
         EndPlot();
     }

     Important notes:

     - #title_id must be unique to the current ImGui ID scope. If you need to avoid ID
       collisions or don't want to display a title in the plot, use double hashes
       (e.g. "MyPlot##HiddenIdText" or "##NoTitle").
     - #size is the **frame** size of the plot widget, not the plot area. The default
       size of plots (i.e. when ImVec2(0,0)) can be modified in your ImPlotStyle.
    """
    pass

# IMPLOT_API void EndPlot();    /* original C++ signature */
def end_plot() -> None:    # implot.h:629
    """ Only call EndPlot() if BeginPlot() returns True! Typically called at the end
     of an if statement conditioned on BeginPlot(). See example above.
    """
    pass

#-----------------------------------------------------------------------------
# [SECTION] Begin/End Subplots
#-----------------------------------------------------------------------------

# Starts a subdivided plotting context. If the function returns True,
# EndSubplots() MUST be called! Call BeginPlot/EndPlot AT MOST [rows*cols]
# times in  between the begining and end of the subplot context. Plots are
# added in row major order.
#
# Example:
#
# if (BeginSubplots("My Subplot",2,3,ImVec2(800,400)) {
#     for (int i = 0; i < 6; ++i) {
#         if (BeginPlot(...)) {
#             ImPlot::PlotLine(...);
#             ...
#             EndPlot();
#         }
#     }
#     EndSubplots();
# }
#
# Produces:
#
# [0] | [1] | [2]
# ----|-----|----
# [3] | [4] | [5]
#
# Important notes:
#
# - #title_id must be unique to the current ImGui ID scope. If you need to avoid ID
#   collisions or don't want to display a title in the plot, use double hashes
#   (e.g. "MySubplot##HiddenIdText" or "##NoTitle").
# - #rows and #cols must be greater than 0.
# - #size is the size of the entire grid of subplots, not the individual plots
# - #row_ratios and #col_ratios must have AT LEAST #rows and #cols elements,
#   respectively. These are the sizes of the rows and columns expressed in ratios.
#   If the user adjusts the dimensions, the arrays are updated with new ratios.
#
# Important notes regarding BeginPlot from inside of BeginSubplots:
#
# - The #title_id parameter of _BeginPlot_ (see above) does NOT have to be
#   unique when called inside of a subplot context. Subplot IDs are hashed
#   for your convenience so you don't have call PushID or generate unique title
#   strings. Simply pass an empty string to BeginPlot unless you want to title
#   each subplot.
# - The #size parameter of _BeginPlot_ (see above) is ignored when inside of a
#   subplot context. The actual size of the subplot will be based on the
#   #size value you pass to _BeginSubplots_ and #row/#col_ratios if provided.

# IMPLOT_API bool BeginSubplots(const char* title_id,    /* original C++ signature */
#                              int rows,
#                              int cols,
#                              const ImVec2& size,
#                              ImPlotSubplotFlags flags = 0,
#                              float* row_ratios        = NULL,
#                              float* col_ratios        = NULL);
def begin_subplots(title_id: str, rows: int, cols: int, size: ImVec2, flags: ImPlotSubplotFlags = 0, row_ratios: Optional[float] = None, col_ratios: Optional[float] = None) -> Tuple[bool, Optional[float], Optional[float]]:    # implot.h:681
    pass

# IMPLOT_API void EndSubplots();    /* original C++ signature */
def end_subplots() -> None:    # implot.h:691
    """ Only call EndSubplots() if BeginSubplots() returns True! Typically called at the end
     of an if statement conditioned on BeginSublots(). See example above.
    """
    pass

#-----------------------------------------------------------------------------
# [SECTION] Setup
#-----------------------------------------------------------------------------

# The following API allows you to setup and customize various aspects of the
# current plot. The functions should be called immediately after BeginPlot
# and before any other API calls. Typical usage is as follows:

# if (BeginPlot(...)) {                     1) begin a new plot
#     SetupAxis(ImAxis_X1, "My X-Axis");    2) make Setup calls
#     SetupAxis(ImAxis_Y1, "My Y-Axis");
#     SetupLegend(ImPlotLocation_North);
#     ...
#     SetupFinish();                        3) [optional] explicitly finish setup
#     PlotLine(...);                        4) plot items
#     ...
#     EndPlot();                            5) end the plot
# }
#
# Important notes:
#
# - Always call Setup code at the top of your BeginPlot conditional statement.
# - Setup is locked once you start plotting or explicitly call SetupFinish.
#   Do NOT call Setup code after you begin plotting or after you make
#   any non-Setup API calls (e.g. utils like PlotToPixels also lock Setup)
# - Calling SetupFinish is OPTIONAL, but probably good practice. If you do not
#   call it yourself, then the first subsequent plotting or utility function will
#   call it for you.

# IMPLOT_API void SetupAxis(ImAxis axis, const char* label=NULL, ImPlotAxisFlags flags=0);    /* original C++ signature */
def setup_axis(axis: ImAxis, label: str = None, flags: ImPlotAxisFlags = 0) -> None:    # implot.h:723
    """ Enables an axis or sets the label and/or flags for an existing axis. Leave #label = None for no label."""
    pass
# IMPLOT_API void SetupAxisLimits(ImAxis axis, double v_min, double v_max, ImPlotCond cond = ImPlotCond_Once);    /* original C++ signature */
def setup_axis_limits(axis: ImAxis, v_min: float, v_max: float, cond: ImPlotCond = ImPlotCond_.once) -> None:    # implot.h:725
    """ Sets an axis range limits. If ImPlotCond_Always is used, the axes limits will be locked."""
    pass
# IMPLOT_API void SetupAxisLinks(ImAxis axis, double* link_min, double* link_max);    /* original C++ signature */
def setup_axis_links(axis: ImAxis, link_min: float, link_max: float) -> Tuple[float, float]:    # implot.h:727
    """ Links an axis range limits to external values. Set to None for no linkage. The pointer data must remain valid until EndPlot."""
    pass
# IMPLOT_API void SetupAxisFormat(ImAxis axis, const char* fmt);    /* original C++ signature */
def setup_axis_format(axis: ImAxis, fmt: str) -> None:    # implot.h:729
    """ Sets the format of numeric axis labels via formater specifier (default="%g"). Formated values will be double (i.e. use %f)."""
    pass
# IMPLOT_API void SetupAxisScale(ImAxis axis, ImPlotScale scale);    /* original C++ signature */
def setup_axis_scale(axis: ImAxis, scale: ImPlotScale) -> None:    # implot.h:737
    """ Sets an axis' scale using built-in options."""
    pass
# IMPLOT_API void SetupAxisLimitsConstraints(ImAxis axis, double v_min, double v_max);    /* original C++ signature */
def setup_axis_limits_constraints(axis: ImAxis, v_min: float, v_max: float) -> None:    # implot.h:741
    """ Sets an axis' limits constraints."""
    pass
# IMPLOT_API void SetupAxisZoomConstraints(ImAxis axis, double z_min, double z_max);    /* original C++ signature */
def setup_axis_zoom_constraints(axis: ImAxis, z_min: float, z_max: float) -> None:    # implot.h:743
    """ Sets an axis' zoom constraints."""
    pass

# IMPLOT_API void SetupAxes(const char* x_label, const char* y_label, ImPlotAxisFlags x_flags=0, ImPlotAxisFlags y_flags=0);    /* original C++ signature */
def setup_axes(x_label: str, y_label: str, x_flags: ImPlotAxisFlags = 0, y_flags: ImPlotAxisFlags = 0) -> None:    # implot.h:746
    """ Sets the label and/or flags for primary X and Y axes (shorthand for two calls to SetupAxis)."""
    pass
# IMPLOT_API void SetupAxesLimits(double x_min, double x_max, double y_min, double y_max, ImPlotCond cond = ImPlotCond_Once);    /* original C++ signature */
def setup_axes_limits(x_min: float, x_max: float, y_min: float, y_max: float, cond: ImPlotCond = ImPlotCond_.once) -> None:    # implot.h:748
    """ Sets the primary X and Y axes range limits. If ImPlotCond_Always is used, the axes limits will be locked (shorthand for two calls to SetupAxisLimits)."""
    pass

# IMPLOT_API void SetupLegend(ImPlotLocation location, ImPlotLegendFlags flags=0);    /* original C++ signature */
def setup_legend(location: ImPlotLocation, flags: ImPlotLegendFlags = 0) -> None:    # implot.h:751
    """ Sets up the plot legend."""
    pass
# IMPLOT_API void SetupMouseText(ImPlotLocation location, ImPlotMouseTextFlags flags=0);    /* original C++ signature */
def setup_mouse_text(location: ImPlotLocation, flags: ImPlotMouseTextFlags = 0) -> None:    # implot.h:753
    """ Set the location of the current plot's mouse position text (default = South|East)."""
    pass

# IMPLOT_API void SetupFinish();    /* original C++ signature */
def setup_finish() -> None:    # implot.h:757
    """ Explicitly finalize plot setup. Once you call this, you cannot make anymore Setup calls for the current plot!
     Note that calling this function is OPTIONAL; it will be called by the first subsequent setup-locking API call.
    """
    pass

#-----------------------------------------------------------------------------
# [SECTION] SetNext
#-----------------------------------------------------------------------------

# Though you should default to the `Setup` API above, there are some scenarios
# where (re)configuring a plot or axis before `BeginPlot` is needed (e.g. if
# using a preceding button or slider widget to change the plot limits). In
# this case, you can use the `SetNext` API below. While this is not as feature
# rich as the Setup API, most common needs are provided. These functions can be
# called anwhere except for inside of `Begin/EndPlot`. For example:

# if (ImGui::Button("Center Plot"))
#     ImPlot::SetNextPlotLimits(-1,1,-1,1);
# if (ImPlot::BeginPlot(...)) {
#     ...
#     ImPlot::EndPlot();
# }
#
# Important notes:
#
# - You must still enable non-default axes with SetupAxis for these functions
#   to work properly.

# IMPLOT_API void SetNextAxisLimits(ImAxis axis, double v_min, double v_max, ImPlotCond cond = ImPlotCond_Once);    /* original C++ signature */
def set_next_axis_limits(axis: ImAxis, v_min: float, v_max: float, cond: ImPlotCond = ImPlotCond_.once) -> None:    # implot.h:783
    """ Sets an upcoming axis range limits. If ImPlotCond_Always is used, the axes limits will be locked."""
    pass
# IMPLOT_API void SetNextAxisLinks(ImAxis axis, double* link_min, double* link_max);    /* original C++ signature */
def set_next_axis_links(axis: ImAxis, link_min: float, link_max: float) -> Tuple[float, float]:    # implot.h:785
    """ Links an upcoming axis range limits to external values. Set to None for no linkage. The pointer data must remain valid until EndPlot!"""
    pass
# IMPLOT_API void SetNextAxisToFit(ImAxis axis);    /* original C++ signature */
def set_next_axis_to_fit(axis: ImAxis) -> None:    # implot.h:787
    """ Set an upcoming axis to auto fit to its data."""
    pass

# IMPLOT_API void SetNextAxesLimits(double x_min, double x_max, double y_min, double y_max, ImPlotCond cond = ImPlotCond_Once);    /* original C++ signature */
def set_next_axes_limits(x_min: float, x_max: float, y_min: float, y_max: float, cond: ImPlotCond = ImPlotCond_.once) -> None:    # implot.h:790
    """ Sets the upcoming primary X and Y axes range limits. If ImPlotCond_Always is used, the axes limits will be locked (shorthand for two calls to SetupAxisLimits)."""
    pass
# IMPLOT_API void SetNextAxesToFit();    /* original C++ signature */
def set_next_axes_to_fit() -> None:    # implot.h:792
    """ Sets all upcoming axes to auto fit to their data."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Plot Items
#-----------------------------------------------------------------------------

# The main plotting API is provied below. Call these functions between
# Begin/EndPlot and after any Setup API calls. Each plots data on the current
# x and y axes, which can be changed with `SetAxis/Axes`.
#
# The templated functions are explicitly instantiated in implot_items.cpp.
# They are not intended to be used generically with custom types. You will get
# a linker error if you try! All functions support the following scalar types:
#
# float, double, ImS8, ImU8, ImS16, ImU16, ImS32, ImU32, ImS64, ImU64
#
#
# If you need to plot custom or non-homogenous data you have a few options:
#
# 1. If your data is a simple struct/class (e.g. Vector2), you can use striding.
#    This is the most performant option if applicable.
#
#    struct Vector2 { float X, Y; };
#    ...
#    Vector2 data[42];
#    ImPlot::PlotLine("line", &data[0].x, &data[0].y, 42, 0, 0, sizeof(Vector2));
#
# 2. Write a custom getter C function or C++ lambda and pass it and optionally your data to
#    an ImPlot function post-fixed with a G (e.g. PlotScatterG). This has a slight performance
#    cost, but probably not enough to worry about unless your data is very large. Examples:
#
#    ImPlotPoint MyDataGetter(None* data, int idx) {
#        MyData* my_data = (MyData*)data;
#        ImPlotPoint p;
#        p.x = my_data->GetTime(idx);
#        p.y = my_data->GetValue(idx);
#        return p
#    }
#    ...
#    auto my_lambda = [](int idx, None*) {
#        double t = idx / 999.0;
#        return ImPlotPoint(t, 0.5+0.5*std::sin(2*PI*10*t));
#    };
#    ...
#    if (ImPlot::BeginPlot("MyPlot")) {
#        MyData my_data;
#        ImPlot::PlotScatterG("scatter", MyDataGetter, &my_data, my_data.Size());
#        ImPlot::PlotLineG("line", my_lambda, None, 1000);
#        ImPlot::EndPlot();
#    }
#
# NB: All types are converted to double before plotting. You may lose information
# if you try plotting extremely large 64-bit integral types. Proceed with caution!

# Plots a standard 2D line plot.
# IMPLOT_TMP void PlotLine(const char* label_id, const T* values, int count, double xscale=1, double xstart=0, ImPlotLineFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_line(label_id: str, values: np.ndarray, xscale: float = 1, xstart: float = 0, flags: ImPlotLineFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:847
    pass
# IMPLOT_TMP void PlotLine(const char* label_id, const T* xs, const T* ys, int count, ImPlotLineFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_line(label_id: str, xs: np.ndarray, ys: np.ndarray, flags: ImPlotLineFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:848
    pass

# Plots a standard 2D scatter plot. Default marker is ImPlotMarker_Circle.
# IMPLOT_TMP void PlotScatter(const char* label_id, const T* values, int count, double xscale=1, double xstart=0, ImPlotScatterFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_scatter(label_id: str, values: np.ndarray, xscale: float = 1, xstart: float = 0, flags: ImPlotScatterFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:852
    pass
# IMPLOT_TMP void PlotScatter(const char* label_id, const T* xs, const T* ys, int count, ImPlotScatterFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_scatter(label_id: str, xs: np.ndarray, ys: np.ndarray, flags: ImPlotScatterFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:853
    pass

# Plots a a stairstep graph. The y value is continued constantly to the right from every x position, i.e. the interval [x[i], x[i+1]) has the value y[i]
# IMPLOT_TMP void PlotStairs(const char* label_id, const T* values, int count, double xscale=1, double xstart=0, ImPlotStairsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_stairs(label_id: str, values: np.ndarray, xscale: float = 1, xstart: float = 0, flags: ImPlotStairsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:857
    pass
# IMPLOT_TMP void PlotStairs(const char* label_id, const T* xs, const T* ys, int count, ImPlotStairsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_stairs(label_id: str, xs: np.ndarray, ys: np.ndarray, flags: ImPlotStairsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:858
    pass

# Plots a shaded (filled) region between two lines, or a line and a horizontal reference. Set yref to +/-INFINITY for infinite fill extents.
# IMPLOT_TMP void PlotShaded(const char* label_id, const T* values, int count, double yref=0, double xscale=1, double xstart=0, ImPlotShadedFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_shaded(label_id: str, values: np.ndarray, yref: float = 0, xscale: float = 1, xstart: float = 0, flags: ImPlotShadedFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:862
    pass
# IMPLOT_TMP void PlotShaded(const char* label_id, const T* xs, const T* ys, int count, double yref=0, ImPlotShadedFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_shaded(label_id: str, xs: np.ndarray, ys: np.ndarray, yref: float = 0, flags: ImPlotShadedFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:863
    pass
# IMPLOT_TMP void PlotShaded(const char* label_id, const T* xs, const T* ys1, const T* ys2, int count, ImPlotShadedFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_shaded(label_id: str, xs: np.ndarray, ys1: np.ndarray, ys2: np.ndarray, flags: ImPlotShadedFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:864
    pass

# Plots a bar graph. Vertical by default. #bar_size and #shift are in plot units.
# IMPLOT_TMP void PlotBars(const char* label_id, const T* values, int count, double bar_size=0.67, double shift=0, ImPlotBarsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_bars(label_id: str, values: np.ndarray, bar_size: float = 0.67, shift: float = 0, flags: ImPlotBarsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:868
    pass
# IMPLOT_TMP void PlotBars(const char* label_id, const T* xs, const T* ys, int count, double bar_size, ImPlotBarsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_bars(label_id: str, xs: np.ndarray, ys: np.ndarray, bar_size: float, flags: ImPlotBarsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:869
    pass


# Plots vertical error bar. The label_id should be the same as the label_id of the associated line or bar plot.
# IMPLOT_TMP void PlotErrorBars(const char* label_id, const T* xs, const T* ys, const T* err, int count, ImPlotErrorBarsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_error_bars(label_id: str, xs: np.ndarray, ys: np.ndarray, err: np.ndarray, flags: ImPlotErrorBarsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:876
    pass
# IMPLOT_TMP void PlotErrorBars(const char* label_id, const T* xs, const T* ys, const T* neg, const T* pos, int count, ImPlotErrorBarsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_error_bars(label_id: str, xs: np.ndarray, ys: np.ndarray, neg: np.ndarray, pos: np.ndarray, flags: ImPlotErrorBarsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:877
    pass

# Plots stems. Vertical by default.
# IMPLOT_TMP void PlotStems(const char* label_id, const T* values, int count, double ref=0, double scale=1, double start=0, ImPlotStemsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_stems(label_id: str, values: np.ndarray, ref: float = 0, scale: float = 1, start: float = 0, flags: ImPlotStemsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:880
    pass
# IMPLOT_TMP void PlotStems(const char* label_id, const T* xs, const T* ys, int count, double ref=0, ImPlotStemsFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_stems(label_id: str, xs: np.ndarray, ys: np.ndarray, ref: float = 0, flags: ImPlotStemsFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:881
    pass

# IMPLOT_TMP void PlotInfLines(const char* label_id, const T* values, int count, ImPlotInfLinesFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_inf_lines(label_id: str, values: np.ndarray, flags: ImPlotInfLinesFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:884
    """ Plots infinite vertical or horizontal lines (e.g. for references or asymptotes)."""
    pass



# IMPLOT_TMP double PlotHistogram(const char* label_id, const T* values, int count, int bins=ImPlotBin_Sturges, double bar_scale=1.0, ImPlotRange range=ImPlotRange(), ImPlotHistogramFlags flags=0);    /* original C++ signature */
def plot_histogram(label_id: str, values: np.ndarray, bins: int = ImPlotBin_.sturges, bar_scale: float = 1.0, range: ImPlotRange = ImPlotRange(), flags: ImPlotHistogramFlags = 0) -> float:    # implot.h:894
    """ Plots a horizontal histogram. #bins can be a positive integer or an ImPlotBin_ method. If #range is left unspecified, the min/max of #values will be used as the range.
     Otherwise, outlier values outside of the range are not binned. The largest bin count or density is returned.
    """
    pass

# IMPLOT_TMP double PlotHistogram2D(const char* label_id, const T* xs, const T* ys, int count, int x_bins=ImPlotBin_Sturges, int y_bins=ImPlotBin_Sturges, ImPlotRect range=ImPlotRect(), ImPlotHistogramFlags flags=0);    /* original C++ signature */
def plot_histogram2_d(label_id: str, xs: np.ndarray, ys: np.ndarray, x_bins: int = ImPlotBin_.sturges, y_bins: int = ImPlotBin_.sturges, range: ImPlotRect = ImPlotRect(), flags: ImPlotHistogramFlags = 0) -> float:    # implot.h:898
    """ Plots two dimensional, bivariate histogram as a heatmap. #x_bins and #y_bins can be a positive integer or an ImPlotBin. If #range is left unspecified, the min/max of
     #xs an #ys will be used as the ranges. Otherwise, outlier values outside of range are not binned. The largest bin count or density is returned.
    """
    pass

# Plots digital data. Digital plots do not respond to y drag or zoom, and are always referenced to the bottom of the plot.
# IMPLOT_TMP void PlotDigital(const char* label_id, const T* xs, const T* ys, int count, ImPlotDigitalFlags flags=0, int offset=0, int stride=sizeof(T));    /* original C++ signature */
def plot_digital(label_id: str, xs: np.ndarray, ys: np.ndarray, flags: ImPlotDigitalFlags = 0, offset: int = 0, stride: int = -1) -> None:    # implot.h:901
    pass

# IMPLOT_API void PlotImage(const char* label_id, ImTextureID user_texture_id, const ImPlotPoint& bounds_min, const ImPlotPoint& bounds_max, const ImVec2& uv0=ImVec2(0,0), const ImVec2& uv1=ImVec2(1,1), const ImVec4& tint_col=ImVec4(1,1,1,1), ImPlotImageFlags flags=0);    /* original C++ signature */
def plot_image(label_id: str, user_texture_id: ImTextureID, bounds_min: ImPlotPoint, bounds_max: ImPlotPoint, uv0: ImVec2 = ImVec2(0,0), uv1: ImVec2 = ImVec2(1,1), tint_col: ImVec4 = ImVec4(1,1,1,1), flags: ImPlotImageFlags = 0) -> None:    # implot.h:905
    """ Plots an axis-aligned image. #bounds_min/bounds_max are in plot coordinates (y-up) and #uv0/uv1 are in texture coordinates (y-down)."""
    pass

# IMPLOT_API void PlotText(const char* text, double x, double y, const ImVec2& pix_offset=ImVec2(0,0), ImPlotTextFlags flags=0);    /* original C++ signature */
def plot_text(text: str, x: float, y: float, pix_offset: ImVec2 = ImVec2(0,0), flags: ImPlotTextFlags = 0) -> None:    # implot.h:908
    """ Plots a centered text label at point x,y with an optional pixel offset. Text color can be changed with ImPlot::PushStyleColor(ImPlotCol_InlayText, ...)."""
    pass

# IMPLOT_API void PlotDummy(const char* label_id, ImPlotDummyFlags flags=0);    /* original C++ signature */
def plot_dummy(label_id: str, flags: ImPlotDummyFlags = 0) -> None:    # implot.h:911
    """ Plots a dummy item (i.e. adds a legend entry colored by ImPlotCol_Line)"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Plot Tools
#-----------------------------------------------------------------------------

# The following can be used to render interactive elements and/or annotations.
# Like the item plotting functions above, they apply to the current x and y
# axes, which can be changed with `SetAxis/SetAxes`.

# IMPLOT_API bool DragPoint(int id, double* x, double* y, const ImVec4& col, float size = 4, ImPlotDragToolFlags flags=0);    /* original C++ signature */
def drag_point(id: int, x: float, y: float, col: ImVec4, size: float = 4, flags: ImPlotDragToolFlags = 0) -> Tuple[bool, float, float]:    # implot.h:922
    """ Shows a draggable point at x,y. #col defaults to ImGuiCol_Text."""
    pass
# IMPLOT_API bool DragLineX(int id, double* x, const ImVec4& col, float thickness = 1, ImPlotDragToolFlags flags=0);    /* original C++ signature */
def drag_line_x(id: int, x: float, col: ImVec4, thickness: float = 1, flags: ImPlotDragToolFlags = 0) -> Tuple[bool, float]:    # implot.h:924
    """ Shows a draggable vertical guide line at an x-value. #col defaults to ImGuiCol_Text."""
    pass
# IMPLOT_API bool DragLineY(int id, double* y, const ImVec4& col, float thickness = 1, ImPlotDragToolFlags flags=0);    /* original C++ signature */
def drag_line_y(id: int, y: float, col: ImVec4, thickness: float = 1, flags: ImPlotDragToolFlags = 0) -> Tuple[bool, float]:    # implot.h:926
    """ Shows a draggable horizontal guide line at a y-value. #col defaults to ImGuiCol_Text."""
    pass
# IMPLOT_API bool DragRect(int id, double* x1, double* y1, double* x2, double* y2, const ImVec4& col, ImPlotDragToolFlags flags=0);    /* original C++ signature */
def drag_rect(id: int, x1: float, y1: float, x2: float, y2: float, col: ImVec4, flags: ImPlotDragToolFlags = 0) -> Tuple[bool, float, float, float, float]:    # implot.h:928
    """ Shows a draggable and resizeable rectangle."""
    pass

# Shows an annotation callout at a chosen point. Clamping keeps annotations in the plot area. Annotations are always rendered on top.
# IMPLOT_API void Annotation(double x, double y, const ImVec4& col, const ImVec2& pix_offset, bool clamp, bool round = false);    /* original C++ signature */
def annotation(x: float, y: float, col: ImVec4, pix_offset: ImVec2, clamp: bool, round: bool = False) -> None:    # implot.h:931
    pass
# IMPLOT_API void Annotation(double x, double y, const ImVec4& col, const ImVec2& pix_offset, bool clamp, const char* fmt, ...)           ;    /* original C++ signature */
def annotation(x: float, y: float, col: ImVec4, pix_offset: ImVec2, clamp: bool, fmt: str) -> None:    # implot.h:932
    pass

# Shows a x-axis tag at the specified coordinate value.
# IMPLOT_API void TagX(double x, const ImVec4& col, bool round = false);    /* original C++ signature */
def tag_x(x: float, col: ImVec4, round: bool = False) -> None:    # implot.h:936
    pass
# IMPLOT_API void TagX(double x, const ImVec4& col, const char* fmt, ...)           ;    /* original C++ signature */
def tag_x(x: float, col: ImVec4, fmt: str) -> None:    # implot.h:937
    pass

# Shows a y-axis tag at the specified coordinate value.
# IMPLOT_API void TagY(double y, const ImVec4& col, bool round = false);    /* original C++ signature */
def tag_y(y: float, col: ImVec4, round: bool = False) -> None:    # implot.h:941
    pass
# IMPLOT_API void TagY(double y, const ImVec4& col, const char* fmt, ...)           ;    /* original C++ signature */
def tag_y(y: float, col: ImVec4, fmt: str) -> None:    # implot.h:942
    pass

#-----------------------------------------------------------------------------
# [SECTION] Plot Utils
#-----------------------------------------------------------------------------

# Select which axis/axes will be used for subsequent plot elements.
# IMPLOT_API void SetAxis(ImAxis axis);    /* original C++ signature */
def set_axis(axis: ImAxis) -> None:    # implot.h:950
    pass
# IMPLOT_API void SetAxes(ImAxis x_axis, ImAxis y_axis);    /* original C++ signature */
def set_axes(x_axis: ImAxis, y_axis: ImAxis) -> None:    # implot.h:951
    pass

# Convert pixels to a position in the current plot's coordinate system. Passing IMPLOT_AUTO uses the current axes.
# IMPLOT_API ImPlotPoint PixelsToPlot(const ImVec2& pix, ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def pixels_to_plot(pix: ImVec2, x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImPlotPoint:    # implot.h:954
    pass
# IMPLOT_API ImPlotPoint PixelsToPlot(float x, float y, ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def pixels_to_plot(x: float, y: float, x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImPlotPoint:    # implot.h:955
    pass

# Convert a position in the current plot's coordinate system to pixels. Passing IMPLOT_AUTO uses the current axes.
# IMPLOT_API ImVec2 PlotToPixels(const ImPlotPoint& plt, ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def plot_to_pixels(plt: ImPlotPoint, x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImVec2:    # implot.h:958
    pass
# IMPLOT_API ImVec2 PlotToPixels(double x, double y, ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def plot_to_pixels(x: float, y: float, x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImVec2:    # implot.h:959
    pass

# IMPLOT_API ImVec2 GetPlotPos();    /* original C++ signature */
def get_plot_pos() -> ImVec2:    # implot.h:962
    """ Get the current Plot position (top-left) in pixels."""
    pass
# IMPLOT_API ImVec2 GetPlotSize();    /* original C++ signature */
def get_plot_size() -> ImVec2:    # implot.h:964
    """ Get the curent Plot size in pixels."""
    pass

# IMPLOT_API ImPlotPoint GetPlotMousePos(ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def get_plot_mouse_pos(x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImPlotPoint:    # implot.h:967
    """ Returns the mouse position in x,y coordinates of the current plot. Passing IMPLOT_AUTO uses the current axes."""
    pass
# IMPLOT_API ImPlotRect GetPlotLimits(ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def get_plot_limits(x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImPlotRect:    # implot.h:969
    """ Returns the current plot axis range."""
    pass

# IMPLOT_API bool IsPlotHovered();    /* original C++ signature */
def is_plot_hovered() -> bool:    # implot.h:972
    """ Returns True if the plot area in the current plot is hovered."""
    pass
# IMPLOT_API bool IsAxisHovered(ImAxis axis);    /* original C++ signature */
def is_axis_hovered(axis: ImAxis) -> bool:    # implot.h:974
    """ Returns True if the axis label area in the current plot is hovered."""
    pass
# IMPLOT_API bool IsSubplotsHovered();    /* original C++ signature */
def is_subplots_hovered() -> bool:    # implot.h:976
    """ Returns True if the bounding frame of a subplot is hovered."""
    pass

# IMPLOT_API bool IsPlotSelected();    /* original C++ signature */
def is_plot_selected() -> bool:    # implot.h:979
    """ Returns True if the current plot is being box selected."""
    pass
# IMPLOT_API ImPlotRect GetPlotSelection(ImAxis x_axis = IMPLOT_AUTO, ImAxis y_axis = IMPLOT_AUTO);    /* original C++ signature */
def get_plot_selection(x_axis: ImAxis = IMPLOT_AUTO, y_axis: ImAxis = IMPLOT_AUTO) -> ImPlotRect:    # implot.h:981
    """ Returns the current plot box selection bounds. Passing IMPLOT_AUTO uses the current axes."""
    pass
# IMPLOT_API void CancelPlotSelection();    /* original C++ signature */
def cancel_plot_selection() -> None:    # implot.h:983
    """ Cancels a the current plot box selection."""
    pass

# IMPLOT_API void HideNextItem(bool hidden = true, ImPlotCond cond = ImPlotCond_Once);    /* original C++ signature */
def hide_next_item(hidden: bool = True, cond: ImPlotCond = ImPlotCond_.once) -> None:    # implot.h:987
    """ Hides or shows the next plot item (i.e. as if it were toggled from the legend).
     Use ImPlotCond_Always if you need to forcefully set this every frame.
    """
    pass

# Use the following around calls to Begin/EndPlot to align l/r/t/b padding.
# Consider using Begin/EndSubplots first. They are more feature rich and
# accomplish the same behaviour by default. The functions below offer lower
# level control of plot alignment.

# IMPLOT_API bool BeginAlignedPlots(const char* group_id, bool vertical = true);    /* original C++ signature */
def begin_aligned_plots(group_id: str, vertical: bool = True) -> bool:    # implot.h:996
    """ Align axis padding over multiple plots in a single row or column. #group_id must
     be unique. If this function returns True, EndAlignedPlots() must be called.
    """
    pass
# IMPLOT_API void EndAlignedPlots();    /* original C++ signature */
def end_aligned_plots() -> None:    # implot.h:998
    """ Only call EndAlignedPlots() if BeginAlignedPlots() returns True!"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Legend Utils
#-----------------------------------------------------------------------------

# IMPLOT_API bool BeginLegendPopup(const char* label_id, ImGuiMouseButton mouse_button=1);    /* original C++ signature */
def begin_legend_popup(label_id: str, mouse_button: ImGuiMouseButton = 1) -> bool:    # implot.h:1005
    """ Begin a popup for a legend entry."""
    pass
# IMPLOT_API void EndLegendPopup();    /* original C++ signature */
def end_legend_popup() -> None:    # implot.h:1007
    """ End a popup for a legend entry."""
    pass
# IMPLOT_API bool IsLegendEntryHovered(const char* label_id);    /* original C++ signature */
def is_legend_entry_hovered(label_id: str) -> bool:    # implot.h:1009
    """ Returns True if a plot item legend entry is hovered."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Drag and Drop
#-----------------------------------------------------------------------------

# IMPLOT_API bool BeginDragDropTargetPlot();    /* original C++ signature */
def begin_drag_drop_target_plot() -> bool:    # implot.h:1016
    """ Turns the current plot's plotting area into a drag and drop target. Don't forget to call EndDragDropTarget!"""
    pass
# IMPLOT_API bool BeginDragDropTargetAxis(ImAxis axis);    /* original C++ signature */
def begin_drag_drop_target_axis(axis: ImAxis) -> bool:    # implot.h:1018
    """ Turns the current plot's X-axis into a drag and drop target. Don't forget to call EndDragDropTarget!"""
    pass
# IMPLOT_API bool BeginDragDropTargetLegend();    /* original C++ signature */
def begin_drag_drop_target_legend() -> bool:    # implot.h:1020
    """ Turns the current plot's legend into a drag and drop target. Don't forget to call EndDragDropTarget!"""
    pass
# IMPLOT_API void EndDragDropTarget();    /* original C++ signature */
def end_drag_drop_target() -> None:    # implot.h:1022
    """ Ends a drag and drop target (currently just an alias for ImGui::EndDragDropTarget)."""
    pass

# NB: By default, plot and axes drag and drop *sources* require holding the Ctrl modifier to initiate the drag.
# You can change the modifier if desired. If ImGuiModFlags_None is provided, the axes will be locked from panning.

# IMPLOT_API bool BeginDragDropSourcePlot(ImGuiDragDropFlags flags=0);    /* original C++ signature */
def begin_drag_drop_source_plot(flags: ImGuiDragDropFlags = 0) -> bool:    # implot.h:1028
    """ Turns the current plot's plotting area into a drag and drop source. You must hold Ctrl. Don't forget to call EndDragDropSource!"""
    pass
# IMPLOT_API bool BeginDragDropSourceAxis(ImAxis axis, ImGuiDragDropFlags flags=0);    /* original C++ signature */
def begin_drag_drop_source_axis(axis: ImAxis, flags: ImGuiDragDropFlags = 0) -> bool:    # implot.h:1030
    """ Turns the current plot's X-axis into a drag and drop source. You must hold Ctrl. Don't forget to call EndDragDropSource!"""
    pass
# IMPLOT_API bool BeginDragDropSourceItem(const char* label_id, ImGuiDragDropFlags flags=0);    /* original C++ signature */
def begin_drag_drop_source_item(label_id: str, flags: ImGuiDragDropFlags = 0) -> bool:    # implot.h:1032
    """ Turns an item in the current plot's legend into drag and drop source. Don't forget to call EndDragDropSource!"""
    pass
# IMPLOT_API void EndDragDropSource();    /* original C++ signature */
def end_drag_drop_source() -> None:    # implot.h:1034
    """ Ends a drag and drop source (currently just an alias for ImGui::EndDragDropSource)."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Styling
#-----------------------------------------------------------------------------

# Styling colors in ImPlot works similarly to styling colors in ImGui, but
# with one important difference. Like ImGui, all style colors are stored in an
# indexable array in ImPlotStyle. You can permanently modify these values through
# GetStyle().Colors, or temporarily modify them with Push/Pop functions below.
# However, by default all style colors in ImPlot default to a special color
# IMPLOT_AUTO_COL. The behavior of this color depends upon the style color to
# which it as applied:
#
#     1) For style colors associated with plot items (e.g. ImPlotCol_Line),
#        IMPLOT_AUTO_COL tells ImPlot to color the item with the next unused
#        color in the current colormap. Thus, every item will have a different
#        color up to the number of colors in the colormap, at which point the
#        colormap will roll over. For most use cases, you should not need to
#        set these style colors to anything but IMPLOT_COL_AUTO; you are
#        probably better off changing the current colormap. However, if you
#        need to explicitly color a particular item you may either Push/Pop
#        the style color around the item in question, or use the SetNextXXXStyle
#        API below. If you permanently set one of these style colors to a specific
#        color, or forget to call Pop, then all subsequent items will be styled
#        with the color you set.
#
#     2) For style colors associated with plot styling (e.g. ImPlotCol_PlotBg),
#        IMPLOT_AUTO_COL tells ImPlot to set that color from color data in your
#        **ImGuiStyle**. The ImGuiCol_ that these style colors default to are
#        detailed above, and in general have been mapped to produce plots visually
#        consistent with your current ImGui style. Of course, you are free to
#        manually set these colors to whatever you like, and further can Push/Pop
#        them around individual plots for plot-specific styling (e.g. coloring axes).

# IMPLOT_API ImPlotStyle& GetStyle();    /* original C++ signature */
def get_style() -> ImPlotStyle:    # implot.h:1070
    """ Provides access to plot style structure for permanant modifications to colors, sizes, etc."""
    pass

# IMPLOT_API void StyleColorsAuto(ImPlotStyle* dst = NULL);    /* original C++ signature */
def style_colors_auto(dst: ImPlotStyle = None) -> None:    # implot.h:1073
    """ Style plot colors for current ImGui style (default)."""
    pass
# IMPLOT_API void StyleColorsClassic(ImPlotStyle* dst = NULL);    /* original C++ signature */
def style_colors_classic(dst: ImPlotStyle = None) -> None:    # implot.h:1075
    """ Style plot colors for ImGui "Classic"."""
    pass
# IMPLOT_API void StyleColorsDark(ImPlotStyle* dst = NULL);    /* original C++ signature */
def style_colors_dark(dst: ImPlotStyle = None) -> None:    # implot.h:1077
    """ Style plot colors for ImGui "Dark"."""
    pass
# IMPLOT_API void StyleColorsLight(ImPlotStyle* dst = NULL);    /* original C++ signature */
def style_colors_light(dst: ImPlotStyle = None) -> None:    # implot.h:1079
    """ Style plot colors for ImGui "Light"."""
    pass

# Use PushStyleX to temporarily modify your ImPlotStyle. The modification
# will last until the matching call to PopStyleX. You MUST call a pop for
# every push, otherwise you will leak memory! This behaves just like ImGui.

# Temporarily modify a style color. Don't forget to call PopStyleColor!
# IMPLOT_API void PushStyleColor(ImPlotCol idx, ImU32 col);    /* original C++ signature */
def push_style_color(idx: ImPlotCol, col: ImU32) -> None:    # implot.h:1086
    pass
# IMPLOT_API void PushStyleColor(ImPlotCol idx, const ImVec4& col);    /* original C++ signature */
def push_style_color(idx: ImPlotCol, col: ImVec4) -> None:    # implot.h:1087
    pass
# IMPLOT_API void PopStyleColor(int count = 1);    /* original C++ signature */
def pop_style_color(count: int = 1) -> None:    # implot.h:1089
    """ Undo temporary style color modification(s). Undo multiple pushes at once by increasing count."""
    pass

# IMPLOT_API void PushStyleVar(ImPlotStyleVar idx, float val);    /* original C++ signature */
def push_style_var(idx: ImPlotStyleVar, val: float) -> None:    # implot.h:1092
    """ Temporarily modify a style variable of float type. Don't forget to call PopStyleVar!"""
    pass
# IMPLOT_API void PushStyleVar(ImPlotStyleVar idx, int val);    /* original C++ signature */
def push_style_var(idx: ImPlotStyleVar, val: int) -> None:    # implot.h:1094
    """ Temporarily modify a style variable of int type. Don't forget to call PopStyleVar!"""
    pass
# IMPLOT_API void PushStyleVar(ImPlotStyleVar idx, const ImVec2& val);    /* original C++ signature */
def push_style_var(idx: ImPlotStyleVar, val: ImVec2) -> None:    # implot.h:1096
    """ Temporarily modify a style variable of ImVec2 type. Don't forget to call PopStyleVar!"""
    pass
# IMPLOT_API void PopStyleVar(int count = 1);    /* original C++ signature */
def pop_style_var(count: int = 1) -> None:    # implot.h:1098
    """ Undo temporary style variable modification(s). Undo multiple pushes at once by increasing count."""
    pass

# The following can be used to modify the style of the next plot item ONLY. They do
# NOT require calls to PopStyleX. Leave style attributes you don't want modified to
# IMPLOT_AUTO or IMPLOT_AUTO_COL. Automatic styles will be deduced from the current
# values in your ImPlotStyle or from Colormap data.

# IMPLOT_API void SetNextLineStyle(const ImVec4& col = IMPLOT_AUTO_COL, float weight = IMPLOT_AUTO);    /* original C++ signature */
def set_next_line_style(col: ImVec4 = IMPLOT_AUTO_COL, weight: float = IMPLOT_AUTO) -> None:    # implot.h:1106
    """ Set the line color and weight for the next item only."""
    pass
# IMPLOT_API void SetNextFillStyle(const ImVec4& col = IMPLOT_AUTO_COL, float alpha_mod = IMPLOT_AUTO);    /* original C++ signature */
def set_next_fill_style(col: ImVec4 = IMPLOT_AUTO_COL, alpha_mod: float = IMPLOT_AUTO) -> None:    # implot.h:1108
    """ Set the fill color for the next item only."""
    pass
# IMPLOT_API void SetNextMarkerStyle(ImPlotMarker marker = IMPLOT_AUTO, float size = IMPLOT_AUTO, const ImVec4& fill = IMPLOT_AUTO_COL, float weight = IMPLOT_AUTO, const ImVec4& outline = IMPLOT_AUTO_COL);    /* original C++ signature */
def set_next_marker_style(marker: ImPlotMarker = IMPLOT_AUTO, size: float = IMPLOT_AUTO, fill: ImVec4 = IMPLOT_AUTO_COL, weight: float = IMPLOT_AUTO, outline: ImVec4 = IMPLOT_AUTO_COL) -> None:    # implot.h:1110
    """ Set the marker style for the next item only."""
    pass
# IMPLOT_API void SetNextErrorBarStyle(const ImVec4& col = IMPLOT_AUTO_COL, float size = IMPLOT_AUTO, float weight = IMPLOT_AUTO);    /* original C++ signature */
def set_next_error_bar_style(col: ImVec4 = IMPLOT_AUTO_COL, size: float = IMPLOT_AUTO, weight: float = IMPLOT_AUTO) -> None:    # implot.h:1112
    """ Set the error bar style for the next item only."""
    pass

# IMPLOT_API ImVec4 GetLastItemColor();    /* original C++ signature */
def get_last_item_color() -> ImVec4:    # implot.h:1115
    """ Gets the last item primary color (i.e. its legend icon color)"""
    pass

# IMPLOT_API const char* GetStyleColorName(ImPlotCol idx);    /* original C++ signature */
def get_style_color_name(idx: ImPlotCol) -> str:    # implot.h:1118
    """ Returns the null terminated string name for an ImPlotCol."""
    pass
# IMPLOT_API const char* GetMarkerName(ImPlotMarker idx);    /* original C++ signature */
def get_marker_name(idx: ImPlotMarker) -> str:    # implot.h:1120
    """ Returns the null terminated string name for an ImPlotMarker."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Colormaps
#-----------------------------------------------------------------------------

# Item styling is based on colormaps when the relevant ImPlotCol_XXX is set to
# IMPLOT_AUTO_COL (default). Several built-in colormaps are available. You can
# add and then push/pop your own colormaps as well. To permanently set a colormap,
# modify the Colormap index member of your ImPlotStyle.

# Colormap data will be ignored and a custom color will be used if you have done one of the following:
#     1) Modified an item style color in your ImPlotStyle to anything other than IMPLOT_AUTO_COL.
#     2) Pushed an item style color using PushStyleColor().
#     3) Set the next item style with a SetNextXXXStyle function.

# Add a new colormap. The color data will be copied. The colormap can be used by pushing either the returned index or the
# string name with PushColormap. The colormap name must be unique and the size must be greater than 1. You will receive
# an assert otherwise! By default colormaps are considered to be qualitative (i.e. discrete). If you want to create a
# continuous colormap, set #qual=False. This will treat the colors you provide as keys, and ImPlot will build a linearly
# interpolated lookup table. The memory footprint of this table will be exactly ((size-1)*255+1)*4 bytes.
# IMPLOT_API ImPlotColormap AddColormap(const char* name, const ImVec4* cols, int size, bool qual=true);    /* original C++ signature */
def add_colormap(name: str, cols: ImVec4, size: int, qual: bool = True) -> ImPlotColormap:    # implot.h:1141
    pass
# IMPLOT_API ImPlotColormap AddColormap(const char* name, const ImU32*  cols, int size, bool qual=true);    /* original C++ signature */
def add_colormap(name: str, cols: ImU32, size: int, qual: bool = True) -> ImPlotColormap:    # implot.h:1142
    pass

# IMPLOT_API int GetColormapCount();    /* original C++ signature */
def get_colormap_count() -> int:    # implot.h:1145
    """ Returns the number of available colormaps (i.e. the built-in + user-added count)."""
    pass
# IMPLOT_API const char* GetColormapName(ImPlotColormap cmap);    /* original C++ signature */
def get_colormap_name(cmap: ImPlotColormap) -> str:    # implot.h:1147
    """ Returns a null terminated string name for a colormap given an index. Returns None if index is invalid."""
    pass
# IMPLOT_API ImPlotColormap GetColormapIndex(const char* name);    /* original C++ signature */
def get_colormap_index(name: str) -> ImPlotColormap:    # implot.h:1149
    """ Returns an index number for a colormap given a valid string name. Returns -1 if name is invalid."""
    pass

# IMPLOT_API void PushColormap(ImPlotColormap cmap);    /* original C++ signature */
def push_colormap(cmap: ImPlotColormap) -> None:    # implot.h:1152
    """ Temporarily switch to one of the built-in (i.e. ImPlotColormap_XXX) or user-added colormaps (i.e. a return value of AddColormap). Don't forget to call PopColormap!"""
    pass
# IMPLOT_API void PushColormap(const char* name);    /* original C++ signature */
def push_colormap(name: str) -> None:    # implot.h:1154
    """ Push a colormap by string name. Use built-in names such as "Default", "Deep", "Jet", etc. or a string you provided to AddColormap. Don't forget to call PopColormap!"""
    pass
# IMPLOT_API void PopColormap(int count = 1);    /* original C++ signature */
def pop_colormap(count: int = 1) -> None:    # implot.h:1156
    """ Undo temporary colormap modification(s). Undo multiple pushes at once by increasing count."""
    pass

# IMPLOT_API ImVec4 NextColormapColor();    /* original C++ signature */
def next_colormap_color() -> ImVec4:    # implot.h:1160
    """ Returns the next color from the current colormap and advances the colormap for the current plot.
     Can also be used with no return value to skip colors if desired. You need to call this between Begin/EndPlot!
    """
    pass

# Colormap utils. If cmap = IMPLOT_AUTO (default), the current colormap is assumed.
# Pass an explicit colormap index (built-in or user-added) to specify otherwise.

# IMPLOT_API int GetColormapSize(ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def get_colormap_size(cmap: ImPlotColormap = IMPLOT_AUTO) -> int:    # implot.h:1166
    """ Returns the size of a colormap."""
    pass
# IMPLOT_API ImVec4 GetColormapColor(int idx, ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def get_colormap_color(idx: int, cmap: ImPlotColormap = IMPLOT_AUTO) -> ImVec4:    # implot.h:1168
    """ Returns a color from a colormap given an index >= 0 (modulo will be performed)."""
    pass
# IMPLOT_API ImVec4 SampleColormap(float t, ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def sample_colormap(t: float, cmap: ImPlotColormap = IMPLOT_AUTO) -> ImVec4:    # implot.h:1170
    """ Sample a color from the current colormap given t between 0 and 1."""
    pass

# IMPLOT_API void ColormapScale(const char* label, double scale_min, double scale_max, const ImVec2& size = ImVec2(0,0), const char* format = "%g", ImPlotColormapScaleFlags flags = 0, ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def colormap_scale(label: str, scale_min: float, scale_max: float, size: ImVec2 = ImVec2(0,0), format: str = "%g", flags: ImPlotColormapScaleFlags = 0, cmap: ImPlotColormap = IMPLOT_AUTO) -> None:    # implot.h:1173
    """ Shows a vertical color scale with linear spaced ticks using the specified color map. Use double hashes to hide label (e.g. "##NoLabel"). If scale_min > scale_max, the scale to color mapping will be reversed."""
    pass
# IMPLOT_API bool ColormapSlider(const char* label, float* t, ImVec4* out = NULL, const char* format = "", ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def colormap_slider(label: str, t: float, out: ImVec4 = None, format: str = "", cmap: ImPlotColormap = IMPLOT_AUTO) -> Tuple[bool, float]:    # implot.h:1175
    """ Shows a horizontal slider with a colormap gradient background. Optionally returns the color sampled at t in [0 1]."""
    pass
# IMPLOT_API bool ColormapButton(const char* label, const ImVec2& size = ImVec2(0,0), ImPlotColormap cmap = IMPLOT_AUTO);    /* original C++ signature */
def colormap_button(label: str, size: ImVec2 = ImVec2(0,0), cmap: ImPlotColormap = IMPLOT_AUTO) -> bool:    # implot.h:1177
    """ Shows a button with a colormap gradient brackground."""
    pass

# IMPLOT_API void BustColorCache(const char* plot_title_id = NULL);    /* original C++ signature */
def bust_color_cache(plot_title_id: str = None) -> None:    # implot.h:1186
    """ When items in a plot sample their color from a colormap, the color is cached and does not change
     unless explicitly overriden. Therefore, if you change the colormap after the item has already been plotted,
     item colors will NOT update. If you need item colors to resample the new colormap, then use this
     function to bust the cached colors. If #plot_title_id is None, then every item in EVERY existing plot
     will be cache busted. Otherwise only the plot specified by #plot_title_id will be busted. For the
     latter, this function must be called in the same ImGui ID scope that the plot is in. You should rarely if ever
     need this function, but it is available for applications that require runtime colormap swaps (e.g. Heatmaps demo).
    """
    pass

#-----------------------------------------------------------------------------
# [SECTION] Input Mapping
#-----------------------------------------------------------------------------

# IMPLOT_API ImPlotInputMap& GetInputMap();    /* original C++ signature */
def get_input_map() -> ImPlotInputMap:    # implot.h:1193
    """ Provides access to input mapping structure for permanant modifications to controls for pan, select, etc."""
    pass

# IMPLOT_API void MapInputDefault(ImPlotInputMap* dst = NULL);    /* original C++ signature */
def map_input_default(dst: ImPlotInputMap = None) -> None:    # implot.h:1196
    """ Default input mapping: pan = LMB drag, box select = RMB drag, fit = LMB double click, context menu = RMB click, zoom = scroll."""
    pass
# IMPLOT_API void MapInputReverse(ImPlotInputMap* dst = NULL);    /* original C++ signature */
def map_input_reverse(dst: ImPlotInputMap = None) -> None:    # implot.h:1198
    """ Reverse input mapping: pan = RMB drag, box select = LMB drag, fit = LMB double click, context menu = RMB click, zoom = scroll."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Miscellaneous
#-----------------------------------------------------------------------------

# Render icons similar to those that appear in legends (nifty for data lists).
# IMPLOT_API void ItemIcon(const ImVec4& col);    /* original C++ signature */
def item_icon(col: ImVec4) -> None:    # implot.h:1205
    pass
# IMPLOT_API void ItemIcon(ImU32 col);    /* original C++ signature */
def item_icon(col: ImU32) -> None:    # implot.h:1206
    pass
# IMPLOT_API void ColormapIcon(ImPlotColormap cmap);    /* original C++ signature */
def colormap_icon(cmap: ImPlotColormap) -> None:    # implot.h:1207
    pass

# IMPLOT_API ImDrawList* GetPlotDrawList();    /* original C++ signature */
def get_plot_draw_list() -> ImDrawList:    # implot.h:1210
    """ Get the plot draw list for custom rendering to the current plot area. Call between Begin/EndPlot."""
    pass
# IMPLOT_API void PushPlotClipRect(float expand=0);    /* original C++ signature */
def push_plot_clip_rect(expand: float = 0) -> None:    # implot.h:1212
    """ Push clip rect for rendering to current plot area. The rect can be expanded or contracted by #expand pixels. Call between Begin/EndPlot."""
    pass
# IMPLOT_API void PopPlotClipRect();    /* original C++ signature */
def pop_plot_clip_rect() -> None:    # implot.h:1214
    """ Pop plot clip rect. Call between Begin/EndPlot."""
    pass

# IMPLOT_API bool ShowStyleSelector(const char* label);    /* original C++ signature */
def show_style_selector(label: str) -> bool:    # implot.h:1217
    """ Shows ImPlot style selector dropdown menu."""
    pass
# IMPLOT_API bool ShowColormapSelector(const char* label);    /* original C++ signature */
def show_colormap_selector(label: str) -> bool:    # implot.h:1219
    """ Shows ImPlot colormap selector dropdown menu."""
    pass
# IMPLOT_API bool ShowInputMapSelector(const char* label);    /* original C++ signature */
def show_input_map_selector(label: str) -> bool:    # implot.h:1221
    """ Shows ImPlot input map selector dropdown menu."""
    pass
# IMPLOT_API void ShowStyleEditor(ImPlotStyle* ref = NULL);    /* original C++ signature */
def show_style_editor(ref: ImPlotStyle = None) -> None:    # implot.h:1223
    """ Shows ImPlot style editor block (not a window)."""
    pass
# IMPLOT_API void ShowUserGuide();    /* original C++ signature */
def show_user_guide() -> None:    # implot.h:1225
    """ Add basic help/info block for end users (not a window)."""
    pass
# IMPLOT_API void ShowMetricsWindow(bool* p_popen = NULL);    /* original C++ signature */
def show_metrics_window(p_popen: Optional[bool] = None) -> Optional[bool]:    # implot.h:1227
    """ Shows ImPlot metrics/debug information window."""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Demo
#-----------------------------------------------------------------------------

# IMPLOT_API void ShowDemoWindow(bool* p_open = NULL);    /* original C++ signature */
def show_demo_window(p_open: Optional[bool] = None) -> Optional[bool]:    # implot.h:1234
    """ Shows the ImPlot demo window (add implot_demo.cpp to your sources!)"""
    pass


# namespace ImPlot

#-----------------------------------------------------------------------------
# [SECTION] Obsolete API
#-----------------------------------------------------------------------------

# The following functions will be removed! Keep your copy of implot up to date!
# Occasionally set '#define IMPLOT_DISABLE_OBSOLETE_FUNCTIONS' to stay ahead.
# If you absolutely must use these functions and do not want to receive compiler
# warnings, set '#define IMPLOT_DISABLE_OBSOLETE_WARNINGS'.

####################    </generated_from:implot.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
