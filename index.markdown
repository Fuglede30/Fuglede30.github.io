---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: 'Brake the System: Outsmarting urban traffic in NY and LA'
---

# Under the Hood: The Dataset
Every day, millions of Americans lose precious time sitting in traffic. Whether it’s the frustration of a delayed commute, the cost of wasted fuel, or the toll on productivity, traffic congestion is more than just a a local issure — it’s a national issue that touches nearly everyone.

This website explores the complex dataset of traffic congestion in the United States through a powerful, real-world dataset comprising 33 million traffic events across 49 U.S. states, recorded between **March 2016 and September 2022**. The data — sourced from a network of APIs pulling live traffic updates — is rich and comprehensive, drawing on:

- Federal and state transportation departments  
- Law enforcement reports  
- Roadway sensors and traffic cameras  
- Real-time GPS and telemetry feeds

Each entry in this **12 GB dataset** is packed with details, from **severity levels** and **expected delays**, to **weather conditions**, **timestamps**, and **geographic coordinates**. Together, these records paint a detailed picture of when, where, and how congestion happens.

While the dataset spans the entire country, we focus on **New York City** and **Los Angeles** — two iconic urban giants that consistently rank as the most **traffic-congested** and **densely populated** cities in the U.S. [2]. Their scale, diversity, and traffic challenges make them ideal case studies for uncovering patterns, trends, and insights that could apply to cities nationwide. 
For a reasonable comparison between NYC and LA, we must first know how many observations the dataset has in each city. For NYC, we have $604.606$ observations and for LA we have 905.284 observations. Additionally, NYC is 778.2 km^2 [5] whereas LA is 1.302 km^2 [6]. This suggests that we should also consider the number of streets in each city where car congestions have occurred. For NYC, the number of streets reported where car congestions have occured is ``606``, whereas in LA, the reported number of streets is ``1721`` - more than double. This indicates, that although NYC has 30% less observations than LA, the congestions that do occur in NYC are likely to happen on fewer, more heavily trafficked streets whereas for LA, it has more streets and highways to distribute over. 

Our main goal is to help users spot where and when traffic tends to be the worst in each city, and to see how things like weather, time of day, or even the day of the week play a role. With this, we hope to discover patterns that could help improve traffic management, or simply just help commuters make better travel choices.

# Clocks and Congestion: How Time Shapes Traffic Trends
We begin by creating histograms and calender plots to explore the distribution of congestion events over time — specifically across different hours of the day, days of the week, and months of the year. We generate these plots separately for New York City and Los Angeles to allow for a direct comparison between the two.
<div style="text-align: center;">
  <img src="yearly_boxplot.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  1: Number of car congestions for LA and NYC throughout the years 2016-2022.
  </p>
</div>

In Figure 1. we see that 2016 and 2022 are the years with the least observations for both cities, which aligns with 3 months missing in each. On the other hand, we see that the number of car congestions in 2017-2019 are fairly stable in both cities. However, LA peaks a bit more than previous years in 2020, and in 2021 we see both cities having a significant increase in number of car congestions. Further, online research shows that New York City, indeed had a *Great Gotham Vroom Boom in 2020*, leading to 19% more bought cars from June to July compared to 2019 due to the first wave of Covid. Due to this, there was an increase in car sales, as people tried to avoid taking public transportation [3][4]. New York City being very public-transport dependent and very urban dense, it would be plausible that the number of car congestions increased during this time. The same spike can be seen for Los Angeles, that is heavily car-centric, that people were likely reluctant to take public transport. Further, LA hosts much of TV production that was otherwise shut down during Covid, and boom in delivery services along with infrastructure projects [4]. 

### Weekly trends
<div style="text-align: center;">
  <img src="week_histogram.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  2: Weekly average car congestion for LA and NYC.
  </p>
</div>
Considering Figure 2, the plots reveals that both cities show similar patterns in terms of when congestion occurs. Weekdays were consistently more congested than weekends. Friday stands out as the busiest day for both cities, with LA reaching over 170,000 congestion events. The numbers start to drop on Saturday and hit their lowest on Sunday, especially in NYC, with only around 35,000 events. This trend makes sense as people are commuting to work during the week, while weekends are typically more relaxed with fewer people on the road. 

