from flask import Flask, render_template
import numpy as np
app = Flask(__name__)

import plotly.graph_objects as go


def readCSV():
    file = open("obradjeni_podaci/poljoprivreda.csv")
    numpy_array = np.loadtxt(file, delimiter=",")

    return numpy_array


def generateMatrixOnMap(lonA, lonB, latC, latD, startPoint, endPoint):
    min_val, max_val = 50, 50

    #trenutno radi testiranja se i dalje koristi random generisanje matrice
    map = np.random.uniform(2, 3, size=(min_val, max_val))

    # za zastitu:
    map = readCSV()

    min_val, max_val = map.shape


    koeficijentX = (lonB - lonA) / min_val
    koeficijentY = (latD - latC) / max_val


    endPoint = (415, 587)


    for idx, x in np.ndenumerate(map):
        newIdx = (lonA + idx[0] * koeficijentX, latD - idx[1] * koeficijentY)
        if newIdx == startPoint:
            startPoint = idx
        if newIdx == endPoint:
            endPoint = idx





    #poziva se kao:
    # generateMatrixOnMap(20.314415, 22.172852, 43.503542, 44.445289, (0, 0), (49, 49))

    map[startPoint[0], startPoint[1]] = -999
    map[endPoint[0], endPoint[1]] = -999

    # Initialize auxiliary arrays
    distmap = np.ones((min_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    originmap = np.ones((min_val, max_val), dtype=int) * np.nan
    visited = np.zeros((min_val, max_val), dtype=bool)
    finished = False
    x, y = np.int(0), np.int(0)
    count = 0

    # Loop Dijkstra until reaching the target cell
    while not finished:
        # move to x+1,y
        if x < min_val - 1:
            if distmap[x + 1, y] > map[x + 1, y] + distmap[x, y] and not visited[x + 1, y]:
                distmap[x + 1, y] = map[x + 1, y] + distmap[x, y]
                originmap[x + 1, y] = np.ravel_multi_index([x, y], (min_val, max_val))
        # move to x-1,y
        if x > 0:
            if distmap[x - 1, y] > map[x - 1, y] + distmap[x, y] and not visited[x - 1, y]:
                distmap[x - 1, y] = map[x - 1, y] + distmap[x, y]
                originmap[x - 1, y] = np.ravel_multi_index([x, y], (min_val, max_val))
        # move to x,y+1
        if y < max_val - 1:
            if distmap[x, y + 1] > map[x, y + 1] + distmap[x, y] and not visited[x, y + 1]:
                distmap[x, y + 1] = map[x, y + 1] + distmap[x, y]
                originmap[x, y + 1] = np.ravel_multi_index([x, y], (min_val, max_val))
        # move to x,y-1
        if y > 0:
            if distmap[x, y - 1] > map[x, y - 1] + distmap[x, y] and not visited[x, y - 1]:
                distmap[x, y - 1] = map[x, y - 1] + distmap[x, y]
                originmap[x, y - 1] = np.ravel_multi_index([x, y], (min_val, max_val))

        visited[x, y] = True
        dismaptemp = distmap
        dismaptemp[np.where(visited)] = np.Infinity
        # now we find the shortest path so far
        minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
        x, y = minpost[0], minpost[1]
        if x == min_val - 1 and y == max_val - 1:
            finished = True
        count = count + 1

    # Start backtracking to plot the path
    mattemp = map.astype(float)
    x, y = min_val - 1, max_val - 1
    path = []
    mattemp[np.int(x), np.int(y)] = np.nan

    while x > 0.0 or y > 0.0:
        path.append([np.int(x), np.int(y)])
        xxyy = np.unravel_index(np.int(originmap[np.int(x), np.int(y)]), (min_val, max_val))
        x, y = xxyy[0], xxyy[1]
        mattemp[np.int(x), np.int(y)] = np.nan
    path.append([np.int(x), np.int(y)])

    print('mattempje:')

    print(mattemp)

    print('put je:')

    dobreTacke = []
    loseTacke = []


    koeficijentX = (lonB - lonA) / min_val
    koeficijentY = (latD - latC) / max_val

    for idx, x in np.ndenumerate(mattemp):
        idx = (lonA + idx[0] * koeficijentX, latD - idx[1] * koeficijentY)
        if str(x) == 'nan':
            dobreTacke.append(idx)
        else:
            loseTacke.append(idx)



    print('The path length is: ' + np.str(distmap[min_val - 1, max_val - 1]))

    maxnum = 1  # sta je maxnum??
    print('The dump/mean path should have been: ' + np.str(maxnum * max_val))



    return (dobreTacke, loseTacke)

@app.route('/')
def index():
    return 'Hakaton welcome';

@app.route('/testMap')
def testMap():
    #bg lat, lon:  44.8125,  20.4612

    # tackePuta = generateMatrixOnMap()

    startPoint = (20.314415, 44.445289)
    endPoint = (22.13568326, 43.52237694)

    allTacke = generateMatrixOnMap(20.314415, 22.172852, 43.503542,44.445289, startPoint, endPoint)

    dobreTackeLat = []
    dobreTackeLon = []

    for tacka in allTacke[0]:
        dobreTackeLat.append(tacka[1])
        dobreTackeLon.append(tacka[0])

    loseTackeLat = []
    loseTackeLon = []

    for tacka in allTacke[1]:
        loseTackeLat.append(tacka[1])
        loseTackeLon.append(tacka[0])

    latitude = [20.6576, 20.8954]
    longitude = [44.0970, 44.3209]
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
        lon=longitude,
        lat=latitude,
        marker={'size': 4, 'color': '#f00'}))
    #granice regiona:
    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lon=[20.314415, 20.314415, 22.172852, 22.172852, 20.314415],
        lat = [44.445289, 43.503542, 43.503542, 44.445289, 44.445289],
        marker = {'size': 10, 'color': '#ff0'}))


    #dobre tacke, normalizovane:
    fig.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=dobreTackeLon,
        lat=dobreTackeLat,
        marker={'size': 10, 'color': '#00f'}))

    #
    # #lose tacke, normalizovane:
    # fig.add_trace(go.Scattermapbox(
    #     mode="markers",
    #     lon=loseTackeLon,
    #     lat=loseTackeLat,
    #     marker={'size': 10, 'color': '#f00'}))

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