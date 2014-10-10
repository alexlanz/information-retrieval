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

        rank = 1

        for term, obj in sorted(terms.items(), key=lambda k: k[1].frequency, reverse=True):
            self.writeTableRow(str(rank), term, str(obj.frequency))
            rank += 1

        self.writeTableDelimiter(3)


    def outputTermsWithRanksInDocuments(self, terms):
        self.outputText("Ranks of the terms")
        self.outputText("------------------\n")

        for term, obj in terms.items():
            self.outputText("\n")
            self.outputText("Term: " + term)
            self.writeTableHeader("Document", "Rank")

            for hit in obj.hits:
                self.writeTableRow(hit.document, str(hit.rank))

            self.writeTableDelimiter(2)


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