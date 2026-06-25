#include <Python.h>

int main(){
    Py_Initialize();
    const char* pythonCode = R"(
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arr1d = np.random.randint(10,50,10)
print(arr1d)
print(np.round(np.random.normal(50,10,10)))

print(np.round(np.random.uniform(10,20,4)))
binomial_data = np.random.binomial(n=12, p=0.2, size=10000)
plt.figure(figsize=(7, 4))
sns.histplot(binomial_data, kde=False, discrete=True, color='skyblue')
plt.title('Binomial Distribution (n=12, p=0.2)')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()

print(np.random.poisson(34,9).reshape(3,1,3))
poisson_distribution = np.random.poisson(lam=34, size=10000)

# plot
plt.figure(figsize=(7, 4))
sns.histplot(poisson_distribution, kde=True, color='salmon')
plt.title('Poisson Distribution ($\lambda=34$)')
plt.xlabel("Number of events")
plt.ylabel("Frequency")
plt.show()

print(np.round(np.random.exponential(5,10)))

exponential_data = np.random.exponential(scale=5, size=10000)

# plot
plt.figure(figsize=(7,4))
sns.histplot(exponential_data, kde=True, color='lightgreen')
plt.title('Exponential Distribution (scale=5)')
plt.xlabel('Value / Time Between Events')
plt.ylabel('Frequency')
plt.show()
)";


PyRun_SimpleString(pythonCode);
Py_Finalize();
}