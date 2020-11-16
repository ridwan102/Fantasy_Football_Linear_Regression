# Project 2: Regression
Predicting the Fantasy Points in a subsequent game for a NFL Running Back (RB) and Wide Receiver (WR) based off of the statistics from the previous game.

#### Presentation Link: [YouTube](https://www.youtube.com/watch?v=8dBq4N-We7o&t=1s)

## Project Scope

 Features (Independent Variables):
 - RB: Carries/Game,Yards/Carry, Rushing Yards, Rushing Touchdowns, Receptions, Receiving Yards, Receiving Touchdowns, Fumbles
 - WR: Receptions, Receiving Yards, Receiving Touchdowns, Carries/Game,Yards/Carry, Rushing Yards, Rushing Touchdowns, Fumbles

 Dependent Variable (Target): Fantasy Football Points for next game 

## Data
- Analyze data from 2019 season from Pro-Football-Reference (https://www.pro-football-reference.com/)
- Running Backs and Wide Receivers around 500 Rushing/Receiving Yards and above

## Methodology
Apply all regression models as aforementioned and compare Train, Validation, and Test R^2 values to determine best for model. Utilize other regression models such as LASSO and Ridge to Feature Engineer. Create running average of statistics for entire 2019 season (ie.: If Game 3 and predicting Fantasy Points for Game 4, then Game 3 statistics will be an average of games 1, 2, and 3.)

## Deliverable
Present model with the best RSME score to determine how many points model comes within actual score. Reduce RSME as much as possible to create most accurate model. 

## Future Iterations

Aggregate Features on 4-week running averages (ie.: Game 5 features predicting Fantasy Points for Game 6, average statistics from Games 2,3,4, and 5)

## Target Audience
- Fantasy Football Enthusiasts

## Skills:

 * basics of the web (requests, HTML, CSS, JavaScript)
 * `BeautifulSoup` (web scraping)
 * `numpy`, `pandas`, `Jupyter Notebooks`
 * `statsmodels`, `scikit-learn`
 * `Seaborn`
 * `Matplotlib`
 * `Yellowbrick`
