# Capstone Project
# Modelling Football Players Valuation in the Top 5 Leagues

--------------------------------------------------------


### Introduction
--------------------------------------------------------
To some, European football is just a sport - ninety minutes on a grass pitch where one team tries to score more than the other. But to hundreds of millions of people world wide, football is so much more than that. Football is all you had growing up, football is your families way out of poverty, football is life. For many of us, football is a major part of our lives and supporting your childhood club can almost be an irrational attachment.

In November 2023, a Boca Juniors fan committed suicide after his team lost in the Copa final. Football clubs are not a traditional business as so many people rely on them for entertainment, but also their personal well being. And that’s why it is imperative for a team to be ran properly. One huge aspect of football management is finances. 

Within the last few years, we have seen many teams penalized for breaking financial regulations. Most notably, Juventus suffered a 10 point deduction and were prohibited from participating in European competitions for a year. This punishment alone is worth tens of millions of dollars.

This comes to my project: my project is centered on valuing football players. Over the last two decades, transfer fees have soared dramatically: from the world record transfer fee of €46.00m for Rio Ferdinand in 2003 to €222.00m for Neymar in 2017, marking a 482% increase in just 14 years! This surge has often left the public confused, questioning the rationale behind these skyhigh figures fee, as many football player fees can be worth more than their whole neighborhoods house value. Nowadays, securing valuable players is more crucial than ever before and this can be achieved through accurate player valuations.

My aim is to develop a model that uses the players last season statistics to predict their market valuation. Traditional models have primarily relied on using basic metrics such as goals scored, matches played, age to determine market value, which I find too basic for an accurate assessment. My approach involves diving into more intricate metrics, including market trends, specific performance metrics, and contextual analysis. This deeper exploration intends to provide a fuller picture of a player's value, surpassing the accuracy of current conventional models. Additionally, we can dive deep into the most important features for determining valuation. Is it goals scored? Or perhaps tackles per 90 minutes? These project will provide insights into these features.

This model will benefit multiple stakeholders within football. It offers clubs a reliable method to aseess player value, aiding in the valuation of potential signings and providing insights into the worth of their existing players. By offering enhanced information, this model equips clubs with valuable data that can inform their decision making processes. The potential impact is enormous - a financially sustainable club that can divert their finances to other operations. Additionally, fan relations may improve greatly.


Project Directory
│
├── Notebooks
│   ├── Inspiration.ipynb               <- Notebook 0 - Inspiration for this project, initial thoughts
│   ├── Initial_EDA.ipynb               <- Notebook 1 - Initial EDA and data cleaning
│   ├── FinalEDA_InitialModeling.ipynb  <- Notebook 2 - Additional EDA, data preprocessing, and cleaning
│   └── Final_Modeling.ipynb            <- Notebook 3 - Final EDA, data modeling, evaluation, and conclusion
│
├── Data
│   ├── 2021-2022 Football Player Stats.csv
│   ├── 2022-2023 Football Player Stats.csv
│   ├── player_valuations.csv
│   ├── players.csv
│   └── Created DataFrames
│
├── Presentations
│   ├── Presentation_1.pdf              <- Presentation 1 - Scope of project and basic EDA
│   ├── Presentation_2.pdf              <- Presentation 2 - Data preprocessing and baseline modeling
│   └── Final_Presentation.pdf          <- Final Presentation - Project overview and results
│
├── App_Demo
│   ├── app.py                          <- Streamlit app
│   ├── final_model.pkl                 <- pkl file for Streamlit app
│   ├── scaler.pkl                      <- pkl file for Streamlit app
│   ├── shap_explainer.pkl              <- pkl file for Streamlit app
│   └── (other necessary files)
│
├── environment_export.yml              <- Required environment file to run packages
└── README.md                           <- Readme file for project


### Datasets (4 original Datasets from Kaggle)
--------------------------------------------------------
-- 2021-2022 Football Player Stats.csv (2921 rows x 143 columns)<br>
-- https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats/data<br>
-- 2022-2023 Football Player Stats.csv (2689 rows x 124 columns)<br>
-- https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats/code<br>
-- player_valuations.csv (440643 rows x 9 columns)<br>
-- https://www.kaggle.com/datasets/davidcariboo/player-scores?select=player_valuations.csv<br>
-- players.csv (30302 rows x 23 columns)<br>
-- https://www.kaggle.com/datasets/davidcariboo/player-scores?select=players.csv<br>


### Table of Contents
--------------------------------------------------------
-- Dataset introduction<br>
-- Data dictionary<br>
-- Preprocessing & Data Cleaning<br>
-- EDA<br>
-- Modeling<br>
-- Conclusions<br>

