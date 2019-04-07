

def plot_table(desc, tab_data, height=700, width=700):
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
    from plotly.graph_objs import layout
    init_notebook_mode()

    trace = go.Table(
        header=dict(values=desc),
        cells=dict(values=tab_data))

    layout = Layout(
        showlegend=False,
        height=height,
        width=width,
    )

    data = [trace]
    fig = dict(data=data, layout=layout)
    iplot(fig)