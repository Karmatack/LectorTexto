from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    EXCEPINFO, VgaColor, _lcid, typelib_path, Library, IEnumVARIANT,
    Color, Checked, Monochrome, _check_version, OLE_COLOR,
    OLE_CANCELBOOL, OLE_YPOS_PIXELS, IDispatch, OLE_OPTEXCLUSIVE,
    OLE_XPOS_CONTAINER, OLE_XPOS_HIMETRIC, OLE_YSIZE_PIXELS,
    IFontEventsDisp, OLE_YPOS_HIMETRIC, StdPicture, CoClass,
    Unchecked, GUID, FONTSTRIKETHROUGH, COMMETHOD, DISPPROPERTY,
    FONTBOLD, HRESULT, OLE_XSIZE_CONTAINER, OLE_YSIZE_CONTAINER,
    IPictureDisp, IUnknown, IFontDisp, OLE_YSIZE_HIMETRIC, IPicture,
    OLE_XSIZE_HIMETRIC, Default, FONTITALIC, BSTR, OLE_HANDLE,
    OLE_YPOS_CONTAINER, Font, dispid, FONTSIZE, DISPMETHOD,
    OLE_XPOS_PIXELS, DISPPARAMS, Picture, OLE_ENABLEDEFAULTBOOL,
    IFont, StdFont, VARIANT_BOOL, FONTUNDERSCORE, FontEvents,
    FONTNAME, Gray, OLE_XSIZE_PIXELS
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'OLE_YSIZE_HIMETRIC', 'IPicture', 'VgaColor',
    'OLE_XSIZE_HIMETRIC', 'Default', 'LoadPictureConstants',
    'typelib_path', 'FONTITALIC', 'Library', 'OLE_HANDLE', 'Color',
    'Checked', 'OLE_YPOS_CONTAINER', 'Monochrome', 'OLE_COLOR',
    'OLE_CANCELBOOL', 'OLE_YPOS_PIXELS', 'Font', 'FONTSIZE',
    'OLE_TRISTATE', 'OLE_OPTEXCLUSIVE', 'OLE_XPOS_CONTAINER',
    'OLE_XPOS_HIMETRIC', 'OLE_YSIZE_PIXELS', 'IFontEventsDisp',
    'OLE_XPOS_PIXELS', 'OLE_YPOS_HIMETRIC', 'StdPicture', 'Picture',
    'Unchecked', 'FONTSTRIKETHROUGH', 'FONTBOLD',
    'OLE_ENABLEDEFAULTBOOL', 'OLE_XSIZE_CONTAINER', 'IFont',
    'StdFont', 'OLE_YSIZE_CONTAINER', 'FONTUNDERSCORE', 'FontEvents',
    'OLE_XSIZE_PIXELS', 'IPictureDisp', 'FONTNAME', 'Gray',
    'IFontDisp'
]

