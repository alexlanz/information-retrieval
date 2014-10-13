class Output:
    ROW_WIDTH = 30
    OUTPUT_FILE = "result.txt"

    file = None

    def __init__(self):
        self.file = open(self.OUTPUT_FILE, "w")

    def __del__(self):
        self.file.close()


    # Output Function
    def outputText(self, text):
        self.write(text)


    def outputTermsWithFrequency(self, terms):
        self.writeTableHeader("Rank", "Term", "Frequency")

        rank = 0

        for term, frequency in terms:
            rank += 1
            self.writeTableRow(str(rank), term, str(frequency))

        self.writeTableDelimiter(3)


    def outputNewLine(self):
        self.outputText("")


    # Table Construction
    def writeTableHeader(self, *texts):
        columns = len(texts)

        self.writeTableDelimiter(columns)
        self.writeTableRawRow(texts)
        self.writeTableDelimiter(columns)


    def writeTableRow(self, *texts):
        self.writeTableRawRow(texts)


    def writeTableDelimiter(self, numberOfRows):
        delimiter = "-" * self.ROW_WIDTH;
        delimiterTexts = []

        for i in range(numberOfRows):
            delimiterTexts.append(delimiter)

        self.writeTableRawRow(delimiterTexts)


    def writeTableRawRow(self, texts):
        if len(texts) > 0:
            self.write(self.getRowString(texts))


    def getRowString(self, texts):
        row = "|"

        for text in texts:
            row += self.getCellString(text) + "|"

        return row


    def getCellString(self, text):
        textLength = len(text)
        missingSpaces = self.ROW_WIDTH - textLength
        missingText = " " * missingSpaces
        return  " " + text + missingText + " "


    # File Handling
    def write(self, text):
        self.file.write(text + "\n");