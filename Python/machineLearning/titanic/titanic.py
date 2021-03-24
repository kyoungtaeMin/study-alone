# Titanic analysis and visualization

# %%
from IPython import get_ipython
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=1.5)

import missingno as msno

# ignore warnings
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
# 데이터 확인


# %%
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# %%
df_train.head(10)

# %%
df_train.shape

# %%
df_train.describe()

# %%
df_test.describe()

# %%
df_train.columns
# %%
for col in df_train.columns:
  msg = 'column: {: >10}\t Percent of NaN value: {: .2f}%'.format(col, 100 * (df_train[col].isnull().sum() / df_train[col].shape[0]))
  print(msg)

# %%
for col in df_test.columns:
  msg = 'column: {: >10}\t Percent of NaN value: {: .2f}%'.format(col, 100 * (df_test[col].isnull().sum() / df_test[col].shape[0]))
  print(msg)
  
# %%
msno.matrix(df=df_train.iloc[:, :], figsize=(8, 8), color=(1, 0.5, 0.2))

# %%
msno.bar(df=df_train.iloc[:, :], figsize=(8, 8), color=(1, 0.5, 0.2))

# %%
msno.bar(df=df_test.iloc[:, :], figsize=(8, 8), color=(0.5, 1, 0.2))

# %%
f, ax = plt.subplots(1, 2, figsize=(15, 8))

df_train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Pie plot - Survived')
ax[0].set_ylabel('')
sns.countplot('Survived', data=df_train, ax=ax[1])
ax[1].set_title('Count plot - Survived')
plt.show()


# %%
# EDA - Pclass


# %%
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).count()

# %%
df_train[['Pclass', 'Survived']].groupby(['Pclass']).sum()

# %%
pd.crosstab(df_train['Pclass'], df_train['Survived'], margins=True).style.background_gradient(cmap='cool')

# %%
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar()

# %%
y_position = 1.02
f, ax = plt.subplots(1, 2, figsize=(15, 8))
df_train['Pclass'].value_counts().plot.bar(color=['#CD7F32', '#FFDF00', '#D3D3D3'], ax=ax[0])
ax[0].set_title('Number of passengers By Pclass', y=y_position)
ax[0].set_ylabel('Count')
sns.countplot('Pclass', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('Pclass : Survived vs Dead', y=y_position)
plt.show()


# %%
# EDA - Sex


# %%
f, ax = plt.subplots(1, 2, figsize=(15, 8))
df_train[['Sex', 'Survived']].groupby(['Sex'], as_index=True).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')
sns.countplot('Sex', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('Sex: Survived vs Dead')
plt.show()

# %%
pd.crosstab(df_train['Sex'], df_train['Survived'], margins=True).style.background_gradient(cmap='summer_r')


# %%
# Both Sex and Pclass


# %%
sns.factorplot('Pclass', 'Survived', hue='Sex', data=df_train, size=6, aspect=1.5)

# %%
sns.factorplot(x='Sex', y='Survived', hue='Pclass', data=df_train, saturation=.5,
               size=9, aspect=1)


# %%
# EDA - Age


# %%
print('Oldest Passenger: {: .1f} years'.format(df_train['Age'].max()))
print('Youngest Passenger: {: .1f} years'.format(df_train['Age'].min()))
print('Average age of Passengers: {: .1f} years'.format(df_train['Age'].mean()))

# %%
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df_train[df_train['Survived'] == 1]['Age'], ax=ax)
sns.kdeplot(df_train[df_train['Survived'] == 0]['Age'], ax=ax)
plt.legend(['Survived == 1', 'Survived == 0'])
plt.show()

# %%
df_train[df_train['Survived'] == 1]['Age'].hist()

# %%
plt.figure(figsize=(8, 6))
df_train['Age'][df_train['Pclass'] == 1].plot(kind='kde')
df_train['Age'][df_train['Pclass'] == 2].plot(kind='kde')
df_train['Age'][df_train['Pclass'] == 3].plot(kind='kde')

plt.xlabel('Age')
plt.title('Age Distribution within classes')
plt.legend(['1st Class', '2nd Class', '3rd Class'])

# %%
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df_train[(df_train['Survived'] == 0) & (df_train['Pclass'] == 1)]['Age'], ax=ax)
sns.kdeplot(df_train[(df_train['Survived'] == 1) & (df_train['Pclass'] == 1)]['Age'], ax=ax)
plt.title('Pclass 1st')
plt.legend(['Survived == 0', 'Survived == 1'])
plt.show()

