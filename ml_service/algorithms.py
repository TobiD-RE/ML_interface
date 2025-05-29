from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

ALGORITHM_MAP = {
    'logistic_regression': LogisticRegression(max_iter=200),
    'random_forest': RandomForestClassifier(),
    'decision_tree': DecisionTreeClassifier(),
    'svm': SVC()
}