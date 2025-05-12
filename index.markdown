---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: 'Brake the System: Outsmarting urban traffic in NY & LA'
---

# Under the Hood: The Dataset
In this one-pager, we explore the temporal rhythms of traffic congestion across major U.S. cities—zeroing in on New York and Los Angeles. What if the when of traffic mattered just as much as the where?

To drive this analysis, we use the U.S. Traffic Congestions (2016–2022) dataset, compiled by Sobhan Moosavi. It contains detailed records of congestion incidents across major urban areas, based on real-time traffic reports. The dataset was last accessed on May 10, 2025. For consistency and completeness, our analysis focuses exclusively on congestion data from 2016 through 2022—the full available range.

# Top Congestion Hotspots in New York and Los Angeles

We want to look at some of the places where the traffic is overloaded most often, in order to maybe choose routes around these places. Other ways we can use this are to alarm the town council to do something about these hotspots.

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
  Figure 1: Heatmaps showing the 10 most congested locations in New York City and Los Angeles from 2016–2022.
</p>

Looking at the heatmaps above, it’s clear that some areas in both New York and Los Angeles deal with much heavier traffic congestion than others. In New York, places like the intersection of West Street and Battery Place, Washington Mews and 5th Avenue, and 6th Avenue near Central Park South stand out. These are all busy parts of the city where a lot of streets come together, so it’s not surprising they get backed up. Making improvements to the infrastructure in these areas could really help ease the flow.

In Los Angeles, the worst congestion spots are mostly found in the Boyle Heights area. The top three are the merge between the Santa Monica and Golden State Freeways, the split between the Golden State and San Bernardino Freeways, and the merge between the Santa Ana and San Bernardino Freeways. These are big freeway junctions that see a lot of traffic every day. If the city focused on improving how traffic moves through these spots, it could make a real difference for drivers across L.A.

## The 24 hour cyckle of NY and LA traffic
We are now looking at how the traffic congestions evolve through the 24 hour cyckle of the day. WE are likely to see that rushhours happens, as they do in most cities. But here we can also see where the rush hour starts and ends.

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
  Figure 2: Time-based heatmaps showing how traffic congestion developed across New York City and Los Angeles through the day, from 2016 to 2022.
</p>

We notice that the rush hour seem to start at around 8:40 in LA but it starts much earlier in New York with big clusters of congestions starting as early as 6:00. The rush hour does not look as much like a rush "hour" since it lasts through out most of the day. Here we first see a decline in cluster at around 21:30 in LA and for NY it lasts untill 23:10. It is an indication that there generally is too many cars in these big cities since there is not much of a break in trafiic through the day.

# The inpact of weather


# Conclusion: End of the Road

## refferences
