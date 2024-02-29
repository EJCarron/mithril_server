# import flast module
from flask import Flask, request
import mithril

# instance of flask application
app = Flask(__name__)


# home route that returns below text when root url is accessed
@app.route("/createnetwork")
def createnetwork():
    body = request.get_json()

    try:
        mithril.createnetwork(ch_officer_ids=body.get('ch_officer_ids', None),
                              ch_company_numbers=body.get('ch_company_numbers', None),
                              ol_node_ids=body.get('ol_node_ids', None),
                              save_json_path=body.get('save_json_path', ''),
                              save_csvs_path=body.get('save_csvs_path', ''),
                              save_xlsx_path=body.get('save_xlsx_path', ''),
                              save_neo4j=body.get('save_neo4j', False),
                              overwrite_neo4j=body.get('overwrite_neo4j', False),
                              same_as=body.get('same_as', None),
                              expand=body.get('expand', 0)
                              )
    except:
        return 'fail'

    return 'success'


if __name__ == '__main__':
    app.run()
