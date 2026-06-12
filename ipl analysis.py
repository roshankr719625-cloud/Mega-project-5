import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Match": [1, 2, 3],
    "Team": ["MI", "CSK", "MI"],
    "Opponent": ["CSK", "RCB", "RCB"],
    "Runs": [180, 170, 150],
    "Wickets": [6, 7, 8],
    "Winner": ["MI", "CSK", "CSK"],
    "Batsman": ["Rohit", "Dhoni", "Kohli"],
    "Bowler": ["Bumrah", "Chahal", "Bumrah"],
    "is_wicket": [0, 1, 1]
}
df = pd.DataFrame(data)
wins = df["Winner"].value_counts()
print(wins)

# top_batsman = df.groupby("Batsman")["Runs"].sum().sort_values(ascending=False).head(5)
# print(top_batsman)


# wickets = df[df["is_wicket"] == 1]
# top_bowlers = wickets["Bowler"].value_counts().head(5)
# print(top_bowlers)

# toss_win = df[df["Toss_winner"] == df["Winner"]]
# impact = len(toss_win) / len(df) * 100
# print(impact) 

# avg_runs = df["Runs"].mean()
# print(avg_runs)

df["Winner"].value_counts().plot(kind="bar")
plt.title("Ipl Team Wins")
plt.show()





