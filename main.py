import snap

Graph = snap.TUNGraph.New()

edgeList = snap.LoadEdgeList(snap.PUNGraph, "facebook.txt", 0, 1)

# Add nodes
for NI in edgeList.Nodes():
    Graph.AddNode(NI.GetId())

# Add edges
for EI in edgeList.Edges():
    Graph.AddEdge(EI.GetSrcNId(), EI.GetDstNId())

# Overview
numberOfNodes = snap.CntNonZNodes(Graph)
numberOfEdges = edges = Graph.GetEdges()

print("Number of nodes: " + str(numberOfNodes))
print("Number of edges: " + str(numberOfEdges))
print("")

# Plot
snap.PlotInDegDistr(Graph, "distribution", "In-degree distribution")
snap.PlotOutDegDistr(Graph, "distribution", "Out-degree distribution")

# Weakly Connected Components
ComponentDist = snap.TIntPrV()
snap.GetWccSzCnt(Graph, ComponentDist)

print("Weakly Connected Components:")
for comp in ComponentDist:
    print("  Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))
print("")

# Hits (hubs and authorities)
NIdHubH = snap.TIntFltH()
NIdAuthH = snap.TIntFltH()
snap.GetHits(Graph, NIdHubH, NIdAuthH)
print("Top 10 hubs:")
for idx,item in enumerate(sorted(NIdHubH, key=lambda elem:NIdHubH[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.2f" % (item, NIdHubH[item]))
print("")

print("Top 10 authorities:")
for idx,item in enumerate(sorted(NIdAuthH, key=lambda elem:NIdAuthH[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.2f" % (item, NIdAuthH[item]))
print("")

# Page rank
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)
print("Top 10 page rank scores:")
for idx,item in enumerate(sorted(PRankH, key=lambda elem:PRankH[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.5f" % (item, PRankH[item]))
print("")

# Degree centrality
centralityDictionary = {}
for NI in Graph.Nodes():
    DegCentr = snap.GetDegreeCentr(Graph, NI.GetId())
    centralityDictionary[NI.GetId()] = DegCentr
print("Top 10 degree centrality nodes:")
for idx,item in enumerate(sorted(centralityDictionary, key=lambda elem:centralityDictionary[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.5f" % (item, centralityDictionary[item]))
print("")

# Closeness centrality
for NI in Graph.Nodes():
    CloseCentr = snap.GetClosenessCentr(Graph, NI.GetId())
    centralityDictionary[NI.GetId()] = CloseCentr
print("Top 10 closeness nodes:")
for idx,item in enumerate(sorted(centralityDictionary, key=lambda elem:centralityDictionary[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.5f" % (item, centralityDictionary[item]))
print("")

# Farness centrality
for NI in Graph.Nodes():
    FarCentr = snap.GetFarnessCentr(Graph, NI.GetId())
    centralityDictionary[NI.GetId()] = FarCentr
print("Top 10 farness nodes:")
for idx,item in enumerate(sorted(centralityDictionary, key=lambda elem:centralityDictionary[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.5f" % (item, centralityDictionary[item]))
print("")

# Betweenness centrality
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
print("Top 10 betweenness:")
for node in Nodes:
    print "node: %d centrality: %f" % (node, Nodes[node])
for edge in Edges:
    print "edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge])
print("")

# Eigen centrality
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(Graph, NIdEigenH)
print("Top 10 eigen centrality:")
for idx,item in enumerate(sorted(NIdEigenH, key=lambda elem:NIdEigenH[elem], reverse=True)):
    if idx == 10:
        break
    print("%d\t%0.5f" % (item, NIdEigenH[item]))