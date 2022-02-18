import csv
import os


class FileWriter:
    articleCsvPath = os.path.join(os.path.dirname(__file__), '../ressource/cleaned/articles.csv')
    linkRelationshipCsvPath = os.path.join(os.path.dirname(__file__), '../ressource/cleaned/linkRelationship.csv')
    externalRelationshipCsvPath = os.path.join(os.path.dirname(__file__),
                                               '../ressource/cleaned/externalRelationship.csv')
    otherRelationshipCsvPath = os.path.join(os.path.dirname(__file__), '../ressource/cleaned/otherRelationship.csv')

    articleCsv = None
    linkRelationshipCsv = None
    externalRelationshipCsv = None
    otherRelationshipCsv = None

    @staticmethod
    def write(csvFile, data):
        csv.writer(csvFile, delimiter='<').writerow(data)

    @staticmethod
    def createFilesIfNotExist():
        if not os.path.exists(FileWriter.articleCsvPath):
            FileWriter.articleCsv = open(FileWriter.articleCsvPath, "a", newline="")
            FileWriter.write(FileWriter.articleCsv, ("articleID:ID", ":LABEL"))

        if not os.path.exists(FileWriter.linkRelationshipCsvPath):
            FileWriter.linkRelationshipCsv = open(FileWriter.linkRelationshipCsvPath, "a", newline="")
            FileWriter.write(FileWriter.linkRelationshipCsv, (":START_ID", "date", "n", ":END_ID", ":TYPE"))

        if not os.path.exists(FileWriter.externalRelationshipCsvPath):
            FileWriter.externalRelationshipCsv = open(FileWriter.externalRelationshipCsvPath, "a", newline="")
            FileWriter.write(FileWriter.externalRelationshipCsv, (":START_ID", "date", "n", ":END_ID", ":TYPE"))

        if not os.path.exists(FileWriter.otherRelationshipCsvPath):
            FileWriter.otherRelationshipCsv = open(FileWriter.otherRelationshipCsvPath, "a", newline="")
            FileWriter.write(FileWriter.otherRelationshipCsv, (":START_ID", "date", "n", ":END_ID", ":TYPE"))

    @staticmethod
    def removeFilesIfExist():
        if os.path.exists(FileWriter.articleCsvPath):
            os.remove(FileWriter.articleCsvPath)

        if os.path.exists(FileWriter.linkRelationshipCsvPath):
            os.remove(FileWriter.linkRelationshipCsvPath)

        if os.path.exists(FileWriter.externalRelationshipCsvPath):
            os.remove(FileWriter.externalRelationshipCsvPath)

        if os.path.exists(FileWriter.otherRelationshipCsvPath):
            os.remove(FileWriter.otherRelationshipCsvPath)
