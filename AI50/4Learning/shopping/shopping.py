import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    evidence = []
    labels = []
    Months = ["jan", "feb", "mar", "apr", "may", "june", "jul", "aug", "sep", "oct", "nov", "dec"]
    toInt = ["Administrative", "Informational", "ProductRelated", "Month",
              "OperatingSystems", "Browser", "Region", "TrafficType", "VisitorType", "Weekend"]
    toFloat = ["Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
               "BounceRates", "ExitRates", "PageValues", "SpecialDay"]
    
    with open(filename) as f:  # opent he CSV and create DictReader
        reader = csv.DictReader(f)

        for row in reader:  # for each dictionary / row
            tempEvidence = []
            for cell in row:  # check what field it is amd convert accordingly
                if cell == "Revenue":
                    if row[cell] == "TRUE" : labels.append(1)
                    else: labels.append(0)
                elif cell in toInt:
                    if cell == "Month":
                        tempEvidence.append(Months.index(row[cell].lower()))
                    elif cell == "VisitorType":
                        if row[cell] == "Returning_Visitor":tempEvidence.append(1)
                        else: tempEvidence.append(0)
                    elif cell == "Weekend":
                        if row[cell] == "TRUE":tempEvidence.append(1)
                        else: tempEvidence.append(0)
                    else:
                        tempEvidence.append(int(row[cell]))
                elif cell in toFloat:
                    tempEvidence.append(float(row[cell]))
                else: sys.exit(f"{cell} type not coercable.")
         

            evidence.append(tempEvidence)
    
    return (evidence, labels)
    raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    
    model= KNeighborsClassifier(n_neighbors = 1)
    model.fit(evidence, labels)

    return model
    raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positives = 0
    negatives = 0
    totalPositives = 0 
    totalNegatives = 0 
    
    for p, a in zip(predictions, labels):
        if a == 1: totalPositives += 1
        else: totalNegatives += 1
        if p == a:
            if a == 1 : positives += 1
            else: negatives += 1
    
    sensitivity = positives / totalPositives
    specificity = negatives / totalNegatives
    



    return (sensitivity, specificity)
    raise NotImplementedError


if __name__ == "__main__":
    main()
