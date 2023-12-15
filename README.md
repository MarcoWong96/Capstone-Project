# Capstone Project
# Modelling Football Players Valuation in the Top 5 Leagues

--------------------------------------------------------

### Introduction
--------------------------------------------------------
Within the evergrowing sphere of sport, people are looking for new tools to gain a competitive edge. The recent advancement of nutrition has allowed many of the top athletes to stay in their prime well into their thirties. Historically, this would be the rare exception, not the rule. Lebron James, Steph Curry, Novak Djokovic, Serena Williams, Cristiano Ronaldo, Lionel Messi are all examples of the positive effects nutrition, combined with many other advancements, has had on the longevity of their careers. Whilst many sports have started to implement data tools to drive their decision making, I believe there is a massive opportunity for growth in this domain, especially in European Football.

North American sports teams have made greater strides in utilizing the capabilities of data driven tools. The movie 'Moneyball', a biographical film released in 2011, tells a story of a baseball team - the Oakland Athletics - using a sabermetrics approach to build an undervalued but talented team. Given the team's measly budget, the team overperformed greatly and went on a unprecedented 20 game winning spree, but ended up losing in the latter stage of the world series. This movie perfectly encapsulates the power of data in a historically dataless sporting world, that data driven insights can be truly a game changer. Ultimately, I am convinced that within the realm of European Football, the potential of data remains significantly untapped.

My project is centered on valuing football players. Over the last two decades, transfer fees have soared dramatically: from the world record transfer fee of €46.00m for Rio Ferdinand in 2003 to €222.00m for Neymar in 2017, marking a 482% increase in just 14 years! This surge has often left the public confused, questioning the rationale behind these skyhigh figures fee, as many football player fees can be worth more than their whole neighborhoods house value.

Additionally, financial efficiency is imperative for a successful football club. On top of financial requirements within a club and their shareholders, tightening regulations like Financial Fair Play (FFP) has forced clubs to rethink their transfer strategies. Overlooking these regulations have led to tremendous penalties, with Juventus and Everton F.C. suffering 10 points deductions due to violations of FFP. Nowadays, securing valuable players is more crucial than ever before and this can be achieved through accurate player valuations.

My aim is to develop a model that uses the players season statistics to predict their market valuation. Traditional models have primarily relied on using basic metrics such as goals scored, matches played, age to determine market value, which I find too basic for an accurate assessment. My approach involves diving into more intricate metrics, including market trends, specific performance metrics, and contextual analysis. This deeper exploration intends to provide a fuller picture of a player's value, surpassing the accuracy of current conventional models.

This model will benefit multiple stakeholders within football. It offers clubs a reliable method to aseess player value, aiding in the valuation of potential signings and providing insights into the worth of their existing players. By offering enhanced information, this model equips clubs with valuable data that can inform their decision making processes.

### Project Organization (In progress)
--------------------------------------------------------
Notebooks (FOLDER)<br>
-- Initial EDA<br> 
-- FinalEDA+InitialModelling
-- Modelling<br>
-- Modelling 2<br>
-- Modelling 3<br>
-- Data (FOLDER)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-- 2021-2022 Football Player Stats.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;-- 2022-2023 Football Player Stats.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;-- player_valuations.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;-- players.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;-- Transfer fees (to be found)<br>

Presentations (FOLDER)<br>
-- Presentation 1<br>
-- Presentation 2<br>
-- Presentation 3<br>



### Datasets
--------------------------------------------------------
-- 2021-2022 Football Player Stats.csv (2921 rows x 143 columns)<br>
-- https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats/data<br>
-- 2022-2023 Football Player Stats.csv (2689 rows x 124 columns)<br>
-- https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats/code<br>
-- player_valuations.csv (440643 rows x 9 columns)<br>
-- https://www.kaggle.com/datasets/davidcariboo/player-scores?select=player_valuations.csv<br>
-- players.csv (30302 rows x 23 columns)<br>
-- https://www.kaggle.com/datasets/davidcariboo/player-scores?select=players.csv<br>
-- Transfer fees.csv (to be found)<br>



### Exploratory Data Analysis (EDA)
--------------------------------------------------------
As our player statistics and player valuation datasets are all seperated, our initial exploratory data analysis (EDA) largely consists on looking at the relationships between our features. After drawing up a correlation matrix between our feature variables, we can see some interesting patterns between our features:
- There are many highly correlated blocks in our correlation matrix. This indicates the nature of the dataset having many overlapping features. For example, passes completed, passes attempted, pass completion percentage, (passes) total distance are all similar features and will likely have a high correlation with each other.<br>
- There are also many blocks of negative correlations. This may allude to the specialist nature of certain positions in football. For example, the most negative pair of statistics are 'Touches in Final third' and 'Touches in first third' - this means a player that has many touches in the final third, will likely have very little in their own third.<br>

With regards to our target variable 'player valuation', our dataset encompasses players from over 10 leagues. This is not within the scope of this project, however, we can still look at the distribution of the valuation, even though it will likely skew the analysis to the right.

Here are some statistics regarding the distribution:

- The mean valuation per player is 4,032,582.<br>
- The median valuation is 800,000. <br>
- The maximum valuation is 180,000,000. <br>

Note that this valuation dataset has information over 20 years. Due to inflation, prices have been rising year on year. Since our analysis is only on players in the last two years, the distribution for our analysis should be less skewed compared to the described statistics above.


### Modelling
--------------------------------------------------------
Our first baseline model has been completed. Using a linear regression, we have achieved a 5 fold cross validation R squared score of 0.375 and a 5 fold cross validation mean absolute error score of 7,661,307. Whilst this is quite a poor model in terms of accuracy, it has lead to some insight on which variables have high or low correlation. 

High positive correlation coefficients include:<br>
GcaDef:defensive actions that lead to a goal<br>
Comp_Premier League: player in premier league<br>
90's: MMnutes played divided by 90<br>
Pos_FW: Position of player is forward, have very high correlation coefficients.<br>

High negative correlation coefficients include:<br>
GCA: Goal creating action<br>
Comp_Ligue 1: Player in Ligue 1<br>
TKL: Number of players tackled<br>
BLKPass: Number of times blocking a pass by standing in its path<br>

Our next step is to perform feature selection, and decide on different models/ hyperparameters.

### Conclusion
--------------------------------------------------------
