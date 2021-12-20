import pandas as pd
data = {
  "age": [60, 45, 33, 75, 22, 27, 30],
  "qualified": [True, True, False, True, False, False, False]
}

df=pd.DataFrame(data)
print(df)
