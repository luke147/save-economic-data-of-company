#!/usr/bin/python

import PyPDF2, sys

class SaveEconomicData:
    years = []
    values = {}
    matchCharsForAmount = "(0123456789,)"
    yearLength = 4
    
    def IsAmount(self, value):
        return any(c in match_chars for c in value)
    
    def SaveHeadAsYears(self, strHead):
        values = strHead.split()
        for value in values:
            if value.isdigit() and (len(value) == self.yearLength):
                self.years.append(int(value))
        
        return len(self.years) > 0
    
    def SaveValues(self, strLine):
        items = strLine.split("  ")
        index = ""
        values = []
        
        for i, item in enumerate(items):
            if i == 0:
                self.values[item] = []
                index = item
                self.values[index] = {}
                continue
            
            yearCount = len(self.years)
            if self.IsAmount(item) and ((i + 1) < yearCount):
                self.values[index][self.years[i - 1]] = item
    
    def Run(self):
        # Open the PDF file
        pdf_file = open('/home/lukas/Dokumenty/investování/Corning Incorporated/Corning - Annual Report - 2021.pdf', 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        years = []
        headIsSaved = False

        # Iterate through each page of the PDF
        numPages = len(pdf_reader.pages)
        for page_num in range(0, numPages):
            if len(self.values) > 0:
                break
            
            text = pdf_reader.pages[page_num].extract_text()
            
            if not "Consolidated Balance Sheets" in text:
                print("page: %d" % page_num)
                continue
            
            print("page: %d" % page_num)
            lines = text.splitlines()
            lineCount = len(lines)
            lineCountUnderHead = 0
            for i, line in enumerate(lines):
                headIsSaved = self.SaveHeadAsYears(line)
                if not headIsSaved:
                    continue
                
                self.SaveValues(line)
        
        pdf_file.close()
        print(self.values)

saveData = SaveEconomicData()
saveData.Run()
