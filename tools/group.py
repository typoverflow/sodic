roadDict = {
    276183: 0,
    276184: 1,
    275911: 2, 
    275912: 3,
    276240: 4,
    276241: 5,
    276264: 6,
    276265: 7,
    276268: 8,
    276269: 9,
    276737: 10,
    276738: 11
}

groupDict = {
    276183: 0,
    276184: 0,
    275911: 1, 
    275912: 0,
    276240: 2,
    276241: 2,
    276264: 2,
    276265: 2,
    276268: 2,
    276269: 2,
    276737: 3,
    276738: 3
}


def iimap(road_id):
    return roadDict.get(road_id, -1)


def igmap(road_id):
    return groupDict.get(road_id, -1)