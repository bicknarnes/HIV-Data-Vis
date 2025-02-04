# Import imports:
from imports import *
import get_gdf

# Get GeoDataFrame from get_gdf.py:
gdf = get_gdf.gdf
# Get stateFIPS_df from get_gdf.py:
stateFIPS_df = get_gdf.stateFIPS_df

'''
Bubble Mapping!

By STATE = Texas
'''

state = 'TX'

# Plot the counties for the contiguous US:
#gdf.plot(figsize = (15, 20))
gdf2 = gdf[gdf['State'] == state].copy()
gdf_points = gdf2.copy()

gdf_points['geometry'] = gdf_points['geometry'].centroid

fig, ax = plt.subplots(figsize=(16,16))
gdf2.plot(ax=ax, 
         color="lightgray", 
         edgecolor="grey", 
         linewidth=0.4)
gdf_points.plot(ax=ax, 
                #color="#07424A", 
                #c=gdf["avg_nh_score"], # I don't know what these colors mean but they're doing something
                markersize="hiv_rate",
                alpha=0.7, 
                categorical=False, 
                legend=True,
                column = "avg_nh_score"
                )
ax.axis("off")
plt.axis('equal')

plt.title("Rate of Persons Living with HIV (size) vs. Average Nursing Home Quality (color) by County\nState = Texas")

# Save & Show the figure:
plt.savefig("figs/texas_map1.png")
plt.show()
