---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: 'Brake the System: Outsmarting urban traffic in NY and LA'
---

# Under the Hood: The Dataset
In this one-pager, we explore the temporal rhythms of traffic congestion across major U.S. cities—zeroing in on New York and Los Angeles. What if the when of traffic mattered just as much as the where?

To drive this analysis, we use the U.S. Traffic Congestions (2016–2022) dataset, compiled by Sobhan Moosavi. It contains detailed records of congestion incidents across major urban areas, based on real-time traffic reports. The dataset was last accessed on April 29. 2025. For consistency and completeness, our analysis focuses exclusively on congestion data from March 22. 2016 to September 8. 2022.

# Clocks and Congestion: How Time Shapes Traffic Trends

<div style="text-align: center;">
  <img src="yearly_boxplot.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  1: Yearly car congestions for LA and NYC.
  </p>
</div>

In Figure 1. above, we see that a clear tendency is that Los Angeles consistently has more congestion events than New York across all years. Both cities show an overall increase in congestion up until 2021, where we see a peak, especially for LA, which reaches over 200,000 congestion events. After 2021, there is a sharp drop for both cities in 2022, likely due to the fact that data after September 8. 2022, is missing. The months after September also have a high rise in traffic congestion, as we see in Figure 3, which explains the drop after 2021. Another observation is that NYC has a slightly more stable trend, while LA shows more variation year to year. This could be tied to differences in city infrastructure, driving culture, or more cars being registered.

<div style="text-align: center;">
  <img src="week_histogram.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  2: Weekly car congestion for LA and NYC.
  </p>
</div>
Moving on to how the weekly day to day traffic looks we notice in Figure 2. above that for both New York and Los Angeles, the number of car congestions is clearly highest on weekdays and lowest during the weekend. Friday stands out as the busiest day for both cities, with LA reaching over 170,000 congestion events. The numbers start to drop on Saturday and hit their lowest on Sunday, especially in NYC, with only around 35,000 events. This trend makes sense as people are commuting to work during the week, while weekends are typically more relaxed with fewer people on the road. LA again shows higher congestion overall, which follows the same pattern as we saw in Figure 1.


<div style="text-align: center;">
<img src="CalenderNY.png" width="100%" /><br />
<img src="CalenderLA.png" width="100%" /><br />
<p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure 3: Calendar plots for car congestions in NYC (top) and LA (bottom).
</p>
</div>

In Figure 3. of our calendar plots, we notice some tendencies. We see that the least busy days are the 1. of January and 4. of July. This likely comes from the fact that a lot of people are hungover after New Year and do not want to do anything, and people being too drunk to be able to drive on the 4. of July. For both calendar plots, we have very similar tendencies. There is more busy months being in February, March, October, November, and the start of December, with the Christmas vacation reducing the congestion occurrences. A takeaway from this is that it looks like people are more happy to leave the car at home when the weather is nice during the warmer seasons.

# The impact of weather

<div style="text-align: center;">
  <img src="effect_of_weather_attributes.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  4: Top 10 streets by distance of car congestion in NYC
  </p>
</div>

From what we saw in Figure 3, we now look at how specific weather attributes impact traffic delays in Figure 4. From the top left plot, we see that higher temperatures seem to reduce traffic delays in LA quite clearly, while NYC has a more stable trend but starts off with higher delays during colder temperatures. This supports the idea that bad weather slows things down more and people might be more likely to use other means of transportation when the weather is nice. For humidity, LA and NYC show a big spike in delay above 80%, this could come from more extreme weather like rain or heatwaves, which occur when humidity is high. With visibility, both cities see fewer delays when visibility is high, which makes sense as it's easier and safer to drive. Pressure doesn't show any strong trend, but we do see random spikes in delay for both cities, especially in NYC. Overall, it looks like LA traffic is more sensitive to weather changes, while NYC stays more consistent across different weather conditions.

# Top Congestion Hotspots in New York and Los Angeles

We want to look at some of the places where the traffic is overloaded most often, in order to maybe choose routes around these places. Other ways we can use this are to alarm the town council to do something about these hotspots.

<div style="text-align: center;">
  <img src="top10_car_congestions.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  5: Top 10 streets with most car congestions
  </p>
</div>

<div style="text-align: center;">
  <img src="top10_distance.png" width="150%" />
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure  6: Top 10 streets by distance of car congestions
  </p>
</div>

<div style="text-align: center; max-width: 100%; margin: auto;">
  <iframe src="severity_bokeh.html" width="138%" height="590" frameborder="0"></iframe>
  <p style="font-style: italic; font-size: 0.9em; color: gray;">
    Figure 7: Interactive plot showing the top 10 streets of each city for each severity levels.
  </p>
</div>


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

Looking at the heatmaps above, it’s clear that some areas in both New York and Los Angeles deal with much heavier traffic congestion than others. In New York, places like the intersection of West Street and Battery Place, Washington Mews and 5th Avenue, and 6th Avenue near Central Park South stand out. These are all busy parts of the city where a lot of streets come together, so it’s not surprising they get backed up. Making improvements to the infrastructure in these areas could really help ease the flow.

In Los Angeles, the worst congestion spots are mostly found in the Boyle Heights area. The top three are the merge between the Santa Monica and Golden State Freeways, the split between the Golden State and San Bernardino Freeways, and the merge between the Santa Ana and San Bernardino Freeways. These are big freeway junctions that see a lot of traffic every day. If the city focused on improving how traffic moves through these spots, it could make a real difference for drivers across L.A.

## The 24-hour cycle of NY and LA traffic
We are now looking at how the traffic congestions evolve through the 24-hour cycle of the day. We are likely to see that rush hours happen, as they do in most cities. But here we can also see where the rush hour starts and ends.

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
  Figure 9: Time-based heatmaps showing how traffic congestion developed across New York City and Los Angeles through the day, from 2016 to 2022.
</p>

We notice that the rush hour seems to start at around 8:40 in LA, but it starts much earlier in New York, with big clusters of congestion starting as early as 6:00. The rush hour does not look as much like a rush "hour" since it lasts throughout most of the day. Here we first see a decline in cluster at around 21:30 in LA, and for NY it lasts until 23:10. It is an indication that there are generally too many cars in these big cities since there is not much of a break in traffic through the day.


# Conclusion: End of the Road

## Refferences and Sources
The dataset used: [US Traffic Congestions 2016-2022](https://www.kaggle.com/datasets/sobhanmoosavi/us-traffic-congestions-2016-2022). Accessed 29th of april 2025
 
