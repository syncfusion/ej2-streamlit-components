import { StreamlitComponentBase, withStreamlitConnection } from "streamlit-component-lib";
import React, { ReactNode } from "react";
import { ClipMode, ColumnChooser, ColumnDirective, ColumnMenu, ColumnsDirective, Edit, Filter, Freeze, GridComponent, Group, InfiniteScroll, PdfExport, Reorder, Resize, RowDD, Search, TextAlign, Toolbar } from '@syncfusion/ej2-react-grids';
import { Inject, ExcelExport, DetailRow, Page, Sort } from '@syncfusion/ej2-react-grids';
import { DateFormatOptions, NumberFormatOptions, registerLicense } from "@syncfusion/ej2-base";
import { ClickEventArgs } from "@syncfusion/ej2-navigations";

interface State {
  refreshed: number
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
export class EJ2Grid extends StreamlitComponentBase<State> {

  constructor(props: any) {
    super(props);
    this.state = { refreshed: 1 }
  }

  private gridInstance: GridComponent | null = null;

  public renderColumns = (data: object[]): any[] => {
    let columns: any[] = [];
    let key: number = 0;
    let columnDirective = this.props.args.params.columnDirective;
    let headerText: string;
    let clipMode: ClipMode | undefined;
    let format: string | NumberFormatOptions | DateFormatOptions | undefined;
    let textAlign: TextAlign | undefined;
    let width: string | number | undefined;
    let isPrimaryKey: boolean | undefined;
    for (let column of Object.keys(data[0])) {
      format = undefined;
      textAlign = undefined;
      headerText = column;
      clipMode = undefined;
      width = undefined;
      isPrimaryKey = false;
      if (this.props.args.params.columnDirective) {
        for (let directive of columnDirective) {
          if (directive.field === column) {
            headerText = directive.headerText;
            clipMode = directive.clipMode;
            format = directive.format ? directive.format : '';
            textAlign = directive.textAlign;
            width = directive.width;
            isPrimaryKey = directive.isPrimaryKey;
          }
        }
      }
      columns.push(<ColumnDirective field={column} headerText={headerText} format={format} textAlign={textAlign} width={width} clipMode={clipMode} isPrimaryKey={isPrimaryKey} key={key++} />);
    }
    return columns;
  }

  public toolbarClick = (args: ClickEventArgs): void => {
    switch (args.item.text) {
      case 'PDF Export':
        this.gridInstance?.pdfExport();
        break;
      case 'Excel Export':
        this.gridInstance?.excelExport();
        break;
      case 'CSV Export':
        this.gridInstance?.csvExport();
        break;
    }
  }

  public render = (): ReactNode => {

    const totalColumns: any[] = this.renderColumns(this.props.args.params.data);

    if (this.props.args.params.licenseKey) {
      console.log('license provided');
      registerLicense(this.props.args.params.licenseKey);
    }


    return (
      <>
        <link rel="stylesheet" href={this.props.args.params.theme} />
        <GridComponent ref={grid => this.gridInstance = grid}
          dataSource={this.props.args.params.data}
          toolbar={this.props.args.params.toolbarItems}
          toolbarClick={this.toolbarClick.bind(this)}
          allowExcelExport={this.props.args.params.allowExcelExport}
          allowKeyboard={this.props.args.params.allowKeyboard}
          allowMultiSorting={this.props.args.params.allowMultiSorting}
          allowPdfExport={this.props.args.params.allowPdfExport}
          allowReordering={this.props.args.params.allowReordering}
          allowRowDragAndDrop={this.props.args.params.allowRowDragAndDrop}
          allowSelection={this.props.args.params.allowSelection}
          allowTextWrap={this.props.args.params.allowTextWrap}
          enableAdaptiveUI={this.props.args.params.enableAdaptiveUI}
          enableColumnVirtualization={this.props.args.params.enableColumnVirtualization}
          enableHeaderFocus={this.props.args.params.enableHeaderFocus}
          enableHover={this.props.args.params.enableHover}
          enableImmutableMode={this.props.args.params.enableImmutableMode}
          enableInfiniteScrolling={this.props.args.params.enableInfiniteScrolling} infiniteScrollSettings={this.props.args.params.infiniteScrollSettings}
          enablePersistence={this.props.args.params.enablePersistence}
          enableStickyHeader={this.props.args.params.enableStickyHeader}
          enableVirtualMaskRow={this.props.args.params.enableVirtualMaskRow}
          enableVirtualization={this.props.args.params.enableVirtualization}
          showColumnChooser={this.props.args.params.showColumnChooser}
          showColumnMenu={this.props.args.params.showColumnMenu}
          childGrid={this.props.args.params.childGrid}
          editSettings={this.props.args.params.editSettings}
          allowGrouping={this.props.args.params.allowGrouping} groupSettings={this.props.args.params.groupSettings}
          allowPaging={this.props.args.params.allowPaging} pageSettings={this.props.args.params.pageSettings}
          allowFiltering={this.props.args.params.allowFiltering} filterSettings={this.props.args.params.filterSettings}
          allowSorting={this.props.args.params.allowSorting} sortSettings={this.props.args.params.sortSettings}
          searchSettings={this.props.args.params.searchSettings}
          selectionSettings={this.props.args.params.selectionSettings}
          textWrapSettings={this.props.args.params.textWrapSettings}
          allowResizing={this.props.args.params.allowResizing}
          height={this.props.args.params.height}
          width={this.props.args.params.width}
          rowHeight={this.props.args.params.rowHeight}
          rowRenderingMode={this.props.args.params.rowRenderingMode}
          selectedRowIndex={this.props.args.params.selectedRowIndex}
          printMode={this.props.args.params.printMode}
          frozenColumns={this.props.args.params.frozenColumns}
          gridLines={this.props.args.params.gridLines}
          frozenRows={this.props.args.params.frozenRows}>
          <ColumnsDirective>
            {totalColumns}
          </ColumnsDirective>
          <Inject services={[Page, Sort, Filter, Group, Toolbar, InfiniteScroll, ExcelExport, PdfExport, Reorder, Resize, RowDD, Edit, Freeze, Search, DetailRow, ColumnChooser, ColumnMenu]} />
        </GridComponent>
      </>
    )
  }

}
export default withStreamlitConnection(EJ2Grid)
