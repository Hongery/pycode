package main

import (
    "fmt"

    "github.com/xuri/excelize/v2"
)

func main() {
    f := excelize.NewFile()
    defer func() {
        if err := f.Close(); err != nil {
            fmt.Println(err)
        }
    }()
    // Create a new sheet.
    // index, err := f.NewSheet("Sheet2")
    // if err != nil {
    //     fmt.Println(err)
    //     return
    // }
	// cell, err := excelize.CoordinatesToCellName(1, 1)
    // Set value of a cell.
    // f.SetSheetRow("Sheet2", "A2", &[]interface{}{"Hello world2222."})
	//f.SetCellValue("Sheet2", "A2", "Hello world11111.")
    // f.SetCellValue("Sheet1", "B2", 200)
    // Set active sheet of the workbook.
    // f.SetActiveSheet(index)
    // Save spreadsheet by the given path.
	c := [][]string{
		{"ag601", "parsing"},
		{"hg305", "detection"},
	}
	es := NewExcelSheet("Sheet1", "label_project_name|label_cat", "|", len(c))
	opts := []ESOption{}
	for i := range c {
		for j:= range c[i] {
			o := WithValue(i, es.Header[j], c[i][j])
			opts = append(opts, o)
		}
	}
	es.DumpSheet(f, opts...)
    if err := f.SaveAs("Book1.xlsx"); err != nil {
        fmt.Println(err)
    }
}