### Dataset Introduction
---------------------------
In this project, we will be using 4 datasets, all of which are obtained from Kaggle.<br>

-- 2021-2022 Player Statistics. This is a dataset which contains each players in season statistics over the course of 2021-2022 season. This is for players in the top 5 leagues.<br>

-- 2022-2023 Player Statistics. This is same as above dataset, except for 2022-2023 season. The source for these two datasets are the same.<br>

-- Player Valuation. This dataset contains player valuation for each player over the last 20 years. Only player ID is shown here, not player name. This dataset is from a different source than above datasets.

-- Player name. This comes from the same source as player valuation. This dataset has player id, with respective player name and certain attributes, such as height of player.


### Data Dictionary
---------------------------
This is our data dictionary from our initial datasets.<br>

- **Rk**: Rank<br>
- **Player**: Player's name<br>
- **Nation**: Player's nation<br>
- **Pos**: Position<br>
- **Squad**: Squad’s name<br>
- **Comp**: League that squad occupies<br>
- **Age**: Player's age<br>
- **Born**: Year of birth<br>
- **MP**: Matches played<br>
- **Starts**: Matches started<br>
- **Min**: Minutes played<br>
- **90s**: Minutes played divided by 90<br>
- **Goals**: Goals scored or allowed<br>
- **Shots**: Shots total (Does not include penalty kicks)<br>
- **SoT**: Shots on target (Does not include penalty kicks)<br>
- **SoT%**: Shots on target percentage (Does not include penalty kicks)<br>
- **G/Sh**: Goals per shot<br>
- **G/SoT**: Goals per shot on target (Does not include penalty kicks)<br>
- **ShoDist**: Average distance, in yards, from goal of all shots taken (Does not include penalty kicks)<br>
- **ShoFK**: Shots from free kicks<br>
- **ShoPK**: Penalty kicks made<br>
- **PKatt**: Penalty kicks attempted<br>
- **PasTotCmp**: Passes completed<br>
- **PasTotAtt**: Passes attempted<br>
- **PasTotCmp%**: Pass completion percentage<br>
- **PasTotDist**: Total distance, in yards, that completed passes have traveled in any direction<br>
- **PasTotPrgDist**: Total distance, in yards, that completed passes have traveled towards the opponent's goal<br>
- **PasShoCmp**: Passes completed (Passes between 5 and 15 yards)<br>
- **PasShoAtt**: Passes attempted (Passes between 5 and 15 yards)<br>
- **PasShoCmp%**: Pass completion percentage (Passes between 5 and 15 yards)<br>
- **PasMedCmp**: Passes completed (Passes between 15 and 30 yards)<br>
- **PasMedAtt**: Passes attempted (Passes between 15 and 30 yards)<br>
- **PasMedCmp%**: Pass completion percentage (Passes between 15 and 30 yards)<br>
- **PasLonCmp**: Passes completed (Passes longer than 30 yards)<br>
- **PasLonAtt**: Passes attempted (Passes longer than 30 yards)<br>
- **PasLonCmp%**: Pass completion percentage (Passes longer than 30 yards)<br>
- **Assists**: Assists<br>
- **PasAss**: Passes that directly lead to a shot (assisted shots)<br>
- **Pas3rd**: Completed passes that enter the 1/3 of the pitch closest to the goal<br>
- **PPA**: Completed passes into the 18-yard box<br>
- **CrsPA**: Completed crosses into the 18-yard box<br>
- **PasProg**: Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area<br>
- **PasAtt**: Passes attempted<br>
- **PasLive**: Live-ball passes<br>
- **PasDead**: Dead-ball passes<br>
- **PasFK**: Passes attempted from free kicks<br>
- **TB**: Completed pass sent between back defenders into open space<br>
- **Sw**: Passes that travel more than 40 yards of the width of the pitch<br>
- **PasCrs**: Crosses<br>
- **TI**: Throw-Ins taken<br>
- **CK**: Corner kicks<br>
- **CkIn**: Inswinging corner kicks<br>
- **CkOut**: Outswinging corner kicks<br>
- **CkStr**: Straight corner kicks<br>
- **PasCmp**: Passes completed<br>
- **PasOff**: Offsides<br>
- **PasBlocks**: Blocked by the opponent who was standing it the path<br>
- **SCA**: Shot-creating actions<br>
- **ScaPassLive**: Completed live-ball passes that lead to a shot attempt<br>
- **ScaPassDead**: Completed dead-ball passes that lead to a shot attempt<br>
- **ScaDrib**: Successful dribbles that lead to a shot attempt<br>
- **ScaSh**: Shots that lead to another shot attempt<br>
- **ScaFld**: Fouls drawn that lead to a shot attempt<br>
- **ScaDef**: Defensive actions that lead to a shot attempt<br>
- **GCA**: Goal-creating actions<br>
- **GcaPassLive**: Completed live-ball passes that lead to a goal<br>
- **GcaPassDead**: Completed dead-ball passes that lead to a goal<br>
- **GcaDrib**: Successful dribbles that lead to a goal<br>
- **GcaSh**: Shots that lead to another goal-scoring shot<br>
- **GcaFld**: Fouls drawn that lead to a goal<br>
- **GcaDef**: Defensive actions that lead to a goal<br>
- **Tkl**: Number of players tackled<br>
- **TklWon**: Tackles in which the tackler's team won possession of the ball<br>
- **TklDef3rd**: Tackles in defensive 1/3<br>
- **TklMid3rd**: Tackles in middle 1/3<br>
- **TklAtt3rd**: Tackles in attacking 1/3<br>
- **TklDri**: Number of dribblers tackled<br>
- **TklDriAtt**: Number of times dribbled past plus number of tackles<br>
- **TklDri%**: Percentage of dribblers tackled<br>
- **TklDriPast**: Number of times dribbled past by an opposing player<br>
- **Blocks**: Number of times blocking the ball by standing in its path<br>
- **BlkSh**: Number of times blocking a shot by standing in its path<br>
- **BlkPass**: Number of times blocking a pass by standing in its path<br>
- **Int**: Interceptions<br>
- **Tkl+Int**: Number of players tackled plus number of interceptions<br>
- **Clr**: Clearances<br>
- **Err**: Mistakes leading to an opponent's shot<br>
- **Touches**: Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch<br>
- **TouDefPen**: Touches in defensive penalty area<br>
- **TouDef3rd**: Touches in defensive 1/3<br>
- **TouMid3rd**: Touches in middle 1/3<br>
- **TouAtt3rd**: Touches in attacking 1/3<br>
- **TouAttPen**: Touches in attacking penalty area<br>
- **TouLive**: Live-ball touches. Does not include corner kicks, free kicks, throw-ins, kick-offs, goal kicks or penalty kicks.<br>
- **ToAtt**: Number of attempts to take on defenders while dribbling<br>
- **ToSuc**: Number of defenders taken on successfully, by dribbling past them<br>
- **ToSuc%**: Percentage of take-ons Completed Successfully<br>
- **ToTkl**: Number of times tackled by a defender during a take-on attempt<br>
- **ToTkl%**: Percentage of time tackled by a defender during a take-on attempt<br>
- **Carries**: Number of times the player controlled the ball with their feet<br>
- **CarTotDist**: Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction<br>
- **CarPrgDist**: Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal<br>
- **CarProg**: Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area<br>
- **Car3rd**: Carries that enter the 1/3 of the pitch closest to the goal<br>
- **CPA**: Carries into the 18-yard box<br>
- **CarMis**: Number of times a player failed when attempting to gain control of a ball<br>
- **CarDis**: Number of times a player loses control of the ball after being tackled by an opposing player<br>
- **Rec**: Number of times a player successfully received a pass<br>
- **RecProg**: Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area<br>
- **CrdY**: Yellow cards<br>
- **CrdR**: Red cards<br>
- **2CrdY**: Second yellow card<br>
- **Fls**: Fouls committed<br>
- **Fld**: Fouls drawn<br>
- **Off**: Offsides<br>
- **Crs**: Crosses<br>
- **TklW**: Tackles in which the tackler's team won possession of the ball<br>
- **PKwon**: Penalty kicks won<br>
- **PKcon**: Penalty kicks conceded<br>
- **OG**: Own goals<br>
- **Recov**: Number of loose balls recovered<br>
- **AerWon**: Aerials won<br>
- **AerLost**: Aerials lost<br>
- **AerWon%**: Percentage of aerials won<br>


