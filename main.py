import requests
import plotly.express as px
import datetime

s = requests.get("https://enkasseienfestforening.dk/timetrial/json/").json()
tt, = [o for o in s if o["id"] == 1849]
durations = tt["durations"]

start_time = datetime.datetime.strptime(
    tt["start_time"], "%Y-%m-%d %H:%M:%S%z")

time_since_start = [start_time + datetime.timedelta(
    seconds=sum(durations[:i])) for i in range(1, len(durations))]

fig = px.scatter(x=time_since_start, y=list(range(1, len(durations))))

fig.update_layout(title={'text': f'En kasse i en KA$$ {start_time.year}'},
                  paper_bgcolor="black", font={'color': 'white'})
fig.update_yaxes(range=[0, 31], title={'text': 'Antal bajere'})
fig.update_xaxes(title={'text': 'Tidspunkt'})

fig.write_html("figure.html")
