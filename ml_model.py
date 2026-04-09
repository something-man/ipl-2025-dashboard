import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from data_generator import generate_historical_matches, get_teams

class MatchPredictor:
    def __init__(self):
        self.model = LogisticRegression()
        self.encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        self.teams = get_teams()
        self._train_model()

    def _train_model(self):
        # Generate 1000 simulated historical matches for training
        df = generate_historical_matches(1000)
        
        # Prepare features (Team1, Team2) and target (Winner)
        X = df[['Team1', 'Team2']]
        y = (df['Winner'] == df['Team1']).astype(int) # 1 if Team1 won, 0 if Team2 won
        
        # Fit encoder and transform
        X_encoded = self.encoder.fit_transform(X)
        self.model.fit(X_encoded, y)

    def predict_winner(self, team1, team2):
        if team1 == team2:
            return "Draw", 50.0
            
        # Prepare input
        input_data = pd.DataFrame({'Team1': [team1], 'Team2': [team2]})
        input_encoded = self.encoder.transform(input_data)
        
        # Predict probability
        prob = self.model.predict_proba(input_encoded)[0]
        
        # Output logic
        if prob[1] > 0.5:
            winner = team1
            win_prob = round(prob[1] * 100, 2)
        else:
            winner = team2
            win_prob = round(prob[0] * 100, 2)
            
        return winner, win_prob
