---
layout: post
title: Project - Squirrel Park
tags: [Projects & coding skills]
excerpt_separator: <!--more-->
---

__This is a data visualization group project from Data Visualization II in UBC's Master of Data Science program.__ <br/>
We built a Heroku App with python `dash`. The App allows users to learn about the distribution of squirrels in the Central Park of New York, and explore the plots interactively.     
<!--more-->
## Authors 
* Cari Gostic, Roc Zhang, Lori Fang

## The link to the App
* The App can be found [here](https://dsci-532-group203-milestone2.herokuapp.com/) (browse with computers).  

## Project's GitHub repo 
* Project's GitHub repo can be found [here](https://github.com/UBC-MDS/DSCI-532_group-203_Lab1-2).  

## App description:
* Our app contains four plots to help our users learn about the distribution of squirrels in the Central Park. It will enable users to  efficiently plan their visit to the park, either to have more interaction with the squirrels or avoid them (for example, if they were planning a picnic). Additionally, users can find information about where to go to observe a certain behavior of the squirrels.  

* The first plot on the top-left is a map of the park, with a color gradient filling in each region. The deeper the color, the more squirrels are observed in that region. With this map, the users can directly plan to which part of the park they should go to find more or fewer squirrels. We think this will be really helpful because the users are shown both the region names as well as the location on an actual map. They won't need to look up those region names if they are unfamiliar with the park.  

* The bar chart on the bottom-left gives information on the exact amount of squirrels observed in each region of the park during the 2018 Squirrel Census. This bar chart displays explicitly the difference in the number of squirrels across park regions. The bars are ordered so that our users can quickly identify the most- and the least-squirrel-populated regions. The bar chart on the top-right shows the difference in the number of squirrels between morning (AM) and afternoon (PM). The value is calculated by `PM` - `AM`, which means positive-value bars (red ones) indicates more squirrels in the afternoon (PM).  

* The last plot on the bottom-right gives information about the squirrel behavior throughout the park. Users can choose a behavior of interest in the drop-down menu, and the plot will update accordingly to show the number of observed instances of that behavior in each park area.   

* Users can select certain regions by clicking on any of the bar charts, or directly on the map, and all plots will interactively highlight the selected regions (as is shown in the second sketch). 


## App Sketch:

![image](https://i.ibb.co/sKKNZzw/Screen-Shot-2019-11-22-at-11-15-11-AM.png)  

> An example of how the plots will interact with the user's selection of regions:

![image](https://i.ibb.co/7Vk3qJ0/Screen-Shot-2019-11-22-at-3-11-33-PM.png)  

## App Usage 
> * View squirrel distribution by park region, time of the day, and behavior.    
> * Direct the mouse to a region or bar on the graphs for detailed information.   
> * Click on the map or any chart to highlight specific regions. Hold "Shift" and click to highlight and compare multiple regions at once!  
> * Use the drop-down menu below the graphs to change the behavior displayed.   
