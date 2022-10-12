# DnDLifespan

## About

In my own life, one of my favorite hobbies is playing the Tabletop Role-playing Game Dungeons and Dragons (D&D). In the game, players create a player character (PC) that they use to tell a collaborative story with others.

Over the years, I've collected data for thirty-one of the characters that I've created for D&D games, also known as campaigns. I've noticed that the lifespan of these characters, defined by the number of days between the first and last time I play them, tend to vary greatly. Some character last for years of enthusiastic play. Other characters, however, sputter out after a mere couple weeks due to disinterest in the campaign. In most of my cases, the lifespan of the campaign and the character are the same. However, there is the rare case where a PC dies, and I make a new one during the course of the same campaign.

Using Bayesian techniques including censoring, prior selection, and model selection, I created nine regression models from my own data to analyze which factors, both involving the campaign itself and the characters I make, to determine which factors most affect the lifespan of a character. For example, are characters where I play with strangers more likely to have short lifespans due to less accountability in continuing the campaign? Are there certain character traits that I'm subconsciously less enthusiastic about, which would inadvertently shorten the campaign and character's lifespan?

While none of the nine tested models were perfect, Model 8, which took the significant variables from the full normal model, was the best compromise between good prediction and overfitting. Overall, the best model thus far showed a mixture of internal and external factors influencing a PC's lifespan in my own D&D games. Notably, these factors include character stats, the ending of the game, character gender, the number of players, and the format that the game is played through. The heavily imputed variables did not have an impact on the final model.


### Running the project

* All .odc files can be run individually in Winbugs independent of the accompanying .csv files. 
* 4d6.py is a file where I simulate stat generation techniques for imputing data.
* PC Winbugs Data.csv is the original data file, while PC_Winbugs_Final.csv is the data cleaned and prepared for analysis.
* Project-Penn.pdf is a pdf write-up of the project methodology and results
