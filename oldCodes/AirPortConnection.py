airports = [
  "BGI",
  "CDG",
  "DEL",
  "DOH",
  "DSM",
  "EWR",
  "EYW",
  "HND",
  "ICN",
  "JFK",
  "LGA",
  "LHR",
  "ORD",
  "SAN",
  "SFO",
  "SIN",
  "TLV",
  "BUD"
]

routes = [
  ["DSM", "ORD"],
  ["ORD", "BGI"],
  ["BGI", "LGA"],
  ["SIN", "CDG"],
  ["CDG", "SIN"],
  ["CDG", "BUD"],
  ["DEL", "DOH"],
  ["DEL", "CDG"],
  ["TLV", "DEL"],
  ["EWR", "HND"],
  ["HND", "ICN"],
  ["HND", "JFK"],
  ["ICN", "JFK"],
  ["JFK", "LGA"],
  ["EYW", "LHR"],
  ["LHR", "SFO"],
  ["SFO", "SAN"],
  ["SFO", "DSM"],
  ["SAN", "EYW"]
]

startingAirport = "LGA"

class AirportNode:
  def __init__(self, airport):
    self.airport = airport
    self.connections = []
    self.isReachable = True
    self.unreachableAirport = []

def depthFirstTraverseAirport(airportGraph, airport, visitedAirport):
  if airport in visitedAirport:
    return
  
  visitedAirport[airport] = True
  connections = airportGraph[airport].connections
  for connection in connections:
    depthFirstTraverseAirport(airportGraph, connection, visitedAirport)

def getUnreachableAirports(airportGraph, airports, startingAirport):
  visitedAirport = {}
  depthFirstTraverseAirport(airportGraph, startingAirport, visitedAirport)

  unreachableAirport = []
  for airport in airports:
    if airport in visitedAirport:
      continue
    airportNode = airportGraph[airport]
    airportNode.isReachable = False
    unreachableAirport.append(airportNode)
  return unreachableAirport

def CreateAirportGraph(airports, routes):
  airportGraph = {}
  for airport in airports:
    airportGraph[airport] = AirportNode(airport)
  for route in routes:
    airport, connection = route
    airportGraph[airport].connections.append(connection)
  return airportGraph

def markUnrachableAirports(airportGraph, unreachableAirportNodes):
  for airportNode in unreachableAirportNodes:
    airport = airportNode.airport
    unreachableAirports = []
    depthFirstAddUnrachable(airportGraph, airport, unreachableAirports, {})
    airportNode.unreachableAirport = unreachableAirports
  print(unreachableAirportNodes)

def depthFirstAddUnrachable(airportGraph, airport, unreachableAirports, visitedAirport):
  if airportGraph[airport].isReachable or airport in visitedAirport:
    return
  
  visitedAirport[airport] = True
  unreachableAirports.append(airport)
  connections = airportGraph[airport].connections
  for connection in connections:
    depthFirstAddUnrachable(airportGraph, connection, unreachableAirports, visitedAirport)

def getResult(airportGraph, unreachableAirportNodes):
  unreachableAirportNodes.sort(key = lambda airport : len(airport.unreachableAirport), reverse=True)
  print(unreachableAirportNodes)

  countConn = 0
  for airportNode in unreachableAirportNodes:
    if airportNode.isReachable:
      continue
    countConn += 1
    connections = airportNode.unreachableAirport
    for connection in connections:
      airportGraph[connection].isReachable = True
  return countConn




def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    airportGraph = CreateAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirports(airportGraph, airports, startingAirport)
    markUnrachableAirports(airportGraph, unreachableAirportNodes)
    return getResult(airportGraph, unreachableAirportNodes)


print(airportConnections(airports, routes, startingAirport))
