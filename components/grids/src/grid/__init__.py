import os
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import json
import typing

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "EJ2Grid",
        url="http://localhost:3001",
    )

else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("EJ2Grid", path=build_dir)

def SfGrid (Data: pd.DataFrame=None, Props: typing.Dict=None):

    if Data is not None:
        dataSet = PdToJson(Data)
        
    elif Props.dataSource is not None:
        dataSet = PdToJson(Props.dataSource)
    
    if Props is None:
        Props = GridProps(dataSet)

    if (Data is not None or Props is not None):
        params ={
                    # Properties
                    'data': dataSet,
                    'allowExcelExport': Props.allowExcelExport,
                    'allowFiltering': Props.allowFiltering,
                    'allowGrouping': Props.allowGrouping,
                    'allowMultiSorting': Props.allowMultiSorting,
                    'allowKeyboard': Props.allowKeyboard,
                    'allowPaging': Props.allowPaging,
                    'allowPdfExport': Props.allowPdfExport,
                    'allowReordering': Props.allowReordering,
                    'allowResizing': Props.allowResizing,
                    'allowRowDragAndDrop': Props.allowRowDragAndDrop,
                    'allowSelection': Props.allowSelection,
                    'allowSorting': Props.allowSorting,
                    'allowTextWrap': Props.allowTextWrap,
                    'enableAdaptiveUI': Props.enableAdaptiveUI,
                    'enableColumnVirtualization': Props.enableColumnVirtualization,
                    'enableHeaderFocus': Props.enableHeaderFocus,
                    'enableHover': Props.enableHover,
                    'enableImmutableMode': Props.enableImmutableMode,
                    'enableInfiniteScrolling': Props.enableInfiniteScrolling,
                    'enablePersistence': Props.enablePersistence,
                    'enableStickyHeader': Props.enableStickyHeader,
                    'enableVirtualMaskRow': Props.enableVirtualMaskRow,
                    'enableVirtualization': Props.enableVirtualization,
                    'enableStickyHeader': Props.enableStickyHeader,
                    'showColumnChooser': Props.showColumnChooser,
                    'showColumnMenu': Props.showColumnMenu,
                    'toolbarItems': Props.toolbarItems,
                    'childGrid': Props.childGrid,
                    'columnDirective': Props.columnDirective,
                    'editSettings': Props.editSettings,
                    'rowCount': Props.rowCount,
                    'sortSettings': Props.sortSettings,
                    'filterSettings': Props.filterSettings,
                    'groupSettings': Props.groupSettings,
                    'pageSettings': Props.pageSettings,
                    'infiniteScrollSettings': Props.infiniteScrollSettings,
                    'textWrapSettings': Props.textWrapSettings,
                    'licenseKey': Props._GridProps__license_key,
                    'height': Props.height,
                    'width': Props.width,
                    'rowHeight': Props.rowHeight,
                    'rowRenderingMode': Props.rowRenderingMode,
                    'selectedRowIndex': Props.selectedRowIndex,
                    'searchSettings': Props.searchSettings,
                    'selectionSettings': Props.selectionSettings,
                    'printMode': Props.printMode,
                    'frozenColumns': Props.frozenColumns,
                    'gridLines': Props.gridLines,
                    'frozenRows': Props.frozenRows,
                    'theme': Props.theme,
                }
        component_value = _component_func(params=params)
    else:
        st.warning('Provide data to render Grid component', icon="⚠️")

def PdToJson(dataframe: pd.DataFrame):
    json_obj = json.loads(dataframe.to_json())
    dict_keys = list(json_obj.keys())
    json_list = []

    for index in range(len(json_obj[dict_keys[0]])):
        row_obj = dict()
        for column in dict_keys:
            row_obj[column] = json_obj[column][str(index)]
        json_list.append(row_obj)
        
    return json_list

class GridProps:
    
    def __init__(self, data: pd.DataFrame=None):
        self.dataSource = data;
        self.allowExcelExport = False
        self.allowFiltering = False
        self.allowGrouping = False
        self.allowKeyboard = True
        self.allowMultiSorting = False
        self.allowPaging = False
        self.allowPdfExport = False
        self.allowReordering = False
        self.allowResizing = False
        self.allowRowDragAndDrop = False
        self.allowSelection = True
        self.allowSorting = False
        self.allowTextWrap = False
        self.enableAdaptiveUI = False
        self.enableColumnVirtualization = False
        self.enableHeaderFocus = False
        self.enableHover = True
        self.enableImmutableMode = False
        self.enableInfiniteScrolling = False
        self.enablePersistence = False
        self.enableRtl = False
        self.enableStickyHeader = False
        self.enableVirtualMaskRow = True
        self.enableVirtualization = False
        self.showColumnChooser = False
        self.showColumnMenu = False
        self.toolbarItems = None
        self.childGrid = None
        self.columnDirective = None
        self.rowCount = None
        self.sortSettings = {}
        self.pageSettings = {}
        self.filterSettings = {}
        self.groupSettings = {}
        self.searchSettings = {}
        self.selectionSettings = {}
        self.infiniteScrollSettings = {}
        self.textWrapSettings = {}
        self.height = '300'
        self.width = 'auto'
        self.rowHeight = None
        self.rowRenderingMode = None
        self.selectedRowIndex = None
        self.printMode = None
        self.frozenColumns = None
        self.frozenRows = None
        self.gridLines = None
        self.editSettings = None
        self.theme = 'https://cdn.syncfusion.com/ej2/22.1.34/material.css'
        self.__license_key = None

    def registerLicense(self, key: str):
        self.__license_key = key

