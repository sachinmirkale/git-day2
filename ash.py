import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Income': [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    'BirthRate': [35, 32, 28, 25, 22, 18, 15]
}

df = pd.DataFrame(data)

# Create regression plot
sns.lmplot(
    data=df,
    x='Income',
    y='BirthRate',
    height=5,
    aspect=1.5
)

plt.title('Income vs Birth Rate')
plt.show()