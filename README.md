# ftc-food-delivery-app-dashboard
This repository contains files to build a dashboard for data analysis of a ficticious food delivery company.

# 1. Business Issue
Pyfood is a tech company which has developed an application that conects restaurants worldwide with delivery drivers and customers.

Through this application is possible to order foods in all registered restaurants and receive it at your home by a drivers which is also registered in the app.

The company make business between restaurants, drivers and customers and generates a lot of data of the deliveries, type of order, weather conditions, traffic conditions and so on. Despite business is going well, in terms of deliveries, the CEO does not has a clear sight of company's growth KPI.

You have been hired as a Data Scientist to create solutions, but before train algorithm, the company's need is having the main strategy KPIs organized in a single tool, so the CEO would may analyze and make decisions.

The type of business is called Marketplace. To understood how the business is going, the CEO would like to see the following growth metrics:

## Company's vision
  1. Total of orders per day.
  1. Total of orders per week.
  1. Distribution of orders per type of traffic conditions.
  1. Comparison between the quantity of orders per city and traffic conditions.
  1. Total of orders per driver per week.
  1. Central location of each city per traffic condition.

## Delivery man's vision
  1. Minimun and maximum age of delivery mans.
  1. Best and worst vehicle conditions.
  1. Average rate per delivery man.
  1. Average rate and standard deviation per traffic conditions.
  1. Average rate and standard deviation per weather conditions.
  1. Top 10 fastest delivery mans per city
  1. Top 10 slowest delivery mans per city

## Restaurant vision
  1. Quantity of unique restaurants.
  1. Average distance between restaurants and delivery point.
  1. Average time and standard deviation of order per city.
  1. Average time and standard deviation of order per city and type of order.
  1. Average time and standard deviation of order per city and traffic conditions
  1. Average time of delivery during festivals.

# Project goal
Create a set of charts that show these metrics in the most clear way for the CEO.

# Strategy for solution
The strategic dashboard was developed using metrics that reflect the 3 main visions of the company's business model:

  - Vision of company growth
  - Vision of restaurant growth
  - Delivery personnel growth vision

Each vision is represented by the following set of metrics.

  - Company growth vision

  1. Orders per day
  1. Percentage of orders by traffic conditions
  1.Number of orders by type and city.
  1. Orders per week
  1. Number of orders by type of delivery
  1. Number of orders by traffic conditions and type of city
 
  - Vision of restaurant growth

  1. Number of unique orders.
  1. Average distance traveled.
  1. Average delivery time during festivals and normal days.
  1. Standard deviation of delivery time during festivals and normal days.
  1. Average delivery time per city.
  1. Distribution of average delivery time by city.
  1. Average delivery time by type of order.
  
  - Overview of delivery man growth

  1. Age of the oldest and youngest delivery driver.
  1. Rating of the best and worst vehicle.
  1. Average rating per delivery person.
  1. Average rating for traffic conditions.
  1. Average rating for weather conditions.
  1. Average time taken by the fastest delivery driver.
  1. Average time taken by the fastest delivery driver per city.

# Final result of the project
Online panel, hosted in a Cloud and available for access from any device connected to the Internet.

The panel can be accessed via this link: 

# Conclusion
My first personal project focused on the transition to a career as a data scientist. My main goal with this project was to develop my programming language skills, which in this case I used Python. In addition, to improve my data analysis skills, I was able to learn how to manipulate the Pandas library and facilitate the visualization and creation of real-time insights through the Streamlit framework.
