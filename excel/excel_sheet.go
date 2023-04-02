package main

import (
	"strings"
	"github.com/xuri/excelize/v2"
)

const (
	defaultHeadersSplit = "|"
)

type ExcelSheet struct {
	SheetName string
	FirstRowTableHeader string
	HeaderMap map[string]int
	Header []string
	ContentCollCount int
	ContentRowCount int
	Content [][]interface{}
}

func NewExcelSheet(sheet, headers, split string, rowCount int) *ExcelSheet {
	split = strings.TrimSpace(split)
	if split == "" {
		split = defaultHeadersSplit
	}
	es := new(ExcelSheet)
	es.SheetName = strings.TrimSpace(sheet)
	es.FirstRowTableHeader = strings.TrimSpace(headers)
	es.Header = strings.Split(es.FirstRowTableHeader, split)
	es.HeaderMap = make(map[string]int)
	for i, h := range es.Header {
		es.HeaderMap[h] = i
	}
	es.ContentCollCount = len(es.Header)
	es.ContentRowCount = rowCount
	es.Content = make([][]interface{}, es.ContentRowCount)
	for i := range es.Content {
		es.Content[i] = make([]interface{}, es.ContentCollCount)
	}
	return es
}

func (es *ExcelSheet) DumpSheet(file *excelize.File, opts ...ESOption) {
	for _, o := range opts {
		o(es)
	}
	file.SetSheetRow(es.SheetName, "A0", &es.Header)
	for i := range es.Content{
		cell, _ := excelize.CoordinatesToCellName(1, i+1)
		file.SetSheetRow(es.SheetName, cell, &es.Content[i])
	}
}