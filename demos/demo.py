from ej2_streamlit_grids import GridComponent, GridProps
import pandas as pd
import streamlit as st


data = pd.read_csv('dataset.csv')
props = GridProps(data)
# Add your Syncfusion Lincense key here.
props.registerLicense('{license key}')

props.height = 250
with st.sidebar:
    st.header('Example options')
    isEditing = st.checkbox('Editing', False)
    if isEditing:
        props.toolbarItems = ['Add', 'Delete', 'Edit']
        props.editSettings = { 'allowAdding': True, 'allowDeleting': True, 'allowEditing': True }

    isFiltering = st.checkbox('Filtering', False)
    props.allowFiltering = isFiltering

    isSorting = st.checkbox('Sorting', False)
    props.allowSorting = isSorting

    isDragDrop = st.checkbox('Drag and Drop', False)
    props.allowRowDragAndDrop = isDragDrop

    isSelection = st.checkbox('Selection', False)
    props.allowSelection = isSelection

    isReorder = st.checkbox('Reorder Columns', False)
    props.allowReordering = isReorder

    isResize = st.checkbox('Resize Columns', False)
    props.allowResizing = isResize

    isHover = st.checkbox('Enable Hover', False)
    props.enableHover = isHover

    isPaging = st.checkbox('Paging', False)
    if isPaging:
        pages = st.number_input('Enter the total number of items on a page', format='%i', step=1)
        props.allowPaging = True
        props.pageSettings = { 'pageSize': pages, 'pageSizes': True }

st.header('Syncfusion Streamlit Grid')
GridComponent(props)