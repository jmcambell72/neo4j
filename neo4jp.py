from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "pen.see.hen-919"))
session = driver.session()

result = session.run("MATCH (n:Apps) RETURN n.appname AS appname")

for record in result:
    print("%s" % (record["appname"]))

session.close()
