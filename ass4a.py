
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score
)

# 1. Load and preprocess CSV
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = df.drop("customerID", axis=1)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

X = pd.get_dummies(df.drop("Churn", axis=1))
y = df["Churn"]

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Supervised Learning - Decision Tree
model1 = DecisionTreeClassifier(max_depth=5, random_state=42)
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

# 5. Semi-Supervised Learning - Self Training
semi_y = y_train.to_numpy().copy()
np.random.seed(42)

indices = np.random.choice(
    len(semi_y), int(0.8 * len(semi_y)), replace=False
)
semi_y[indices] = -1

model2 = SelfTrainingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5, random_state=42),
    threshold=0.75,
    max_iter=10
)
model2.fit(X_train, semi_y)
pred2 = model2.predict(X_test)

# 6. Ensemble Learning - Random Forest
model3 = RandomForestClassifier(n_estimators=100, random_state=42)
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

# 7. Evaluate models
def evaluate(y_true, pred):
    return [
        accuracy_score(y_true, pred),
        precision_score(y_true, pred, zero_division=0),
        recall_score(y_true, pred, zero_division=0),
        f1_score(y_true, pred, zero_division=0)
    ]

results = pd.DataFrame(
    [
        evaluate(y_test, pred1),
        evaluate(y_test, pred2),
        evaluate(y_test, pred3)
    ],
    columns=["Accuracy", "Precision", "Recall", "F1-Score"],
    index=["Decision Tree", "Self-Training", "Random Forest"]
)

print("\nModel Comparison:")
print(results.round(4))

print("\nBest Model:", results["F1-Score"].idxmax())
