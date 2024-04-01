from django.db import connection
from ..models import developer


class developerservice:

    def save(self, mobj):
        mobj.save()



    def search(self, params):
        pageNo = (params["pageNo"] - 1) * 5
        print("pageNo ======>>>>>>>", pageNo)
        dname = params.get("developer_name", "")
        depname = params.get("department", "")
        id = params.get("id", "")
        sql = "select * from ors_developer where 1=1"
        if dname != "":
            sql += " and developer_name like '" + dname + "%%' "
        if depname != "":
            sql += " and department like '" + depname + "%%' "
        if id != "":
            sql += " and id = " + id
        sql += " limit %s, %s"
        print("sql ======>>>>>>", sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, 5])
        result = cursor.fetchall()
        columnName = ("id", "developer_name", "department", "project", "status", "submitting date")
        res = {
            "data": []
        }
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def edit(self, val):
        q = developer.objects.filter()
        q = q.filter(id=val)
        developerList = [developer.to_developer() for developer in q]
        if (developerList[0]):
            return developerList[0]
        else:
            return None

    def get(self, id):
        r = developer.objects.get(id=id)
        return r

    def delete(self, obj):
        obj.delete()

    def preload(self):
        r = developer.objects.all()
        return r