### Preprocessing & Data Cleaning
--------------------------------------------------------
The goal of the preprocessing and cleaning phase of this project is to merge the dataframes and produce a final dataframe with the respective players, their statistics and their valuation. This process has been the most time consuming element of the project. This is largely due to merging multiple different dataframes, each with it's own method of storing names. As we needed to merge on the players names, this required a lot of cleaning and meticulous checks.

There were multiple merges we needed for our dataset:<br>
-- player name and player valuation (on player id)<br>
-- player statistics 2021-2022 and player name/valuation (on player name)<br> 
-- player statistics 2022-2023 and player name/valuation (on player name)<br>
-- player statistics (merged vertically)<br>

After all dataset merging, preprocessing and cleaning, we had a final dataframe consisting 5422 rows and 128 columns. This dataframe will be used for our models.


### Exploratory Data Analysis (EDA)
--------------------------------------------------------
As our player statistics and player valuation datasets are all seperated, our initial exploratory data analysis (EDA) largely consists on looking at the relationships between our features. After drawing up a correlation matrix between our feature variables, we can see some interesting patterns between our features:
- There are many highly correlated blocks in our correlation matrix. This indicates the nature of the dataset having many overlapping features. For example, passes completed, passes attempted, pass completion percentage, (passes) total distance are all similar features and will likely have a high correlation with each other.<br>
- There are also many blocks of negative correlations. This may allude to the specialist nature of certain positions in football. For example, the most negative pair of statistics are 'Touches in Final third' and 'Touches in first third' - this means a player that has many touches in the final third, will likely have very little in their own third.<br>

