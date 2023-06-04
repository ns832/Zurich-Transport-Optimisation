from Pyomo import Graph
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'Webapp',
    password = open("password.txt").read() 
)

cur = conn.cursor() 
cur.execute('SELECT * FROM "zurichdist"' )
conn.commit()
busstops = cur.fetchall()
graph = Graph()
nodes = set()
for values in busstops:
    # print(values)
    (from_node, to_node, distance, id) = values
    if from_node not in graph.edges[to_node]:
        graph.add_edge(from_node, to_node, distance)
        nodes.add(from_node), nodes.add(to_node)
print(graph.edges)
for node in nodes:
    graph.add_node(node)
print(graph.nodes)

