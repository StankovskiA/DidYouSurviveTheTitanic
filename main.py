import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv("C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/titanic/train.csv", index_col=0)
target = df['Survived']
df.drop('Survived', axis='columns', inplace=True)

# We need to give numeric values to these two columns
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

df['sex'] = le_sex.fit_transform(df['Sex'])
df['embarked'] = le_embarked.fit_transform(df['Embarked'])
df.drop(['Sex', 'Embarked', 'Ticket', 'Cabin', 'Name', 'Fare'], axis='columns', inplace=True)


#Based on the mean of Ages column we replace the NaN to 30 so we can work with the decision tree
df['Age'] = df['Age'].fillna(30)

model = tree.DecisionTreeClassifier()
model.fit(df, target)

tdf= pd.read_csv("C:/Users/Asus/PycharmProjects/TitanicPredictionWebsite/DidYouSurvive/titanic/train.csv", index_col=0)
tdf['Age'] = tdf['Age'].fillna(30)
tdf['sex'] = le_sex.fit_transform(tdf['Sex'])
tdf['embarked'] = le_embarked.fit_transform(tdf['Embarked'])
tdf.drop(['Sex', 'Embarked', 'Ticket', 'Cabin', 'Name', 'Fare'], axis='columns', inplace=True)