### Yearly trends
<div style="text-align: center;">
<img src="CalenderNY.png" width="100%" /><br />
<img src="CalenderLA.png" width="100%" /><br />
<p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure 3: Calendar plots for car congestions in NYC (top) and LA (bottom).
</p>
</div>
Looking at the calender plot in Figure 3, we see that winter months experienced more traffic events compared to summer months. Further, we see that the least busy days are the 1. of January and 4. of July. This pattern may be explained by reduced activity due to post–New Year’s hangovers and, on the 4th, by many individuals being unable to drive due to alcohol consumption. For both calendar plots, we have very similar tendencies. The most busy months are February, March, October, November, and the start of December, with the Christmas vacation reducing the congestion occurrences. A takeaway from this is that it looks like people are more happy to leave the car at home when the weather is warmer.

### The 24-hour cycle of NY and LA traffic
We are now looking at how the traffic congestions evolve through the 24-hour cycle of the day.
<div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; max-width: 100%; margin: auto;">
  <div style="flex: 1 1 45%; min-width: 300px;">
    <iframe src="la_time_map.html" width="100%" height="500px" style="border:none;"></iframe>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray;">
      Los Angeles: 2016–2022
    </p>
  </div>
  <div style="flex: 1 1 45%; min-width: 300px;">
    <iframe src="ny_time_map.html" width="100%" height="500px" style="border:none;"></iframe>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray;">
      New York City: 2016–2022
    </p>
  </div>
</div>

<p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray; margin-top: 10px;">
  Figure 4: Time-based heatmaps showing how traffic congestion develops across New York City and Los Angeles. The heat map dots denotes all car congestions in the specific area within 5 minute interval throughout 24 hours of the day. 
</p>

In FIgure 4. we notice that in New York City, congestion events were mainly concentrated during the daytime hours from 7 AM to 5 PM. In contrast, Los Angeles showed a different pattern. The busiest hours occurred between 4 PM and 8 PM. However, it's worth noting that between 8 AM and 4 PM, the number of congestion events in Los Angeles is approximately the same as in New York. The key difference — and what contributes to LA having more overall congestion — may come from the additional traffic between 4 PM and 8 PM, where LA experiences significantly more congestion than NY. These differences highlight how the timing and intensity of traffic congestion vary between the two cities, possibly due to differences in work schedules (Los Angeles is known for having a later peak commute, partly due to its flexible work hours and industries like entertainment and tech [7]), commuting behavior, or urban infrastructure.

# Weather impact on delay from typical traffic
We are now interested in analyzing and testing our assumption on whether the weather attributes played a role on the typical traffic delay. We will use the 4 numeric variables ``Temperature(F)``, ``Humidity(%)``, ``Visibility(mi)``, ``Pressure(in)``. We plot these on the x-axis with ``DelayFromTypicalTraffic(mins)`` on the y-axis. However, due to having ``2139`` unique values for typical traffic delay, and only between ``25-215`` unique values for the weather attributes and approximately 1.5 million observations, we decide to bin the weather attributes in dynamic equal sized bins, such that each attribute has less bins than amount of unique values. To further migitate possible fluctuations for few observations, we use LOWESS smoothing in an attempt to capture a global trend for each weather attribute in relation to delay in typical traffic. 
<div style="text-align: center;">
  <img src="effect_of_weather_attributes.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  5: Delay from typical traffic as a function of weather attributes. The mean values across each respective weather attribute bin along with a LOWESS smoothing fit.
  </p>
</div>

Looking at **`Temperature(F)`**, NYC generally experiences colder weather than LA. In both cities, traffic delays peak at the lowest temperatures, likely due to people avoiding walking or public transport in the cold, or due to weather-related hazards like snow and ice.

While LA shows a steady decline in delay as temperatures rise, NYC follows a nonlinear trend: delays drop, then spike around 40°F, before falling again after 70°F. This mid-range increase may reflect challenges like rain or wind that worsen driving conditions. Both cities see a noticeable drop in delay near 80°F, possibly due to seasonal changes like summer vacations or increased use of alternative transportation.

