from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "pen.see.hen-919"))
session = driver.session()

result = session.run("MATCH (n:Apps) RETURN n.appname AS appname")

resultx = session.run("MATCH (p:Pattern) RETURN p.targetcloud AS targetcloud")

resulty = session.run("MATCH (a:AppConfig) RETURN a.appstartscripts AS startscripts")

resultappcfg = session.run("MATCH (a:AppConfig) WHERE a.appstartscripts = '/etc/rc2.d/S90httpd' RETURN a.appstartscripts AS appscripts")

for record in result:
    print("%s" % (record["appname"]))

for xrecord in resultx:
    print("%s" % (xrecord["targetcloud"]))

for yrecord in resulty:
    print("%s" % (yrecord["startscripts"]))

for apprecord in resultappcfg:
    print ("Apps Config")
    print("%s" % (apprecord["appscripts"]))
session.close()
