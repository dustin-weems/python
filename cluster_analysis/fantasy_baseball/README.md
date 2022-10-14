# **Fantasy Baseball**

*“Just keep going. Everybody gets better if they keep at it.”* **- Ted Williams**

## Overview
In one of my fantasy baseball leagues, teams compete on a weekly basis across ten statistical categories.  Half of these categories are specific to batters, the others are specific to pitchers.  This analysis will focus on the batting categories only.  They are:
* Runs (R)
* Home Runs (HR)
* Runs Batted In (RBI)
* Stolen Bases (SB)
* Batting Average (AVG)

The goal is to win as many of these categories as possible each week.  I will forego the definitions of each category and instead emphasize that "winning" a category means achieving a larger value than your opponent in that given category.  

Before each season begins, the league members will come together for a draft where we select our players for the upcoming year.  For the past two seasons, I have been using a cluster analysis to build tiers to inform my draft rankings for batters.  Generally, a top tier player either contributes strongly to all five categories or shows dominance in most of the categories.  It is important to balance my team's prospective performance across all five categories to stay competitive throughout the season.    

The action of segmenting players into tiers based on expected performance is similar to a business performing customer segmentation at the top of a sales funnel.       

## Core Files
* [2021 Batting Projections](./2021_batting_projections.csv)
* [K-Means Cluster Analysis](./cluster_analysis_on_batter_projections.ipynb)
* [Projections with Clustering Results](./kmeans_output.csv)

## Resources
* [Fangraphs](https://www.fangraphs.com/) - source of the projection data and a great site for fantasy baseball content