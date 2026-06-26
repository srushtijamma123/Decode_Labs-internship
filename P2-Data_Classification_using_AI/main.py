from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)
print("First Flower:", iris.data[0])
print("First Flower Label:", iris.target[0])
X = iris.data      # Features
y = iris.target    # Labels

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 60)
print("🌸 DATA CLASSIFICATION USING AI 🌸")
print("=" * 60)

print(f"\n✅ Model Accuracy : {accuracy * 100:.2f}%")
print("\n🎉 Model trained successfully!")

print("\n🔍 Sample Prediction")
print("-" * 30)

print("\nEnter Flower Measurements")

sepal_length = float(input("Enter Sepal Length (cm): "))
sepal_width = float(input("Enter Sepal Width (cm): "))
petal_length = float(input("Enter Petal Length (cm): "))
petal_width = float(input("Enter Petal Width (cm): "))

sample = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(sample)

print("\n🔍 Flower Details")
print("-" * 30)

print(f"Sepal Length : {sepal_length} cm")
print(f"Sepal Width  : {sepal_width} cm")
print(f"Petal Length : {petal_length} cm")
print(f"Petal Width  : {petal_width} cm")

print(f"\n🌼 Predicted Flower : {iris.target_names[prediction[0]].title()}")