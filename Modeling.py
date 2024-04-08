import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data into a DataFrame
df = pd.read_csv('data.csv', sep=';')

# Remove rows with missing values
df.dropna(inplace=True)

# Feature Engineering: Convert categorical variables into numerical labels
label_encoder = LabelEncoder()
df['Product'] = label_encoder.fit_transform(df['Product'])
df['Region'] = label_encoder.fit_transform(df['Region'])

# Split the data into features and target variable
X = df[['Product', 'Region', 'Quantity']]
y = df['Date']  # Assuming 'Date' as the target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Train Logistic Regression model
logistic_model = LogisticRegression()
logistic_model.fit(X_train_imputed, y_train)

# Make predictions
logistic_predictions = logistic_model.predict(X_test_imputed)

# Evaluate model performance
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
print("Logistic Regression Model Accuracy:", logistic_accuracy)
