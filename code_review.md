# Code Review: Project 2

### Name: Ridwan Alam

[X] README.md included
[X] Slides included
[X] Code included

## Clean Code:
- I like the separate get_df.py and stat_functions.py modules with scraping and dataframe-creation functions -- definitely helps make notebook clean
- I wonder if the wide reciever and running back analysis could have been combined since they're near identical notebooks? A single analysis notebook with a larger dataset? Maybe not just a thought. 
- I like the use of numbered section headings -- I notice inconsistent use of titles after the number though, I think its best to include them on every one to be more descriptive & know what the section is about!

## Good Documentation:
- I don't think you need to include the "being a data scientist: the real sh*t" blurb in your readme haha
- Make sure to include a "results" section in your readme, with a high-level overview of what insight you found from doing this project and what conclusions you've drawn!
- Great use of docstrings on your .py scraping modules to explain what each does! 
- I'd love to see more markdown cells explaining thought process/analysis along the way, for example after you generate a pairplot, describe it a bit. You did a great job of using markdown cells for correct explanations of the data science methods being used though which was great! 
- Nice use of inline comments to caption each chunk of code, very clear & easy to follow your steps 

## Proper Data Science:
- I like the design choice of using running average of all previous games as "previous game" to predict next game, to avoid this becoming a time-series problem. 
- Good pair plot, easy to visually see linear relationships 
- Great job trying out both single validation and cross validation! 
- Correct explanation and implementation of standardization
- In a typical workflow, you wouldn't score on train-val-test all together -- You'd rather score on just train and val, and let the discrepency between scores and the val score inform which model you want to pick & how you should change it. You can then optimize it, and when you have your finalized best model, *then* you'd finally score on the holdout test data to see how it did. Scoring on test set any sooner is "seeing" the data that's supposed to remain unseen; it shouldn't help to inform any choices. 
- A negative R^2 indicates a problem beyond just overfitting ... I'd examine that again 
- Nice Lasso/Ridge tuning
- I would use an x-axis range of like 5 to 15 on your linear model actual vs. predicted graph rather than 0 to 35 -- wil be more clear. Also, you wouldn't fit a line to a this sort of graph. :)

## Comments:
- Great job on project 2!
- Your tested vs. predicted fantasy points are pretty close -- which means its a good model! So highlight that :)
- I'd just love to see more analysis markdown cells throughout explaining not just the data science concepts, but the analysis of your data & results -- what your project is actually about! 
