package main

import (
	"fmt"
)

type ESOption func(es *ExcelSheet)

// row 从 0 开始
func WithValue(row int, h string, value interface{}) ESOption {
	return func(es *ExcelSheet) {
		c, ok := es.HeaderMap[h]
		if !ok {
			fmt.Printf("row(%d) invalid header(%s) not found in headers(%s), set value(%v) fail\n", 
				row, h, es.FirstRowTableHeader, value)
			return
		}
		if row >= es.ContentRowCount {
			fmt.Printf("row(%d) invalid(%d), set header(%s) value(%v) fail\n", 
				row, es.ContentRowCount, h, value)
			return
		}
		es.Content[row][c] = value
	}
}
