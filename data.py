import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

data = pd.DataFrame({
    'past_score':       np.random.randint(40, 100, n),
    'attendance_pct':   np.random.randint(50, 100, n),
    'sleep_hours':      np.random.uniform(4, 9, n).round(1),
    'subject_difficulty': np.random.randint(1, 6, n),  # 1=easy, 5=hard
    'study_hours_needed': np.random.uniform(1, 10, n).round(1)
})

data.to_csv('student_data.csv', index=False)
