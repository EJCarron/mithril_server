# import flast module
from flask import Flask, request, make_response, jsonify
import mithril

# instance of flask application
app = Flask(__name__)


# home route that returns below text when root url is accessed
@app.route("/createnetwork", methods=['POST'])
def createnetwork():
    body = request.get_json()

    try:
        network = mithril.createnetwork(core_nodes=body.get('core_nodes', []),
                                        save_csvs_path=body.get('save_csvs_path', ''),
                                        save_xlsx_path=body.get('save_xlsx_path', ''),
                                        save_neo4j=body.get('save_neo4j', False),
                                        overwrite_neo4j=body.get('overwrite_neo4j', False),
                                        same_as=body.get('same_as', None),
                                        expand=body.get('expand', 0),
                                        network_name=body.get('network_name', '')
                                        )

        resp = make_response(network.to_json(), 200)
        return resp
    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/add_offshore_leak_connections_to_network", methods=['POST'])
def add_offshore_leak_connections_to_network():
    body = request.get_json()

    try:

        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        matches = body.get('matches', None)
        if matches is None:
            resp = make_response('no matches', 400)
            return resp

        updated_network = mithril.add_offshore_leak_connections_to_network(network=network, matches=matches)

        resp = make_response(updated_network.to_json(), 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/add_electoral_commission_donation_connections_to_network", methods=['POST'])
def add_electoral_commission_donation_connections_to_network():
    body = request.get_json()

    try:

        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        matches = body.get('matches', None)
        if matches is None:
            resp = make_response('no matches', 400)
            return resp

        updated_network = mithril.add_electoral_commission_donation_connections_to_network(network=network,
                                                                                           matches=matches)

        resp = make_response(updated_network.to_json(), 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route('/export_network', methods=['POST'])
def export_network():
    body = request.get_json()

    try:

        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        if body.get('save_csvs_path', '') != '':
            mithril.exportcsvs(network=network, export_path=body['save_csvs_path'])

        if body.get('save_xlsx_path', '') != '':
            mithril.exportxlsx(network=network, export_path=body['save_xlsx_path'])

        if body.get('save_neo4j', False):
            mithril.exportgraph(network=network, overwrite_neo4j=body.get('overwrite_neo4j', False))

        if body.get('export_timeline_path', '') != '':
            mithril.export_timeline(network=network, export_path=body['export_timeline_path'])

        resp = make_response('export complete', 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/find_electoral_commission_donation_connections", methods=['POST'])
def find_electoral_commission_donation_connections():
    body = request.get_json()

    try:
        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        potential_matches = mithril.find_potential_electoral_commission_donation_matches(network, None)

        resp = make_response(jsonify(potential_matches), 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/find_ol_connections", methods=['POST'])
def find_ol_connections():
    body = request.get_json()

    try:
        print('LOOKING FOR OL CONNECTION')
        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        potential_matches = mithril.find_potential_offshore_leaks_matches(network)

        resp = make_response(jsonify(potential_matches), 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/expand", methods=['POST'])
def expand():
    body = request.get_json()

    try:
        network_dict = body.get('network', None)

        if network_dict is None:
            return make_response('no network dingus', 400)

        network = mithril.make_network_from_dict(network_dict)

        target_node_ids = body.get('node_ids', None)

        expanded_network = mithril.expand_network(network=network, target_node_ids=target_node_ids)

        resp = make_response(expanded_network.to_json(), 200)

        return resp

    except Exception as e:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/setconfig", methods=['POST'])
def setconfig():
    body = request.get_json()

    try:
        mithril.setconfig(**body)

        resp = make_response('fuck you', 200)
        return resp

    except:
        resp = make_response('You fucked up', 400)
        return resp


@app.route("/companies_house_search", methods=['POST'])
def companies_house_search():
    body = request.get_json()

    try:
        search_result = mithril.companies_house_search(query=body['query'],
                                                       page_number=body['page_number'],
                                                       search_type=body.get('search_type', None)
                                                       )

        return make_response(jsonify(search_result), 200)
    except Exception as e:
        print(e)
        resp = make_response('You fucked up', 400)
        return resp

# @app.route("/export_timeline")
# def export_timeline():
#     body = request.get_json()
#
#     try:
#         network_dict = body.get('network', None)
#
#         if network_dict is None:
#             return make_response('no network dingus', 400)
#
#         network = mithril.make_network_from_dict(network_dict)
#
#         export_path = body.get('export_path', None)
#
#         if export_path is None:
#             return make_response('no export path dingus', 400)
#
#         mithril.export_timeline(network, export_path)
#
#         return make_response('success', 200)
#
#     except Exception as e:
#         resp = make_response('You fucked up', 400)
#         return resp

if __name__ == '__main__':
    app.run()