For **`Humidity(%)`**, delays stay fairly stable around 1.5 minutes, but begin to increase past 80%, likely due to rain or general discomfort leading to more car use.

Finally, lower **`Visibility(mi)`** correlates with longer delays in both cities, as drivers become more cautious. However, LA’s delays stabilize more clearly, suggesting it may be better equipped to handle low-visibility conditions.


# Top Traffic Bottlenecks: Where Congestion Hits Hardest
After conducting a general investigation into overall traffic trends in both NYC and LA, we decided to take a closer look at the **top 10 streets** in each city. Our aim was to analyze how these streets differ across various categories. By focusing on the most frequently affected or busiest streets, we want to look at some of the places where the traffic is overloaded most often, in order to maybe choose routes around these places. Other ways we can use this are to alarm the town council to do something about these hotspots.

<div style="text-align: center;">
  <img src="top10_car_congestions.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  6: Top 10 streets with most car congestions.
  </p>
</div>

The plot reveals that, among the top 3 most congested streets, NYC exhibits higher levels of congestion compared to LA. This is a notable observation that was not apparent when analyzing the full dataset all at once. By narrowing the focus to only the busiest streets, distinct patterns emerge that might otherwise be obscured by the presence of many less-trafficked streets.

One possible explanation for this difference is urban infrastructure: NYC tends to have narrower streets and a denser street grid, which can lead to greater bottlenecks on major roads. In contrast, LA’s urban design typically includes wider roads and more dispersed traffic flow, which may help mitigate congestion even on heavily used streets.

This insight highlights the value of granular, location-specific analysis and demonstrates that while LA may appear more congested overall, individual hotspots in NYC can experience more severe congestion.

In fact, this is a classic example of **Simpson’s paradox** — where a trend that appears in aggregated data disappears or reverses when the data is disaggregated. Although LA shows higher congestion on average, a closer look at the top streets reveals the opposite trend, emphasizing the importance of context and segmentation in data analysis. 

###  Distance vs delay of typical traffic in each city by severity level
Next up we look into the top 10 streets by distance vs delay of typical traffic in each city. This is done as a bokeh plots, where you can choose the severity level. 
<div style="overflow-x: auto; width: 100%; transform: scale(0.85); transform-origin: top left; height: 527px;">
  <iframe src="severity_bokeh.html" width="120%" height="620" style="border: none;" scrolling="no"></iframe>
</div>
<p style="font-style: italic; font-size: 0.9em; color: gray;">
  Figure 7: Interactive bokeh plot showing the top 10 streets of longest distance and delay by each severity level for each city.
</p>

Overall, congestion distances are longer in Los Angeles, which aligns with expectations given LA’s larger geographic size compared to NYC. However, for severity levels 0–2, NYC shows longer congestion distances, suggesting that lower-severity incidents in LA do not stretch as far. This implies that in NYC, even low - severity congestion can span significant distances, while in LA, distance correlates more directly with severity.

At severity level 3, LA once again leads in congestion distance, reinforcing how its vast layout influences severe traffic events.

Looking at delay relative to typical traffic, NYC has longer delays overall, but LA shows higher delays at severity levels 0 and 1 - despite shorter distances. This may indicate denser traffic hotspots in LA where even short-distance congestion causes significant delays.

Interestingly, at severity level 3, LA has longer distances but shorter delays, while NYC has shorter distances but longer delays. This contrast suggests that NYC’s severe congestion is more compact and intense, while LA’s is more spread out, causing less delay per mile. 


<div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; max-width: 100%; margin: auto;">
  <div style="flex: 1 1 45%; min-width: 300px;">
    <iframe src="ny_top_10_congestion.html" width="100%" height="500px" style="border:none;"></iframe>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray;">
      New York City (2016–2022)
    </p>
  </div>
  <div style="flex: 1 1 45%; min-width: 300px;">
    <iframe src="la_top_10_congestion.html" width="100%" height="500px" style="border:none;"></iframe>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray;">
      Los Angeles (2016–2022)
    </p>
  </div>
</div>

