from flask import Flask, render_template
import numpy as np
app = Flask(__name__)

import plotly.graph_objects as go

def generateMatrixOnMap():
    min_val, max_val = 0, 50

    map = np.random.uniform(1, 50, size=(max_val, max_val))
    map[0, 0] = 0
    map[max_val - 1, max_val - 1] = 0

    # Initialize auxiliary arrays
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    originmap = np.ones((max_val, max_val), dtype=int) * np.nan
    visited = np.zeros((max_val, max_val), dtype=bool)
    finished = False
    x, y = np.int(0), np.int(0)
    count = 0

    # Loop Dijkstra until reaching the target cell
    while not finished:
        # move to x+1,y
        if x < max_val - 1:
            if distmap[x + 1, y] > map[x + 1, y] + distmap[x, y] and not visited[x + 1, y]:
                distmap[x + 1, y] = map[x + 1, y] + distmap[x, y]
                originmap[x + 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x-1,y
        if x > 0:
            if distmap[x - 1, y] > map[x - 1, y] + distmap[x, y] and not visited[x - 1, y]:
                distmap[x - 1, y] = map[x - 1, y] + distmap[x, y]
                originmap[x - 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x,y+1
        if y < max_val - 1:
            if distmap[x, y + 1] > map[x, y + 1] + distmap[x, y] and not visited[x, y + 1]:
                distmap[x, y + 1] = map[x, y + 1] + distmap[x, y]
                originmap[x, y + 1] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x,y-1
        if y > 0:
            if distmap[x, y - 1] > map[x, y - 1] + distmap[x, y] and not visited[x, y - 1]:
                distmap[x, y - 1] = map[x, y - 1] + distmap[x, y]
                originmap[x, y - 1] = np.ravel_multi_index([x, y], (max_val, max_val))

        visited[x, y] = True
        dismaptemp = distmap
        dismaptemp[np.where(visited)] = np.Infinity
        # now we find the shortest path so far
        minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
        x, y = minpost[0], minpost[1]
        if x == max_val - 1 and y == max_val - 1:
            finished = True
        count = count + 1

    # Start backtracking to plot the path
    mattemp = map.astype(float)
    x, y = max_val - 1, max_val - 1
    path = []
    mattemp[np.int(x), np.int(y)] = np.nan

    while x > 0.0 or y > 0.0:
        path.append([np.int(x), np.int(y)])
        xxyy = np.unravel_index(np.int(originmap[np.int(x), np.int(y)]), (max_val, max_val))
        x, y = xxyy[0], xxyy[1]
        mattemp[np.int(x), np.int(y)] = np.nan
    path.append([np.int(x), np.int(y)])

    print('mattempje:')

    print(mattemp)

    print('put je:')

    tackePuta = []

    normalizovanX = ((np.random.uniform(44, 50, max_val * max_val))).tolist()
    normalizovanY = ((np.random.uniform(22, 23, max_val * max_val))).tolist()
    counter = 0
    for idx, x in np.ndenumerate(mattemp):
        if str(x) == 'nan':
            idx = (idx[0] + normalizovanX[counter], idx[1] + normalizovanY[counter])
            tackePuta.append(idx)
            counter += 1



    print('The path length is: ' + np.str(distmap[max_val - 1, max_val - 1]))

    maxnum = 1  # sta je maxnum??
    print('The dump/mean path should have been: ' + np.str(maxnum * max_val))

    print('tacke puta su:')

    print(tackePuta)


    return tackePuta

@app.route('/')
def index():
    return 'Hakaton welcome';

@app.route('/testMap')
def testMap():
    #bg lat, lon:  44.8125,  20.4612

    # tackePuta = generateMatrixOnMap()


    latitude = [44.0970, 44.3209]
    longitude = [20.6576, 20.8954]
    # tackePuta[0] = (46.0970, 19.6576)
    # tackePuta[-1] = (43.3209, 21.8954)


    # for tacke in tackePuta:
    #     latitude.append(tacke[0])
    #     longitude.append(tacke[1])

    print('latitude i longitude:')

    print(latitude)
    print(longitude)




    # lat = [46.0970, 43.3209],
    # lon = [19.6576, 21.8954],
    fig = go.Figure(go.Scattermapbox(
        mode="markers+lines",
        lat=latitude,
        lon=longitude,
        marker={'size': 4, 'color': '#f00'}))
    #granice regiona:
    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lat = [44.445289, 43.503542, 43.503542, 44.445289, 44.445289],
        lon = [20.314415, 20.314415, 22.172852, 22.172852, 20.314415],
        marker = {'size': 10, 'color': '#ff0'}))

    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            'style': "stamen-terrain",
            'center': {'lat': 44.0128, 'lon': 20.9114},
            'zoom': 6.8})

    fig.write_html('templates/second_figure.html')

    return render_template('second_figure.html')


if __name__ == '__main__':
    app.run()