The target variable - Player Valuation - is heavily skewed to the right. We have performed a log transformation on this to aide our model. Upon taking the transformation, the distribution has become almost normal, a trait that usually helps model accuracy. We will need to convert this back during model evaluation for interpretable results.

We have also decided to group several categorical factors into buckets - including nationality of players, and the standing of the teams they play for. I grouped these into multiple buckets that has different distributions for valuations. Through ANOVA and TUKEY testing, these distributions have been confirmed to have statistically different distributions. Once again, this should also aide our model.


### Modeling
--------------------------------------------------------
Our first baseline model has been completed. Using a linear regression, we have achieved a 5 fold cross validation R squared score of 0.375 and a 5 fold cross validation mean absolute error score of 7,661,307. Whilst this is quite a poor model in terms of accuracy, it has lead to some insight on which variables have high or low correlation. 

**High positive correlation coefficients include:**<br>
GcaDef: defensive actions that lead to a goal<br>
Comp_Premier League: player in premier league<br>
90's: Minutes played divided by 90<br>
Pos_FW: Position of player is forward, have very high correlation coefficients.<br>

**High negative correlation coefficients include:**<br>
GCA: Goal creating action<br>
Comp_Ligue 1: Player in Ligue 1<br>
TKL: Number of players tackled<br>
BLKPass: Number of times blocking a pass by standing in its path<br>

After our baseline model, we implemented many different models. This included lasso regression, ridge regression, decision tree, random forest, neural network, bagging and gradient boosting algorithms. After performing gridsearch to optimize these models, gradient boosting provided best results. This was measured using our evaluation framework.

Our evaluation framework consisted of measuring the R Squared, Adjusted R Squared, Mean Absolute Error (MAE) and Percentage Mean Absolute Error (PMAE) for each model. Upon comparing these metrics for each model, gradient boosting had the best scores. Additionally, we plotted the distribution of actual valuation versus the predicted valuation by the models and gradient boosting had the lowest spread - a positive characteristic.

Lastly, we performed Recursive Feature Engineering (RFE) on our gradient boosting model. This created a model that reduced our feature set to 20 features whilst only reducing accuracy metrics by a small degree. This model can be used to simulate a simple demonstration if required.


### Conclusion
--------------------------------------------------------

As found earlier, our best performing model was gradient boosting. This model was the best predictor of player valuation, given the player previous season statistics. This was the best performer in all of our evaluation metrics, which included the R squared, adjusted R squared, mean absolute error and percentage mean absolute error. Upon further analysis, we plotted the feature importance of this model and found several key features: the players age, whether he plays for a top team, the amount of minutes played and whether the player plays in the premier league. Further analysis using shap gives a clearer image of how each feature affects the player valuation.<br>

Overall, this project offers a solution to measure football player valuation. Whilst accuracy measurements can be further improved, this project is a first step towards understanding player valuation. Additionally, we have found several key features that help in determining player valuation. 

Next steps in this project will be to improve model accuracy by additional hyperparameter tuning. Neural networks can be further investigated as it showed heavy overfitting in my testing. Potentially supplementing additional data such as marketing potential, player wages, contract length, may also improve the model. We can also try find player transfers that occurred in the last two years and compare our model against that. Lastly, we can try to develop an application that can input these features and produce an accurate valuation. This will be extremely useful for scouts and football clubs alike. However, we do need to further investigate the ethical implications of such a tool as we are putting a monetary value on people. In the wrong hands, this could further causes such as player trafficking, which is a rampant issue in lesser developed countries.