# %%
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df_train[(df_train['Survived'] == 0) & (df_train['Pclass'] == 2)]['Age'], ax=ax)
sns.kdeplot(df_train[(df_train['Survived'] == 1) & (df_train['Pclass'] == 2)]['Age'], ax=ax)
plt.title('Pclass 2nd')
plt.legend(['Survived == 0', 'Survived == 1'])
plt.show()

# %%
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df_train[(df_train['Survived'] == 0) & (df_train['Pclass'] == 3)]['Age'], ax=ax)
sns.kdeplot(df_train[(df_train['Survived'] == 1) & (df_train['Pclass'] == 3)]['Age'], ax=ax)
plt.title('Pclass 3rd')
plt.legend(['Survived == 0', 'Survived == 1'])
plt.show()

# %%
change_age_range_survive_ratio = []

for i in range(1, 81):
  change_age_range_survive_ratio.append(df_train[df_train['Age'] < i]['Survived'].sum() / len(df_train[df_train['Age'] < i]['Survived']))
  
plt.figure(figsize=(7, 7))
plt.plot(change_age_range_survive_ratio)
plt.title('Survival rate change depending in range of Age', y=1.02)
plt.ylabel('Survival rate')
plt.xlabel('Range of Age(0~x)')
plt.show()


# %%
# Pclass, Sex, Age


# %%
f, ax = plt.subplots(1, 2, figsize=(15, 8))
sns.violinplot('Pclass', 'Age', hue='Survived', data=df_train, scale='count', split=True, ax=ax[0])
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0, 110, 10))

sns.violinplot('Sex', 'Age', hue='Survived', data=df_train, scale='count', split=True, ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0, 110, 10))
plt.show()


# %%
# EDA - Embarked


