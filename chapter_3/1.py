import numpy as np

security_breaches = np.random.randint(0, 100, size=(3, 5))

print(security_breaches)
"""
To keep a summary array 2D rather than flat, 
set keepdims=True when calling the aggregating method.
"""
print("breaches per year", security_breaches.sum(axis=0))
print("breaches per client", security_breaches.sum(axis=1))


print("min breaches in gen", security_breaches.min())
print("max breaches in gen", security_breaches.max())
print("avg in a year", security_breaches.mean())
print("avg per year", security_breaches.mean(axis=0))
print("avg per client", security_breaches.mean(axis=1))

print("soma cumulativa", security_breaches.cumsum(axis=1))

# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)
print(cumulative_monthly_industry_sales)

# Plot each industry's cumulative sales by month as separate lines
plt.plot(
    np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label="Liquor Stores"
)
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label="Restaurants")
plt.plot(
    np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label="Department stores"
)
plt.legend()
plt.show()
