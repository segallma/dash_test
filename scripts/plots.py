from load_data import load_cases_rates
import plotly.express as px


df_plot0 = load_cases_rates(path=".\data\cases_by_group.csv")

p = px.line(
    df_plot0,
    x = "year",
    y = "rate",
    color = "group",
    line_dash = "sex")


# Changing formatting

# Set layout and styling compactly
p.update_layout(
    template="simple_white",         # theme_bw equivalent
    title_text="",
    title_font=dict(color="black", size=18, family="Arial, sans-serif")
)

# Axis styling
p.update_xaxes(title_text="Rate", title_font_size=20, title_font_color="black",
                 tickfont_size=14, tickfont_color="black")
p.update_yaxes(title_text="Years", title_font_size=20, title_font_color="black",
                 tickfont_size=14, tickfont_color="black")


p.show(renderer="browser")