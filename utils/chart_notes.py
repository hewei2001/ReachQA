chart_notes = {
    "line chart": """Notes on plotting line charts:
1. Use `plt.plot()` to connect data points with a line. Choose appropriate markers and line styles to differentiate multiple datasets within the same chart.
2. Set the x-axis and y-axis labels clearly, and make sure the tick marks are appropriately spaced to avoid clutter. This enhances readability and interpretation.
3. Adjust the line thickness (`linewidth`) and line style (`linestyle`) to improve visibility and distinguish different data series.
4. Consider employing a grid (`plt.grid(True)`) to facilitate the estimation of values at various points along the line, improving the chart's utility for data analysis, if necessary.
5. Add a legend (`plt.legend()`) to identify different lines, especially when multiple lines are plotted. Position the legend to avoid obscuring data.
6. Consider using color coding for lines to represent different categories or time periods. Ensure that the colors have enough contrast against the background.
7. Experiment with adding annotations or highlighting specific points on the line to draw attention to important values or trends.
""",
    "line chart with data annotation": """Notes on plotting line charts with data annotation:
1. Use `plt.plot()` to connect data points with a line. Choose appropriate markers and line styles to differentiate multiple datasets within the same chart.
2. Set the x-axis and y-axis labels clearly, and make sure the tick marks are appropriately spaced to avoid clutter. This enhances readability and interpretation.
3. Adjust the line thickness (`linewidth`) and line style (`linestyle`) to improve visibility and distinguish different data series.
4. Consider employing a grid (`plt.grid(True)`) to facilitate the estimation of values at various points along the line, improving the chart's utility for data analysis, if necessary.
5. Add a legend (`plt.legend()`) to identify different lines, especially when multiple lines are plotted. Position the legend to avoid obscuring data.
6. Consider using color coding for lines to represent different categories or time periods. Ensure that the colors have enough contrast against the background.
7. Label each data point on the line using `plt.text()` or `plt.annotate()` to display the value of each point. This provides immediate insight into the exact data v
8. Ensure the annotations do not overlap and are placed in a readable manner. Adjust the position of the labels if necessary to maintain clarity.
""",
    "line chart with error bar": """Notes on plotting a line chart with error bars:
1. Use the `errorbar` function to plot the main line chart, specifying `x` and `y` values along with `yerr` for the error margins. This function integrates the line plot with error bars in a single step, ensuring that the error data aligns precisely with the line data.
2. Choose a color and style for the line and markers to enhance visibility and distinguish the main data line from its error bars. For example, a solid line with contrasting error bars can help in distinguishing data trends from their variability.
3. Set the capsize property in the `errorbar` function to add horizontal lines at the tops and bottoms of the error bars, which enhances the readability of the error margins.
4. Adjust the transparency of the error bars using the `alpha` parameter to prevent them from overshadowing the main data line, ensuring that both the data trend and its uncertainty are visible without one dominating the other.
5. Include a legend that explains what the line and the error bars represent, placing it in a position that does not overlap with any critical data points on the chart.
6. Experiment with the axes' limits and scaling to ensure all data points and their error margins are comfortably within the viewable area, enhancing interpretability.
7. Explore different line styles and marker options to add visual variety and highlight different aspects of the data, such as using dashed lines for projections or different markers for subsets of data.
""",
    "pie chart": """Notes on plotting pie charts:
1. Prepare your data so that it sums to 100% or convert it to proportions before plotting. This ensures that the pie chart accurately represents the relative sizes of each category.
2. Use the `autopct` parameter to automatically add labels inside the pie slices with percentage values, enhancing immediate understanding of each category's proportion.
3. Consider employing the `explode` option to slightly separate one or more slices from the rest of the pie, which can be useful for highlighting specific categories.
4. Choose a color palette that provides good contrast between slices for better visual distinction. Avoid using similar shades for adjacent slices.
5. Consider the placement of the legend to ensure it does not overlap with the chart or detract from the data presentation. Positioning it outside the pie chart can often be beneficial.
6. Rotate the start angle of the pie chart using the `startangle` parameter to orient the chart for better layout and readability.
7. Experiment with shadow effects by setting the `shadow` parameter to True, adding depth and a more appealing visual aesthetic to the chart.
""",
    "donut pie chart": """Notes on plotting a donut pie chart:
1. Utilize the `pie` function with the `wedgeprops` parameter to create a hole in the center, setting `wedgeprops=dict(width=0.3)` to adjust the thickness of the donut.
2. Assign distinct colors to each segment to enhance differentiation and visual appeal. Use a color palette that is coherent and appealing.
3. Place labels on or outside the chart to identify each segment, using the `labels` parameter of the `pie` function. Ensure labels are clear and do not overlap with the segments.
4. Adjust the `startangle` parameter to rotate the chart to an orientation that best displays the data and improves readability.
5. Add a legend that clearly identifies what each color represents, ensuring it is positioned to avoid obscuring any part of the chart.
6. Experiment with shadow effects, explode (to pull segments out), and text properties to add depth and focus to important parts of the data.
7. Consider various configurations and styles to explore creative ways of presenting the data, while keeping the chart informative and visually engaging.
""",
    "sector pie chart": """Notes on plotting a sector pie chart:
1. Use the `pie()` function to create the pie chart, providing the data as a list of values that automatically calculates the proportion of each sector.
2. Assign a distinct color to each sector using the `colors` parameter to enhance visual distinction and make the chart more informative.
3. Label each sector directly on the chart using the `labels` parameter, ensuring each label is clear and does not overlap with others. Adjust font size and style as needed for readability.
4. Adjust the `startangle` parameter to rotate the starting point of the first sector, optimizing the chart's orientation for better visual presentation.
5. Utilize the `autopct` parameter to display the percentage value inside each sector, aiding in data interpretation without external references.
6. Experiment with the `explode` parameter to slightly separate one or more sectors from the rest of the pie, highlighting specific data points.
7. Consider adding a legend if additional explanations or categorizations are necessary, placing it outside the pie to avoid blocking any data visualization.
""",
    "ring chart": """Notes on plotting a ring chart:
1. Utilize the `pie` function in Matplotlib but set the `wedgeprops` parameter to include a `width` less than 1 to create a ring rather than a full pie. This inner radius helps differentiate a ring chart from a standard pie chart.
2. Assign distinct colors to each segment for better visual separation and understanding. Use a colormap or manually specify the colors to enhance the chart's aesthetic appeal.
3. Ensure labels are clear and positioned outside the ring to avoid cluttering the chart. Using `bbox_to_anchor` on the legend can help position it optimally without blocking any part of the chart.
4. Adjust the `startangle` parameter to rotate the chart to a starting position that best displays the data segments.
5. Consider adding a central label or title inside the ring to effectively utilize the empty space and provide additional information about the chart.
6. Experiment with different transparency levels (`alpha` values) for the segments to create depth and highlight specific parts of the data.
7. Explore various edge color settings on the segments to define boundaries more clearly if segments are closely colored.
""",
    "bar chart": """Notes on plotting a bar chart:
1. Align the bars along the x-axis using the positions derived from np.arange(len(y_values)), ensuring each bar is centered on its corresponding label for clarity.
2. Set the height of each bar to correspond to the data values, using the `height` parameter in `ax.bar()`. This visually represents the magnitude of each value.
3. Choose distinct colors for each bar to differentiate between data points, or use a consistent color with varying shades to represent different categories or magnitudes.
4. Add text labels above or on the bars to display the exact data values, enhancing readability and providing precise information.
5. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
6. Utilize grid lines along the y-axis to improve the ease of estimating bar values at a glance.
7. Experiment with the bar width (`width` parameter) to find a balance between aesthetics and clarity, ensuring bars are neither too thin to notice nor too thick to overlap or clutter.
""",
    "bar chart with data annotation": """Notes on plotting a bar chart with data annotation:
1. Align the bars along the x-axis using the positions derived from np.arange(len(y_values)), ensuring each bar is centered on its corresponding label for clarity.
2. Set the height of each bar to correspond to the data values, using the `height` parameter in `ax.bar()`. This visually represents the magnitude of each value.
3. Choose distinct colors for each bar to differentiate between data points, or use a consistent color with varying shades to represent different categories or magnitudes.
4. Add text labels above or on the bars to display the exact data values, enhancing readability and providing precise information.
5. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
6. Utilize grid lines along the y-axis to improve the ease of estimating bar values at a glance.
7. Experiment with the bar width (`width` parameter) to find a balance between aesthetics and clarity, ensuring bars are neither too thin to notice nor too thick to overlap or clutter.
8. Position the data annotations clearly, either slightly above the bar or within the bar, ensuring they do not overlap with the bar or other text elements.
9. Format the annotations to match the chart’s style, adjusting font size, color, and alignment to maintain visual coherence and readability.
""",
    "stacked bar chart": """Notes on plotting a stacked bar chart:
1. Organize data into groups where each group represents a category, and within each group, separate the data into subcategories that will be stacked.
2. Use the `bottom` parameter in the `plt.bar` function for stacking subcategories on top of each other. This parameter should be set to the cumulative sum of the previously plotted bars' heights to ensure correct vertical stacking.
3. Assign distinct colors to each subcategory to enhance visual differentiation and ensure each layer within the stack is clearly distinguishable.
4. Label each bar segment directly or use a legend to indicate what each color in the stack represents, ensuring the legend does not overlap with the chart.
5. Adjust the y-axis limits if necessary to accommodate all data without cutting off tall stacks.
6. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
7. Consider experimenting with transparency (alpha setting) to add depth to the visualization and help distinguish overlapping segments.
8. Explore different aesthetics and configurations to emphasize specific aspects of the data, while keeping the overall presentation intuitive and informative.
""",
    "percentage bar chart": """Notes on plotting percentage bar charts:
1. Organize data in a manner that each bar represents a percentage of a whole, ensuring that all bars together sum up to 100% for each category. Use a stacked bar chart if multiple categories are represented within each segment.
2. Align bars horizontally or vertically depending on the layout preference and readability. Horizontal bars are often better for displaying longer labels.
3. Set the x-axis (or y-axis for horizontal bars) to a fixed range of 0-100% to maintain a consistent scale across the chart, which aids in immediate understanding of proportions.
4. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
5. Use distinct colors for different segments within the bars to differentiate the parts of each total percentage. Consider using a consistent color palette that is intuitive (e.g., warmer colors for higher values).
6. Label each bar or segment directly with the percentage value to provide clear, immediate data interpretation without needing to refer to an axis. Ensure labels are readable and do not clutter the visual space.
7. Configure axes and grid lines minimally to avoid visual distraction from the main data representation. Consider disabling the y-axis grid lines in a vertical bar chart.
""",
    "horizontal bar chart": """Notes on plotting horizontal bar charts:
1. Use `barh` method for plotting horizontal bars, where the y-axis typically represents the categories and the x-axis the values. Ensure each bar's y-coordinate corresponds accurately to its category label.
2. Adjust the `height` parameter to control the thickness of the bars, making sure they are neither too thin for visibility nor too thick to overlap if categories are numerous.
3. Apply distinct colors to each bar for better visual separation and to aid in quick identification of different categories. Consider using a color map and legend if the number of categories is large.
4. Align category labels directly with the center of each bar for clarity. This can be achieved by adjusting the `tick_params` and setting the alignment in the `yticks` method.
5. Add value labels on the end of each bar to provide exact data points, enhancing the chart's informational value without cluttering.
6. Consider the scale of the x-axis to ensure it appropriately represents the data range without compressing the bars too much or leaving excessive empty space.
7. Experiment with adding grid lines vertically to improve readability and make it easier to estimate values at a glance.
8. Explore different layout and style configurations to emphasize certain data points or to make the chart more engaging.
""",
    "3D bar chart": """Notes on plotting 3D bar charts:
1. Use the `bar3d` method in Matplotlib, iterate over y_values to plot each column of data.
2. For plotting each column, use np.arange(len(x_labels)) for the X coordinates and [i]*len(x_labels) for the Y coordinates for each group of data. This approach helps avoid overlapping of different data groups. Utilize the bar3d method to draw each set of bars, ensuring that each group is correctly aligned along the x-axis.
3. Set the dimensions of the bars (width, depth), along with other properties such as colors and transparency (alpha), to ensure they are distinct and non-overlapping, thus providing a clear visualization.
4. Ensure that the x-axis and y-axis are properly labeled with categories and groups, respectively. Consider rotating axis labels or adjusting the distance of the axis labels from the axes if they become crowded or overlap.
5. Adjust the viewing angle (`ax.view_init`) to optimize the visibility of all layers in the stacked bars. A poorly chosen angle can obscure data in the rear layers.
6. Employ additional plotting techniques such as grids to enhance the visualization.
7. Experiment with plotting various configurations to add visual variety and highlight different aspects of the data.
""",
    "stacked 3D bar chart": """Notes on plotting a stacked 3D bar chart:
1. Use the `bar3d` method in Matplotlib, stacking data by adjusting the `z` parameter for each subsequent layer of bars. This stacking should be based on the cumulative height of the bars below to avoid visual gaps or overlaps.
2. Choose distinct colors or textures for each layer to clearly differentiate between data sets within each stack. The use of transparency (`alpha` parameter) can also help in distinguishing overlapping areas while maintaining a visual depth.
3. Set the `width` and `depth` parameters uniformly across all bars to maintain consistency and avoid visual distortion. This uniformity helps in comparing the relative sizes of data segments accurately.
4. Ensure that the x-axis and y-axis are properly labeled with categories and groups, respectively. Consider rotating axis labels or adjusting the distance of the axis labels from the axes if they become crowded or overlap.
5. Adjust the viewing angle (`ax.view_init`) to optimize the visibility of all layers in the stacked bars. A poorly chosen angle can obscure data in the rear layers.
6. Encourage creative exploration of different color schemes and lighting effects to enhance the aesthetic appeal and clarity of the data representation.
""",
    "percentage 3D bar chart": """Notes on plotting percentage 3D bar charts:
1. Utilize np.arange(len(x_labels)) for the X coordinates and np.arange(len(y_labels)) for the Y coordinates to establish a grid where each bar will be placed, ensuring clear separation between categories and groups.
2. Use the `bar3d` method to plot each set of bars, setting the Z values as the percentage values of the data. Adjust the height of each bar to represent the percentage accurately.
3. Set uniform bar width and depth across all data points to maintain consistency, while choosing distinct colors for each group to facilitate easy comparison and enhance visual appeal.
4. Normalize the Z-axis to a 0-100 scale to reflect percentage values accurately, ensuring that all bars align with their respective percentage marks.
5. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size or the distance of the axis labels from the axes might be necessary.
6. Consider using a color gradient or varying shades to represent different ranges of percentages, enhancing the interpretability of data.
7. Experiment with different viewing angles and lighting conditions to best showcase the data proportions and to ensure that no data point is obscured.
""",
    "directed node chart": """Notes on plotting directed node charts:
1. Utilize networkx library to handle the graph structure, ensuring nodes and edges are correctly defined. Each node represents an entity, and each directed edge specifies the direction of the relationship.
2. Position nodes in a layout that enhances readability. Common layouts include circular, spring, and shell. The choice of layout should consider the nature of the data and the story you want to tell.
3. Draw arrows on the edges to clearly indicate the direction of each relationship. This can be done using the `arrows=True` parameter in the drawing function.
4. Customize the appearance of nodes and edges by adjusting attributes like color, size, and line style. Different colors or sizes can represent various attributes of the nodes (e.g., centrality, group membership).
5. Label nodes and edges where necessary to provide additional information. Ensure labels are placed to avoid clutter and overlap, possibly adjusting text properties for clarity.
6. Experiment with different visual elements like node shape or edge pattern to make the chart more informative and visually appealing.
""",
    "undirected node chart": """Notes on plotting an undirected node chart:
1. Utilize a graph library like NetworkX to manage and visualize the nodes and edges. Create a graph object and add nodes and edges accordingly.
2. Choose an appropriate layout for the nodes, such as `spring_layout` or `circular_layout`, which positions nodes based on their connectivity or in a circle, respectively. This choice affects the readability and aesthetics of the network.
3. Customize node colors, sizes, and shapes based on attributes such as degree, centrality, or specific metadata to enhance visual distinction and convey additional information.
4. Draw edges with varying thickness or styles (solid, dashed) to represent different types of relationships or weights. Consider using a gradient or varying opacity to indicate the strength of connections.
5. Add labels to nodes and edges where necessary, ensuring they are legible and do not overlap with other elements. You might need to adjust label positions or use label layout algorithms for clarity.
6. Experiment with different color schemes and node arrangements to find the most informative and aesthetically pleasing configuration.
""",
    "radar chart": """Notes on plotting a radar chart:
1. Set up the radar chart framework by defining the number of variables (spokes) corresponding to the dimensions of your data. Use `plt.subplot` with the `polar=True` argument to create a polar plot.
2. Distribute the variables evenly around the circle by calculating the angle for each spoke. This can be achieved with `np.linspace(start=0, stop=2*np.pi, num=len(variables), endpoint=False)` to ensure all variables are spaced equally.
3. Plot data points for each variable on their respective spokes. Connect these points using the `plot` method of the axis object, and close the radar chart by repeating the first value at the end of your data array.
4. When closing the radar chart loop, append the starting angle to the end of the angles array and repeat the first category label. This ensures that the number of angle points matches the number of data points and labels, preventing dimension mismatch errors.
5. Plot each data point on the respective axis, connecting points with lines to form a closed shape, representing one observation or data set. Use different colors or line styles for different data sets to enhance distinction.
6. Adjust the range of each axis, if necessary, to make sure all data points are visible and the chart does not appear overcrowded.
7. Add labels to each axis to clearly indicate what each represents. Position these labels to avoid overlap and ensure readability from any angle.
8. Experiment with different colors, transparencies, and line styles to highlight different aspects of the data and add visual variety.
""",
    "radar chart with area filling": """Notes on plotting a radar chart with area filling:
1. Set up the radar chart framework by defining the number of variables (spokes) corresponding to the dimensions of your data. Use `plt.subplot` with the `polar=True` argument to create a polar plot.
2. Distribute the variables evenly around the circle by calculating the angle for each spoke. This can be achieved with `np.linspace(start=0, stop=2*np.pi, num=len(variables), endpoint=False)` to ensure all variables are spaced equally.
3. Plot data points for each variable on their respective spokes. Connect these points using the `plot` method of the axis object, and close the radar chart by repeating the first value at the end of your data array.
4. Fill the area enclosed by the radar plot using the `fill` method of the axis object, specifying a color and an alpha value for transparency to enhance readability and aesthetic appeal.
5. When closing the radar chart loop, append the starting angle to the end of the angles array and repeat the first category label. This ensures that the number of angle points matches the number of data points and labels, preventing dimension mismatch errors.
6. Adjust the radial limits (range) to make the chart scales clear and to prevent any data from being plotted outside the radar circle.
7. Add labels to each spoke to identify the variables. Position these labels by calculating their angles and using the `text` method with appropriate alignment settings.
8. Experiment with different color schemes and transparency levels to find the best visual representation for the underlying data.
""",
    "area chart": """Notes on plotting an area chart:
1. Use `plt.fill_between` for creating the area under the line, specifying x-values and y-values. This method fills the area between your line plot and the x-axis, effectively creating an area chart.
2. Set appropriate colors and alpha transparency to distinguish between overlapping areas when plotting multiple datasets. This helps in visual differentiation and understanding of layered data.
3. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
4. Consider employing a grid or minor grid lines to improve readability and make it easier to estimate the values represented by the areas, if necessary.
5. Consider customizing the linestyle and linewidth of the plot to enhance aesthetic appeal or to emphasize certain data trends.
6. Experiment with the stacking option (`stacked=True` in `plt.stackplot`) to visualize cumulative totals of different categories over time, providing insights into the relative contributions of each category.
7. Consider adding annotations or labels directly on or near the areas to highlight significant data points or trends, enhancing the informational value of the chart.
""",
    "stacked area chart": """Notes on plotting a stacked area chart:
1. Utilize the `stackplot` function from Matplotlib to layer multiple datasets on top of each other, representing cumulative totals. This function is ideal for showing the contribution of each dataset over time or another variable.
2. Define a clear x-axis (e.g., time or categories) and stack multiple y-values (datasets) on top of each other. Ensure that the order of the datasets is logical and helps in understanding the cumulative effect.
3. Choose distinct, but harmonious colors for each dataset to enhance visual separation while maintaining overall coherence. This helps in distinguishing the layers without overwhelming the viewer.
4. Add a legend to the plot to identify each dataset. Position the legend outside the main plot area to avoid obscuring any data.
5. Consider using transparency (alpha setting) to deal with overlapping areas where colors may blend, ensuring that underlying layers remain visible.
6. Consider annotating significant points or changes in the data directly on the plot to provide context and enhance comprehension, if necessary.
7. Experiment with different color schemes and layer orders to find the most informative and aesthetically pleasing arrangement.
8. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
""",
    "vertical box chart": """Notes on plotting vertical box charts:
1. Arrange data into a list of sequences where each sequence represents a different group or category. This setup is crucial for plotting multiple box plots side by side for comparison.
2. Use the `boxplot` function from Matplotlib, specifying the data list. Set the `vert=True` parameter to ensure the boxes are oriented vertically.
3. Adjust the `positions` parameter if necessary to space the boxes appropriately, avoiding any overlap and ensuring clear distinction between categories.
4. Customize the appearance of the box plots by setting properties such as `patch_artist=True` to fill the boxes with color, and use the `boxprops`, `whiskerprops`, `capprops`, and `medianprops` to style the components of the box plots.
5. When customizing box plots, use `patch_artist=True` correctly and be aware that `PathPatch` objects do not support methods like `get_xy` or `get_xdata`. Instead, access vertices directly for complex shapes: `vertices = path_patch.get_path().vertices`.
6. Label each box plot with appropriate x-axis labels that correspond to the categories represented, enhancing readability and understanding.
7. Consider adding notches to the boxes with the `notch=True` parameter to indicate a confidence interval around the median, which adds an analytical dimension to the chart.
8. Experiment with different color schemes and transparency levels (`alpha` parameter) to make the chart visually appealing and to highlight different data groups effectively. 
""",
    "horizontal box chart": """Notes on plotting horizontal box charts:
1. Use the `boxplot` function with the `vert=False` parameter to orient the boxes horizontally.
2. Organize data into a list where each sublist represents a different group or category for comparison. Ensure that data is pre-processed to remove outliers or handle them appropriately within the chart.
3. Adjust the positions parameter to space the boxes evenly and prevent any overlap, enhancing clarity.
4. Customize the box colors and styles using the `patch_artist=True` parameter, which allows for filling the box with color, and set different colors for each box to distinguish between categories.
5. When customizing box plots, use `patch_artist=True` correctly and be aware that `PathPatch` objects do not support methods like `get_xy` or `get_xdata`. Instead, access vertices directly for complex shapes: `vertices = path_patch.get_path().vertices`.
6. Label each box with appropriate y-axis labels, ensuring they correspond to the data categories represented. Consider rotating or adjusting the font size of the labels if space is constrained.
7. Utilize whisker lengths to represent variability outside the upper and lower quartiles effectively. Adjust the `whis` parameter to control the length of the whiskers based on the data distribution.
8. Experiment with adding notches to the boxes (using `notch=True`) to indicate a confidence interval around the median, which can provide additional insight into the statistical significance of the differences between categories.
""",
    "scatter chart": """Notes on plotting scatter charts:
1. Use `plt.scatter()` for plotting individual data points in the scatter chart. Specify the x and y coordinates, which represent the variables you wish to compare.
2. Choose distinct markers and colors for different data groups to enhance differentiation and visual appeal. Use the `marker` and `color` parameters to customize each data group.
3. Adjust the size of the markers with the `s` parameter based on the importance or weight of the data points, if applicable. This can help in emphasizing certain points over others.
4. Consider adding grid lines using `plt.grid(True)` to improve readability and make it easier to estimate the values of the scattered points, if necessary.
5. Add a legend if there are multiple groups of data points, ensuring it is placed in a position that does not obstruct the data visualization.
6. Explore different axes scales (logarithmic or linear) depending on the distribution of your data to enhance the chart's interpretability.
7. If there are many text labels, consider using automated text placement libraries like `adjustText` to prevent overlapping of labels or annotations.
""",
    "scatter chart with smooth fitting": """Notes on plotting a scatter chart with smooth fitting:
1. Use `plt.scatter()` to plot the raw data points, ensuring each point is clearly distinguishable by using different colors or markers for different categories, if applicable.
2. To add a smooth fitting curve, calculate the fit using an appropriate method (e.g., polynomial fit, spline interpolation) depending on the nature of the data. Use libraries like `numpy` for polynomial fit (`np.polyfit()`, `np.poly1d()`) or `scipy` for spline interpolation (`scipy.interpolate.make_interp_spline()`).
3. Plot the fitting curve using `plt.plot()`, ensuring the line is smooth and clearly visible against the scatter points. Adjust the line style and color to enhance visibility without overshadowing the raw data.
4. Set appropriate axis limits and labels to ensure all data points and the fitting curve are within view and clearly labeled for better understanding.
5. Add a legend to differentiate between the scatter points and the fitting curve, ensuring it is positioned to avoid obscuring any important data.
6. Consider adding a grid or increasing the figure size if the plot appears cluttered or data points overlap significantly.
""",
    "3D scatter chart (bubble chart)": """Notes on plotting a 3D scatter chart (bubble chart):
1. Utilize the `scatter` method from Matplotlib's `Axes3D` module to plot each data point in three-dimensional space. Specify `x`, `y`, and `z` coordinates for each data point to position them accurately.
2. Adjust the `s` parameter (size) in the `scatter` method to represent an additional variable, typically the magnitude of each data point. This helps in visualizing data dimensions as the size of each bubble. Be careful to avoid excessive overlap and occlusion.
3. Use the `c` parameter to assign colors based on another variable or category, enhancing the distinctions between different data groups. Employ a colormap to automate color variations and add a color bar to explain the mapping.
4. Set appropriate axis labels and a chart title that clearly describes the variables represented. Ensure that these texts are positioned in a way that they do not overlap with any data points.
5. Experiment with different viewing angles by adjusting the `elev` and `azim` parameters in the `view_init` method. This allows for the best perspective to interpret the data effectively.
6. Consider adding transparency to the bubbles by adjusting the `alpha` parameter, which can prevent visual clutter and make overlapping points easier to view.
7. Encourage exploration of different marker styles and edge colors for further customization and to highlight specific features of the data.
""",
    "heat map": """Notes on plotting a heat map:
1. Use `imshow` or `pcolormesh` from Matplotlib to plot the heat map, selecting the one that best fits the data's resolution and size. `imshow` is typically used for regular grids and image data, while `pcolormesh` is better for irregular grids.
2. Ensure the data array is correctly oriented; rows should correspond to the y-axis (from top to bottom) and columns to the x-axis (from left to right). Adjust the array orientation using numpy's `np.rot90` or `np.flipud` if necessary.
3. Set appropriate color maps to reflect the nature of the data. For instance, use sequential color maps for continuous data and diverging color maps for data with a critical midpoint.
4. Include a color bar to provide a reference scale for the heat map values, adjusting its position and size to not overlap with the main plot.
5. Adjust the aspect ratio of the plot to 'auto' or a specific value to ensure that each cell in the heat map is correctly proportioned, especially important for non-square data grids.
6. Experiment with different interpolation methods in `imshow` (like 'nearest', 'bicubic', etc.) to see how they affect the visualization's clarity and aesthetics.
7. Consider adding gridlines or annotations directly on the heat map to highlight specific data points or areas, enhancing interpretability without cluttering the visualization.
8. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
""",
    "rose chart": """Notes on plotting a rose chart:
1. Modify the axes to use polar coordinates by setting polar=True or using 'projection='polar' when creating the axis.
2. The chart should consist of multiple sectors, each representing a different category. Assign a different color to each sector to enhance distinction.
3. Add a legend adjacent to the chart that clearly labels the category each sector represents. Ensure that the legend is positioned in a way that does not obscure any part of the chart.
4. Ensure that all sectors evenly cover the entire circumference. Each sector should represent a different category with the same angle, calculated by sector_angle = (2 * np.pi) / num_categories. The radius of each sector should be proportional to its corresponding value.
5. Draw sectors corresponding to different categories by setting the width parameter in ax.bar to sector_angle. This ensures that the angles of these sectors sum up to 360 degrees.
6. Experiment with various configurations to add visual diversity and highlight different aspects of the data.
""",
    "funnel chart": """Notes on plotting a funnel chart:
1. Use descending order for the data points to represent the stages of the funnel, ensuring that each stage visually decreases in size.
2. Plot each segment of the funnel using shapes like trapezoids or rectangles. For a more traditional look, use the `matplotlib.patches` module to draw these shapes, ensuring each subsequent shape is slightly smaller than the one above.
3. Color-code each stage of the funnel to differentiate between the stages effectively. Choose contrasting colors to enhance visual clarity.
4. Label each stage directly on the chart or use annotations to indicate the values or percentages that each stage represents. Position these labels inside or near their respective segments to avoid clutter and maintain readability.
5. Experiment with the aspect ratio and scaling to ensure that the funnel is neither too elongated nor too compressed, which could distort the visual representation of the data.
6. Explore different visual embellishments, such as gradients or patterns, to add depth or emphasis to certain stages of the funnel.
""",
    "waterfall chart": """Notes on plotting a waterfall chart:
1. Start with an initial value and sequentially add or subtract values for subsequent data points to depict increases or decreases effectively.
2. Use color coding to distinguish between positive (e.g., green) and negative (e.g., red) changes, enhancing the chart's readability and impact.
3. Connect each bar with a thin line (or a different marker) to visually link the progression of values, emphasizing the flow from one value to the next.
4. Label each bar with the corresponding value change and the resulting end value to provide clear, immediate data insights to viewers.
5. Adjust the spacing between bars if necessary to prevent any visual overlap and maintain a clean, organized appearance.
6. Consider adding a baseline or a starting line to clearly denote the starting point of the data sequence, aiding in visual orientation.
7. Experiment with adding subtle gradients or shadows to bars for a more polished, visually appealing presentation.
8. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
""",
    "histogram": """Notes on plotting histograms:
1. Choose an appropriate number of bins to effectively represent the distribution of data. Too few bins may oversimplify the data, while too many can overcomplicate the visualization.
2. Set the bin edges explicitly if needed, using the `bins` parameter in `plt.hist()`, to ensure they align with meaningful data points or ranges.
3. Use different colors for histograms when comparing multiple datasets in the same plot to enhance distinction between them.
4. Adjust the transparency of the histograms using the `alpha` parameter to prevent one histogram from completely obscuring another when they overlap.
5. Label the axes clearly, including units of measurement, to ensure that the scale and the nature of the data are immediately understandable.
6. Incorporate a legend if multiple histograms are plotted together, ensuring it is positioned to avoid obscuring any data.
7. Experiment with different histogram orientations (horizontal vs. vertical) and styles (e.g., step, bar) to find the best representation for the data and to add visual interest.
8. Adjust the x-axis labels to avoid overlapping, especially if they are lengthy or numerous. Rotating the labels or adjusting the font size might be necessary.
""",
    "tree map": """Notes on plotting a tree map:
1. Start by defining the hierarchy and size of each rectangle, which represent different categories or subcategories. Ensure that the size of each rectangle is proportional to the data value it represents.
2. Utilize a library or function that supports hierarchical data structuring, such as `squarify.plot`, to automatically calculate and plot the rectangles efficiently.
3. Choose a distinct color palette for different levels or categories to enhance visual separation and understanding. Utilize color gradients within categories to indicate variations in subcategories or data magnitude.
4. Label each rectangle clearly with the category name and, if space permits, include the data value. Ensure labels are legible by adjusting font size and contrast against the rectangle's background color.
5. Consider the overall layout to avoid overly thin or overly elongated rectangles, as these can be difficult to compare visually.
6. Experiment with adding borders between rectangles to define edges clearly, which helps in understanding the division between categories.
7. Explore different color and layout schemes to find the most effective way to convey the hierarchical relationships and data proportions.
""",
}


def get_chart_note(chart_type):
    if chart_type in chart_notes:
        return chart_notes[chart_type]
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")


if __name__ == "__main__":
    try:
        chart_type = input("Enter the chart type: ")
        note = get_chart_note(chart_type)
        print(f"Settings for {chart_type}: {note}")
    except ValueError as e:
        print(e)
