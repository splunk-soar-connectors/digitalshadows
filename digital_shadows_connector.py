# File: digital_shadows_connector.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

import json

import phantom.app as phantom
from phantom.base_connector import BaseConnector

from digital_shadows_consts import DS_ACTION_NOT_SUPPORTED
from ds_databreach_connector import DSDataBreachConnector
from ds_incidents_connector import DSIncidentsConnector
from ds_intelligence_incidents_connector import DSIntelligenceIncidentsConnector
from ds_on_poll_connector import DSOnPollConnector
from ds_search_entities_connector import DSSearchEntitiesConnector
from ds_test_connectivity_connector import DSTestConnectivityConnector


class DigitalShadowsConnector(BaseConnector):

    def __init__(self):
        super(DigitalShadowsConnector, self).__init__()

    def test_connectivity(self):
        self.save_progress("Testing connectivity")
        self.save_progress("test")
        test_connectivity_connector = DSTestConnectivityConnector(self)
        return test_connectivity_connector.test_connectivity()

    def get_incident_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        incidents_connector = DSIncidentsConnector(self)
        return incidents_connector.get_incident_by_id(param)

    def get_incident_review_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        incidents_connector = DSIncidentsConnector(self)
        return incidents_connector.get_incident_review_by_id(param)

    def get_incident_list(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        incidents_connector = DSIncidentsConnector(self)
        return incidents_connector.get_incident_list(param)

    def post_incident_review(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        incidents_connector = DSIncidentsConnector(self)
        return incidents_connector.post_incident_review(param)

    def get_intelligence_incident_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        intelligence_incidents_connector = DSIntelligenceIncidentsConnector(self)
        return intelligence_incidents_connector.get_intelligence_incident_by_id(param)

    def get_intel_incident_ioc_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        intelligence_incidents_connector = DSIntelligenceIncidentsConnector(self)
        return intelligence_incidents_connector.get_intel_incident_ioc_by_id(param)

    def get_intelligence_incident(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        intelligence_incidents_connector = DSIntelligenceIncidentsConnector(self)
        return intelligence_incidents_connector.get_intelligence_incident(param)

    def get_data_breach(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach(param)

    def get_data_breach_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach_by_id(param)

    def get_data_breach_record(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach_record(param)

    def get_data_breach_record_by_id(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach_record_by_id(param)

    def get_data_breach_record_by_username(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach_record_by_username(param)

    def get_data_breach_record_reviews(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.get_data_breach_record_reviews(param)

    def post_breach_record_review(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        databreach_connector = DSDataBreachConnector(self)
        return databreach_connector.post_breach_record_review(param)

    def search_entities(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        search_entities_connector = DSSearchEntitiesConnector(self)
        return search_entities_connector.search_entities(param)

    def on_poll(self, param):
        self.save_progress("Entered the function")
        self.save_progress("processing")
        on_poll_connector = DSOnPollConnector(self)
        return on_poll_connector.on_poll(param)

    def handle_action(self, param):

        # get action which is needed to run
        action_id = self.get_action_identifier()

        if param:
            self.save_progress("Ingesting handle action in: {}".format(param))
        if action_id == 'test_connectivity':
            return self.test_connectivity()
        elif action_id == 'get_incident_by_id':
            return self.get_incident_by_id(param)
        elif action_id == 'get_incident_review_by_id':
            return self.get_incident_review_by_id(param)
        elif action_id == 'get_incident_list':
            return self.get_incident_list(param)
        elif action_id == 'post_incident_review':
            return self.post_incident_review(param)
        elif action_id == 'get_intelligence_incident_by_id':
            return self.get_intelligence_incident_by_id(param)
        elif action_id == 'get_intel_incident_ioc_by_id':
            return self.get_intel_incident_ioc_by_id(param)
        elif action_id == 'get_intelligence_incident':
            return self.get_intelligence_incident(param)
        elif action_id == 'get_data_breach':
            return self.get_data_breach(param)
        elif action_id == 'get_data_breach_by_id':
            return self.get_data_breach_by_id(param)
        elif action_id == 'get_data_breach_record':
            return self.get_data_breach_record(param)
        elif action_id == 'get_data_breach_record_by_id':
            return self.get_data_breach_record_by_id(param)
        elif action_id == 'get_data_breach_record_by_username':
            return self.get_data_breach_record_by_username(param)
        elif action_id == 'get_data_breach_record_reviews':
            return self.get_data_breach_record_reviews(param)
        elif action_id == 'post_breach_record_review':
            return self.post_breach_record_review(param)
        elif action_id == 'search_entities':
            return self.search_entities(param)
        elif action_id == 'on_poll':
            return self.on_poll(param)
        else:
            self.save_progress(DS_ACTION_NOT_SUPPORTED.format(action_id))
            return self.set_status(phantom.APP_ERROR, DS_ACTION_NOT_SUPPORTED.format(action_id))


if __name__ == '__main__':

    import sys

    if len(sys.argv) < 2:
        print("No test json specified as input")
        sys.exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = DigitalShadowsConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
