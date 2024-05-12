from flask import Blueprint, render_template
from .football_data import display_upcoming_matches

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('Présentation.html')

@main.route('/soccer')
def soccer():
    return render_template('pageSoccer.html')

@main.route('/premier-league')
def premier_league():
    df_matches = display_upcoming_matches(39, 2023)
    matches = df_matches.to_dict('records') if not df_matches.empty else []
    return render_template('PremierLeague.html', matches=matches)

@main.route('/matchup/')
def matchup():
    return render_template('PageMatchup.html')


   
if __name__ == '__main__':
    main.run(debug=True)
