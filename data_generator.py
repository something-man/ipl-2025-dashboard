import pandas as pd
import numpy as np

# Set seed for reproducibility for the dummy historical data
np.random.seed(42)

TEAMS = [
    "Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Delhi Capitals",
    "Rajasthan Royals",
    "Punjab Kings",
    "Lucknow Super Giants",
    "Gujarat Titans"
]

def get_teams():
    return TEAMS

def get_points_table():
    # IPL 2025 Final League Points Table
    data = [
        ["Punjab Kings", 14, 9, 4, 1, 19, 0.65],
        ["Royal Challengers Bengaluru", 14, 9, 4, 1, 19, 0.42],
        ["Gujarat Titans", 14, 8, 5, 1, 17, 0.81],
        ["Mumbai Indians", 14, 8, 6, 0, 16, 0.35],
        ["Chennai Super Kings", 14, 7, 7, 0, 14, 0.12],
        ["Rajasthan Royals", 14, 7, 7, 0, 14, -0.05],
        ["Kolkata Knight Riders", 14, 6, 8, 0, 12, -0.21],
        ["Sunrisers Hyderabad", 14, 5, 9, 0, 10, -0.45],
        ["Lucknow Super Giants", 14, 4, 10, 0, 8, -0.80],
        ["Delhi Capitals", 14, 3, 11, 0, 6, -1.15]
    ]
    df = pd.DataFrame(data, columns=["Team", "Matches", "Wins", "Losses", "No Result", "Points", "NRR"])
    df.index = df.index + 1
    return df

def get_top_batsmen():
    # IPL 2025 Orange Cap Standings
    data = {
        "Player": ["Sai Sudharsan", "Virat Kohli", "Shubman Gill", "Yashasvi Jaiswal", "Suryakumar Yadav"],
        "Team": ["GT", "RCB", "GT", "RR", "MI"],
        "Runs": [759, 715, 680, 595, 550],
        "Strike Rate": [141.5, 155.2, 149.8, 162.3, 175.4],
        "Average": [54.2, 59.5, 48.5, 42.5, 45.8]
    }
    df = pd.DataFrame(data)
    return df

def get_top_bowlers():
    # IPL 2025 Purple Cap Standings
    data = {
        "Player": ["Prasidh Krishna", "Noor Ahmad", "Josh Hazlewood", "Trent Boult", "Sai Kishore"],
        "Team": ["GT", "CSK", "RCB", "MI", "GT"],
        "Wickets": [25, 24, 21, 21, 19],
        "Economy": [8.1, 7.2, 7.5, 8.0, 6.9],
        "Average": [18.2, 19.5, 20.1, 21.0, 22.5]
    }
    df = pd.DataFrame(data)
    return df

def get_latest_match():
    # IPL 2025 Grand Final: RCB vs PBKS
    # RCB won by 6 runs
    overs = list(range(1, 21))
    
    # RCB Batting first - scored ~ 190
    rcb_runs_per_over = [6, 12, 8, 14, 9, 11, 5, 6, 8, 10, 15, 7, 12, 9, 16, 8, 11, 14, 6, 13]
    rcb_cum = np.cumsum(rcb_runs_per_over) # Total: 200
    
    # PBKS Chasing - scored ~ 194
    pbks_runs_per_over = [8, 10, 6, 15, 7, 9, 8, 12, 5, 8, 14, 9, 10, 11, 12, 13, 7, 15, 8, 7]
    pbks_cum = np.cumsum(pbks_runs_per_over) # Total: 194
    
    df = pd.DataFrame({
        "Over": overs,
        "RCB Runs": rcb_cum,
        "PBKS Runs": pbks_cum
    })
    
    match_info = {
         "Team 1": "Royal Challengers Bengaluru",
         "Team 2": "Punjab Kings",
         "Score 1": f"{rcb_cum[-1]}/7",
         "Score 2": f"{pbks_cum[-1]}/9",
         "Winner": "Royal Challengers Bengaluru (by 6 runs)"
    }
    
    return match_info, df

def get_toss_analysis():
    # Final IPL 2025 toss data impact
    labels = ['Won Toss, Won Match', 'Won Toss, Lost Match']
    values = [38, 62] # Defending actually worked better in pressure games
    
    decision_labels = ['Bat First Win %', 'Bowl First Win %']
    decision_values = [52, 48] # Bat first had slight advantage
    
    return (labels, values), (decision_labels, decision_values)

def generate_historical_matches(num_matches=1000):
    match_data = []
    # Simulating data that perfectly aligns with RCB being champions
    for _ in range(num_matches):
        t1, t2 = np.random.choice(TEAMS, 2, replace=False)
        toss_winner = np.random.choice([t1, t2])
        
        strengths = {
            "Royal Challengers Bengaluru": 1.25,
            "Punjab Kings": 1.2,
            "Gujarat Titans": 1.15,
            "Mumbai Indians": 1.10,
            "Chennai Super Kings": 1.05,
            "Rajasthan Royals": 1.0,
            "Kolkata Knight Riders": 0.95,
            "Sunrisers Hyderabad": 0.9,
            "Lucknow Super Giants": 0.85,
            "Delhi Capitals": 0.8
        }
        
        win_prob_t1 = 0.5 * (strengths[t1] / strengths[t2])
        winner = t1 if np.random.random() < win_prob_t1 else t2
        
        match_data.append({
            "Team1": t1,
            "Team2": t2,
            "TossWinner": toss_winner,
            "Winner": winner
        })
        
    return pd.DataFrame(match_data)
