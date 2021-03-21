# Titanic analysis and visualization

# %%
from IPython import get_ipython
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2)

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
