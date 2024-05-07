from eidospy import Eidos

if __name__ == "__main__":
    eidos = Eidos("https://api.eidos.space/rpc/ce52c92a-5c10-4acd-8638-ed0e5b19741e")
    space = eidos.space("eidos3")
    table = space.table("67d7857386544a30ae312ee4509e0e17")
    for row in table.rows.query({}, {}):
        print(row["title"], row["_id"])
