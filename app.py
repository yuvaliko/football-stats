
from flask import Flask, render_template, request, redirect
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

data = {
    "Date": [],
    "Match": [],
    "Jersey Number": [],
    "Minutes Played": [],
    "Goals": [],
    "Assists": [],
    "Pass Accuracy (%)": [],
    "Shots on Target": [],
    "Tackles": [],
    "Fouls": [],
    "Player Rating": []
}

stats_df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html', stats=stats_df.to_dict(orient='records'))

@app.route('/add', methods=['POST'])
def add_match():
    global stats_df

    date = request.form['date']
    match = request.form['match']
    jersey_number = int(request.form['jersey_number'])
    minutes_played = int(request.form['minutes_played'])
    goals = int(request.form['goals'])
    assists = int(request.form['assists'])
    pass_accuracy = float(request.form['pass_accuracy'])
    shots_on_target = int(request.form['shots_on_target'])
    tackles = int(request.form['tackles'])
    fouls = int(request.form['fouls'])
    player_rating = float(request.form['player_rating'])

    new_data = {
        "Date": date,
        "Match": match,
        "Jersey Number": jersey_number,
        "Minutes Played": minutes_played,
        "Goals": goals,
        "Assists": assists,
        "Pass Accuracy (%)": pass_accuracy,
        "Shots on Target": shots_on_target,
        "Tackles": tackles,
        "Fouls": fouls,
        "Player Rating": player_rating
    }
    stats_df = stats_df.append(new_data, ignore_index=True)
    return redirect('/')

@app.route('/analyze')
def analyze():
    global stats_df

    if stats_df.empty:
        return "No data available to analyze. Please add match data first."

    # Generate Goals and Assists graph
    plt.figure(figsize=(10, 6))
    plt.bar(stats_df["Match"], stats_df["Goals"], color='blue', label='Goals')
    plt.bar(stats_df["Match"], stats_df["Assists"], bottom=stats_df["Goals"], color='green', label='Assists')
    plt.xlabel("Match")
    plt.ylabel("Goals/Assists")
    plt.title("Goals and Assists per Match")
    plt.legend()
    plt.xticks(rotation=45)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    goals_assists_graph = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('analyze.html', goals_assists_graph=goals_assists_graph)

if __name__ == '__main__':
    app.run(debug=True)
