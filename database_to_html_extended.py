#!/usr/bin/env python3
"""
Extended Sports Database to HTML Converter
Handles professional sports, college sports, tennis rankings, and racing
"""

import sqlite3
from datetime import datetime

class SportsDatabase:
    def __init__(self, db_path='sports_records.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def get_all_teams(self):
        """Fetch all teams from the database"""
        self.cursor.execute('SELECT * FROM teams ORDER BY league, rank')
        return self.cursor.fetchall()
    
    def get_teams_by_league(self, league):
        """Fetch teams for a specific league"""
        self.cursor.execute(
            'SELECT * FROM teams WHERE league = ? ORDER BY rank',
            (league,)
        )
        return self.cursor.fetchall()
    
    def get_all_leagues(self):
        """Get list of all unique leagues"""
        self.cursor.execute('SELECT DISTINCT league FROM teams ORDER BY league')
        return [row[0] for row in self.cursor.fetchall()]
    
    def close(self):
        """Close database connection"""
        self.conn.close()

class HTMLGenerator:
    def __init__(self, db):
        self.db = db
        self.html_content = ""
        self.league_emojis = {
            'NFL': '🏈',
            'NBA': '🏀',
            'MLB': '⚾',
            'NHL': '🏒',
            'Tennis (Men)': '🎾',
            'Tennis (Women)': '🎾',
            'NCAAM': '🏀',
            'NCAAFB': '🏈',
            'NASCAR': '🏁',
            'MLS': '⚽'
        }
    
    def generate_html(self, filename='sports_records.html'):
        """Generate complete HTML report"""
        self.html_content = self._create_header()
        
        leagues = self.db.get_all_leagues()
        for league in leagues:
            teams = self.db.get_teams_by_league(league)
            self.html_content += self._create_league_section(league, teams)
        
        self.html_content += self._create_footer()
        
        with open(filename, 'w') as f:
            f.write(self.html_content)
        
        print(f"HTML report generated: {filename}")
        return filename
    
    def _create_header(self):
        """Create HTML header with styling"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comprehensive Sports Records & Rankings</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.95;
        }
        
        .league-section {
            margin-bottom: 35px;
        }
        
        .league-title {
            background: rgba(255, 255, 255, 0.95);
            padding: 15px 20px;
            border-radius: 8px 8px 0 0;
            border-left: 5px solid;
            font-size: 1.4em;
            font-weight: bold;
            color: #333;
            margin-bottom: 0;
        }
        
        .league-section.nfl .league-title { border-left-color: #003d7a; }
        .league-section.nba .league-title { border-left-color: #1d428a; }
        .league-section.mlb .league-title { border-left-color: #12130f; }
        .league-section.nhl .league-title { border-left-color: #000; }
        .league-section.tennis-men .league-title { border-left-color: #00a651; }
        .league-section.tennis-women .league-title { border-left-color: #d61e3e; }
        .league-section.ncaam .league-title { border-left-color: #0066cc; }
        .league-section.ncaafb .league-title { border-left-color: #663300; }
        .league-section.nascar .league-title { border-left-color: #ffcc00; }
        .league-section.mls .league-title { border-left-color: #3d195b; }
        
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
            border-radius: 0 0 8px 8px;
            overflow: hidden;
        }
        
        thead {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        th {
            padding: 15px;
            text-align: left;
            font-weight: 600;
            color: #333;
            border-bottom: 2px solid #ddd;
        }
        
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }
        
        tbody tr:hover {
            background-color: #f8f9fa;
            transition: background-color 0.2s ease;
        }
        
        tbody tr:last-child td {
            border-bottom: none;
        }
        
        .team-name {
            font-weight: 500;
            color: #333;
        }
        
        .stat {
            text-align: center;
            font-weight: bold;
        }
        
        .wins {
            color: #27ae60;
        }
        
        .losses {
            color: #e74c3c;
        }
        
        .draws {
            color: #f39c12;
        }
        
        .points {
            color: #2980b9;
        }
        
        .win-pct {
            background: #f0f0f0;
            border-radius: 4px;
            text-align: center;
            font-weight: 500;
        }
        
        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
            opacity: 0.9;
        }
        
        .summary {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            text-align: center;
            font-size: 0.95em;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8em;
            }
            
            th, td {
                padding: 10px 8px;
                font-size: 0.85em;
            }
            
            .league-title {
                font-size: 1.1em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏆 Comprehensive Sports Database</h1>
            <p>Professional & College Sports • International Rankings</p>
            <p style="font-size: 0.9em; margin-top: 10px;">NFL • NBA • MLB • NHL • Tennis • College Basketball • College Football • NASCAR • MLS</p>
            <p style="font-size: 0.85em; opacity: 0.9; margin-top: 5px;">Updated: ''' + datetime.now().strftime('%B %d, %Y at %I:%M %p') + '''</p>
        </div>
'''
    
    def _create_league_section(self, league, teams):
        """Create HTML section for a league"""
        league_class = league.lower().replace(' ', '-').replace('(', '').replace(')', '')
        emoji = self.league_emojis.get(league, '📊')
        
        league_display_names = {
            'NFL': 'National Football League',
            'NBA': 'National Basketball Association',
            'MLB': 'Major League Baseball',
            'NHL': 'National Hockey League',
            'Tennis (Men)': 'Tennis - Men\'s Rankings (ATP)',
            'Tennis (Women)': 'Tennis - Women\'s Rankings (WTA)',
            'NCAAM': 'NCAA Men\'s Basketball',
            'NCAAFB': 'NCAA Football',
            'NASCAR': 'NASCAR Cup Series',
            'MLS': 'Major League Soccer'
        }
        
        display_name = league_display_names.get(league, league)
        
        html = f'\n        <div class="league-section {league_class}">\n'
        html += f'            <h2 class="league-title">{emoji} {display_name}</h2>\n'
        html += f'            <div class="summary">{len(teams)} entries</div>\n'
        html += '            <table>\n'
        html += '                <thead>\n'
        html += '                    <tr>\n'
        html += '                        <th>#</th>\n'
        html += '                        <th>Name</th>\n'
        
        # Determine which columns to show based on league
        if league in ['Tennis (Men)', 'Tennis (Women)']:
            html += '                        <th>Points</th>\n'
        elif league == 'NASCAR':
            html += '                        <th>Wins</th>\n'
            html += '                        <th>Points</th>\n'
        elif league == 'MLS':
            html += '                        <th>Wins</th>\n'
            html += '                        <th>Losses</th>\n'
            html += '                        <th>Draws</th>\n'
            html += '                        <th>Points</th>\n'
        else:
            html += '                        <th>Wins</th>\n'
            html += '                        <th>Losses</th>\n'
            html += '                        <th>Win %</th>\n'
        
        html += '                    </tr>\n'
        html += '                </thead>\n'
        html += '                <tbody>\n'
        
        for idx, team in enumerate(teams, 1):
            team_id, team_name, team_league, wins, losses, draws, points, rank, _ = team
            
            html += '                    <tr>\n'
            html += f'                        <td class="stat">{idx}</td>\n'
            html += f'                        <td class="team-name">{team_name}</td>\n'
            
            if league in ['Tennis (Men)', 'Tennis (Women)']:
                html += f'                        <td class="stat points">{points:,}</td>\n'
            elif league == 'NASCAR':
                html += f'                        <td class="stat wins">{wins}</td>\n'
                html += f'                        <td class="stat points">{points}</td>\n'
            elif league == 'MLS':
                html += f'                        <td class="stat wins">{wins}</td>\n'
                html += f'                        <td class="stat losses">{losses}</td>\n'
                html += f'                        <td class="stat draws">{draws}</td>\n'
                html += f'                        <td class="stat points">{points}</td>\n'
            else:
                total_games = wins + losses
                win_pct = (wins / total_games * 100) if total_games > 0 else 0
                html += f'                        <td class="stat wins">{wins}</td>\n'
                html += f'                        <td class="stat losses">{losses}</td>\n'
                html += f'                        <td class="stat win-pct">{win_pct:.1f}%</td>\n'
            
            html += '                    </tr>\n'
        
        html += '                </tbody>\n'
        html += '            </table>\n'
        html += '        </div>\n'
        
        return html
    
    def _create_footer(self):
        """Create HTML footer"""
        return '''
        <div class="footer">
            <p>🏆 Comprehensive Sports Rankings Database</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Data provided by SportRadar API • All times in EST</p>
        </div>
    </div>
</body>
</html>
'''

def main():
    db = SportsDatabase('sports_records.db')
    generator = HTMLGenerator(db)
    output_file = generator.generate_html('sports_records.html')
    
    print("\n" + "="*60)
    print("COMPREHENSIVE SPORTS DATABASE")
    print("="*60)
    
    leagues = db.get_all_leagues()
    for league in leagues:
        teams = db.get_teams_by_league(league)
        print(f"\n{league}: {len(teams)} entries")
        if teams:
            print(f"  Leading: {teams[0][1]}")
    
    db.close()
    print(f"\n✅ HTML file created: {output_file}")

if __name__ == '__main__':
    main()
