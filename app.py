@app.route('/add', methods=['POST'])
def add_match():
    global stats_df

    try:
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
    except ValueError as e:
        return f"Error in input data: {e}", 400
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500
