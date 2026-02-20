import plotly.express as px

# Line plot for yearly rate trends

def lineplot(df, x_col, y_col, color_col = None , line_col = None):
    # Line plot
    p = px.line(
    data_frame = df,
    x = x_col,
    y = y_col,
    color = color_col,
    line_dash = line_col)

    # Set layout and styling compactly
    
    p.update_layout(
    template = "simple_white",         # theme_bw equivalent
    title_text = "",
    title_font = dict(color = "black", size = 18, family = "Arial, sans-serif"))

    # Axis styling
    p.update_xaxes(
        title_text = "Years", 
        title_font_size = 20,
        title_font_color = "black",
        tickfont_size = 14, 
        tickfont_color = "black",
        showgrid = True,
        gridcolor = "lightgray",
        gridwidth = 1)
    
    p.update_yaxes(
        title_text = "Rate",
        title_font_size = 20, 
        title_font_color = "black",
        tickfont_size = 14,
        tickfont_color = "black")
    
    return p



