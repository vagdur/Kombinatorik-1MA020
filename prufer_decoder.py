import igraph as ig

def decode (prufer_code):
    
    vertices = list(range(len(prufer_code) + 2))                                        # skapar en lista med noderna 0 --> n + 2.                   
    edge_set = []                                                                       # skapar en tom lista som ska fyllas på med kanst-set.
    i = 0                                                               
    while prufer_code:                                                                  # kör så länge det finns något i prufer_code.
        if vertices[i] not in prufer_code:                                              # om minsta elementet inte finns i pruferkoden så vill vi dra en kant mellan 
            edge_set.append(tuple((prufer_code[0], vertices[i])))                       # första elementet i prufer_code och den minsta möjliga elementet bland noderna
            prufer_code.remove(prufer_code[0])                                          # sen tar vi bort de elementen ur pruferkoden och bland noderna.
            vertices.remove(vertices[i])
            i = 0                                                                       # sätter i till 0 igen så att vi kan starta om sökningen.
        else:
            i += 1                                                                      # annars ökar vi index med 1 och går vidare till nästa nod.
        
    edge_set.append(tuple((vertices[0], vertices[1])))                                  # drar en kant mellan de två noderna som finns kvar.
    return edge_set

def plot_from_edge_set (edge_set, labels):                                                           
    
    g = ig.Graph(n = len(labels), edges = edge_set)
    layout = g.layout(layout = "auto")
    ig.plot(g, target="graph.pdf", layout=layout, vertex_label = labels)
    return
    
    
prufer_code = [0,1,6,2,1,5,1]
prufer_code2 =  []
prufer_code3 = [3,0,2,3]
labels = list(range(len(prufer_code3)+2))    
edge_set = decode(prufer_code3)
plot_from_edge_set(edge_set, labels)