# %%
f, ax = plt.subplots(1, 1, figsize=(7, 7))
df_train[['Embarked', 'Survived']].groupby(['Embarked'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar(ax=ax)

# %%
f, ax = plt.subplots(2, 2, figsize=(20, 15))
sns.countplot('Embarked', data=df_train, ax=ax[0, 0])
ax[0, 0].set_title('(1) No. of Passengers Boared')

sns.countplot('Embarked', hue='Sex', data=df_train, ax=ax[0, 1])
ax[0, 1].set_title('(2) Male-Female split for embarked')

sns.countplot('Embarked', hue='Survived', data=df_train, ax=ax[1, 0])
ax[1, 0].set_title('(3) Embarked vs Survived')

sns.countplot('Embarked', hue='Pclass', data=df_train, ax=ax[1, 1])
ax[1, 1].set_title('(4) Embarked vs Pclass')

plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()


# %%
# EDA - Family : SibSp + Parch


# %%
df_train['FamilySize'] = df_train['SibSp'] + df_train['Parch'] + 1

# %%
print('Maximum size of Family: ', df_train['FamilySize'].max())
print('Miniimum size of Family: ', df_train['FamilySize'].min())

# %%
f, ax = plt.subplots(1, 3, figsize=(20, 8))
sns.countplot('FamilySize', data=df_train, ax=ax[0])
ax[0].set_title('(1) No. of Passenger Boarded', y=1.02)

sns.countplot('FamilySize', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('(2) Survived countplot depending on FamilySize', y=1.02)

df_train[['FamilySize', 'Survived']].groupby(['FamilySize'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar(ax=ax[2])
ax[2].set_title('(3) Survived rate depending on FamilySize', y=1.02)

plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()


# %%
# EDA - Fare, Cabin, Ticket


# %%
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
g = sns.distplot(df_train['Fare'], color='b', label='Skewness: {: .2f}'.format(df_train['Fare'].skew()), ax=ax)
g = g.legend(loc='best')

# %%
df_train['Fare'] = df_train['Fare'].map(lambda i: np.log(i) if i > 0 else 0)

# %%
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
g = sns.distplot(df_train['Fare'], color='b', label='Skewness: {: .2f}'.format(df_train['Fare'].skew()), ax=ax)
g = g.legend(loc='best')

# %%
df_train['Ticket'].value_counts()


# %%
# Feature Engineering - Fill Null in Age


# %%
df_train['Age'].isnull().sum()

# %%
df_train['Name']

# %%
df_train['Initial'] = df_train['Name'].str.extract('([A-Za-z]+)\.')

# %%
df_test['Initial'] = df_test['Name'].str.extract('([A-Za-z]+)\.')

# %%
pd.crosstab(df_train['Initial'],  df_train['Sex']).T.style.background_gradient(cmap='summer_r')

# %%
df_train['Initial'].replace(['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don', 'Dona'],
                            ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr', 'Mr'], inplace=True)

df_test['Initial'].replace(['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don', 'Dona'],
                            ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr', 'Mr'], inplace=True)

# %%
df_train.groupby('Initial').mean()

# %%
df_train.groupby('Initial')['Survived'].mean().plot.bar()

# %%
df_all  = pd.concat([df_train, df_test])

# %%
df_all

# %%
df_all.groupby('Initial').mean()

# %%
df_train.loc[(df_train['Age'].isnull()) & (df_train['Initial'] == 'Mr'), 'Age'] = 33

# %%
df_train.loc[(df_train['Initial'] == 'Mr'), 'Age']

# %%




df_train.loc[(df_train['Age'].isnull()) & (df_train['Initial'] == 'Mrs'), 'Age'] = 37
df_train.loc[(df_train['Age'].isnull()) & (df_train['Initial'] == 'Miss'), 'Age'] = 22
df_train.loc[(df_train['Age'].isnull()) & (df_train['Initial'] == 'Master'), 'Age'] = 5
df_train.loc[(df_train['Age'].isnull()) & (df_train['Initial'] == 'Other'), 'Age'] = 45

# %%
df_test.loc[(df_test['Age'].isnull()) & (df_test['Initial'] == 'Mrs'), 'Age'] = 37
df_test.loc[(df_test['Age'].isnull()) & (df_test['Initial'] == 'Miss'), 'Age'] = 22
df_test.loc[(df_test['Age'].isnull()) & (df_test['Initial'] == 'Master'), 'Age'] = 5
df_test.loc[(df_test['Age'].isnull()) & (df_test['Initial'] == 'Other'), 'Age'] = 45
df_test.loc[(df_test['Age'].isnull()) & (df_test['Initial'] == 'Mr'), 'Age'] = 33

# %%
df_train['Age'].isnull().sum()

# %%
df_test['Age'].isnull().sum()


# %%
# Full Null in Embarked and categorize Age


# %%
df_train['Embarked'].isnull().sum()

# %%
df_train['Embarked'].fillna('S', inplace=True)

# %%
df_train['Embarked'].isnull().sum()

# %%
df_train['Age_cat'] = 0

# %%
df_train

# %%
df_train.loc[(df_train['Age'] <= 10), 'Age_cat'] = 0
df_train.loc[(df_train['Age'] >= 10) & (df_train['Age'] <= 20), 'Age_cat'] = 1
df_train.loc[(df_train['Age'] >= 20) & (df_train['Age'] <= 30), 'Age_cat'] = 2
df_train.loc[(df_train['Age'] >= 30) & (df_train['Age'] <= 40), 'Age_cat'] = 3
df_train.loc[(df_train['Age'] >= 40) & (df_train['Age'] <= 50), 'Age_cat'] = 4
df_train.loc[(df_train['Age'] >= 50) & (df_train['Age'] <= 60), 'Age_cat'] = 5
df_train.loc[(df_train['Age'] >= 60) & (df_train['Age'] <= 70), 'Age_cat'] = 6
df_train.loc[(df_train['Age'] >= 70), 'Age_cat'] = 7

# %%

df_test.loc[(df_train['Age'] <= 10), 'Age_cat'] = 0
df_test.loc[(df_train['Age'] >= 10) & (df_test['Age'] <= 20), 'Age_cat'] = 1
df_test.loc[(df_train['Age'] >= 20) & (df_test['Age'] <= 30), 'Age_cat'] = 2
df_test.loc[(df_train['Age'] >= 30) & (df_test['Age'] <= 40), 'Age_cat'] = 3
df_test.loc[(df_train['Age'] >= 40) & (df_test['Age'] <= 50), 'Age_cat'] = 4
df_test.loc[(df_train['Age'] >= 50) & (df_test['Age'] <= 60), 'Age_cat'] = 5
df_test.loc[(df_train['Age'] >= 60) & (df_test['Age'] <= 70), 'Age_cat'] = 6
df_test.loc[(df_train['Age'] >= 70), 'Age_cat'] = 7

# %%
df_train.head()

# %%
def category_age(x):
  if x < 10:
    return 0
  elif x < 20:
    return 1
  elif x < 30:
    return 2
  elif x < 40:
    return 3
  elif x < 50:
    return 4
  elif x < 60:
    return 5
  elif x < 70:
    return 6
  else:
    return 7

# %%
df_train['Age_cat2'] = df_train['Age'].apply(category_age)

# %%
(df_train['Age_cat'] == df_train['Age_cat2']).all()

# %%
df_train.drop(['Age', 'Age_cat2'], axis=1, inplace=True)
df_test.drop(['Age'], axis=1, inplace=True)

# %%