<p style="text-align: center; font-style: italic; font-size: 0.9em; color: gray; margin-top: 10px;">
  Figure 8: Heatmaps showing the 10 most congested locations in New York City and Los Angeles from 2016–2022.
</p>

Looking at the heatmaps in Figure 8, it’s clear that some areas in both New York and Los Angeles deal with much heavier traffic congestion than others. In New York, places like the intersection of West Street and Battery Place, Washington Mews and 5th Avenue, and 6th Avenue near Central Park South stand out. These are all busy parts of the city where a lot of streets come together, so it’s not surprising they get backed up. Making improvements to the infrastructure in these areas could really help ease the flow.

In Los Angeles, the worst congestion spots are mostly found in the Boyle Heights area. The top three are the merge between the Santa Monica and Golden State Freeways, the split between the Golden State and San Bernardino Freeways, and the merge between the Santa Ana and San Bernardino Freeways. These are big freeway junctions that see a lot of traffic every day. If the city focused on improving how traffic moves through these spots, it could make a real difference for drivers across L.A.

# Conclusion: End of the Road
Our deep dive into traffic congestion across New York City and Los Angeles reveals not just when and where congestion occurs, but how it behaves differently in two of America’s most iconic cities. From a high-level perspective, Los Angeles records more congestion events overall, likely due to its larger size and car-centric layout. Yet, New York City shows higher delay times, even over shorter distances, highlighting how its dense infrastructure can intensify congestion.

Time-based patterns show weekday peaks, with Fridays being the worst, and winter months consistently busier than summer. LA tends to have a later congestion peak (4–8 PM) compared to NYC’s more typical morning-to-afternoon cycle.

Weather plays a measurable role with colder, more humid, or low-visibility conditions correlating with increased delays. This supports the idea that inclement weather pushes more people into cars and slows traffic down.

Digging into street-level analysis reveals hotspot paradoxes: while LA may spread its congestion over more streets, NYC’s top streets suffer more intensely, demonstrating how localized analysis can reveal trends that aggregate data might obscure.

Ultimately, these insights are more than just interesting — they’re actionable. By identifying congestion patterns tied to time, weather, and geography, urban planners, policymakers, and commuters alike can make smarter, data-driven decisions. Whether it’s improving specific traffic chokepoints or adjusting commute schedules, data like this gives us the tools to "brake the system"—and outsmart urban traffic.

## Refferences and Sources
The dataset used: [US Traffic Congestions 2016-2022](https://www.kaggle.com/datasets/sobhanmoosavi/us-traffic-congestions-2016-2022). Accessed 29th of april 2025

[1] Moosavi, S., Samavatian, M. H., Nandi, A., Parthasarathy, S., & Ramnath, R. (2019). Short and long-term pattern discovery over large-scale geo-spatiotemporal data. Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2905–2913. https://doi.org/10.1145/3292500.3330755

[2] Insider Monkey. (n.d.). *30 most densely populated cities in the US*. Yahoo Finance. Retrieved May 13, 2025, from https://finance.yahoo.com/news/30-most-densely-populated-cities-140312195.html

[3] Car and Driver. (2021, August 30). What will New York do with the cars they purchased during the pandemic? Retrieved May 13, 2025, from https://www.caranddriver.com/features/a37293032/what-will-new-york-do-with-the-cars-they-purchased-during-the-pandemic/

[4] New York Times. (2020, August 12). Car buying in New York during the coronavirus pandemic. Retrieved May 13, 2025, from https://www.nytimes.com/2020/08/12/style/car-buying-new-york-coronavirus.html

[5] Wikipedia. (n.d.). New York City. Wikipedia, den frie encyklopædi. Retrieved May 13, 2025, from https://da.wikipedia.org/wiki/New_York_City

[6] Wikipedia. (n.d.). Los Angeles. Wikipedia, den frie encyklopædi. Hentet 13. maj 2025 fra https://da.wikipedia.org/wiki/Los_Angeles

[7] Drivemode. (2018, June 20). Drivemode data report: Where and when commuting takes the longest. Retrieved May 13, 2025, from https://www.drivemode.com/blog/engineering/drivemode-data-report-commuting-durations/
 
