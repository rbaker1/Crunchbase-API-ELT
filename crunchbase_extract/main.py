from py_crunchbase import PyCrunchbase, Entities
import pickle
import io
import json
from datetime import datetime

class CrunchbaseExtractor:
    """
    This is the class that will extract organizations from Crunchbase
    """

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def callAPI(self):
        limit_n = 15

        def objectNamer():
            prefix_str = 'cb_org_extract'
            dt_string = datetime.now().strftime("%Y%m%d%H%M%S")
            suffix_str = '.json'

            return prefix_str + dt_string + suffix_str

        def apitooutput(data):
            output = []
            for i in data:
                output.append(i)
               # r = json.dumps(output)
            output_io = io.BytesIO()
            pickle.dump(output, output_io)
            output_io.seek(0)
            return output_io

        pycb = PyCrunchbase(self.api_key)  # needs to be as secret AWS
        api = pycb.search_organizations_api()
        org_facet_ids = Entities.Organization.Facets
        cb_data = api.select(
            'acquirer_identifier',
            'aliases',
            'categories',
            'category_groups',
            'closed_on',
            'company_type',
            'contact_email',
            'created_at',
            'delisted_on',
            'demo_days',
            'description',
            'diversity_spotlights',
            'entity_def_id',
            'equity_funding_total',
            'exited_on',
            'facebook',
            'facet_ids',
            'founded_on',
            'founder_identifiers',
            'funding_stage',
            'funding_total',
            'funds_total',
            'hub_tags',
            'identifier',
            'investor_identifiers',
            'investor_stage',
            'investor_type',
            'ipo_status',
            'last_equity_funding_total',
            'last_equity_funding_type',
            'last_funding_at',
            'last_funding_total',
            'last_funding_type',
            'layout_id',
            'legal_name',
            'linkedin',
            'listed_stock_symbol',
            'location_group_identifiers',
            'location_identifiers',
            'name',
            'num_acquisitions',
            'num_alumni',
            'num_articles',
            'num_current_advisor_positions',
            'num_current_positions',
            'num_diversity_spotlight_investments',
            'num_employees_enum',
            'num_enrollments',
            'num_event_appearances',
            'num_exits',
            'num_exits_ipo',
            'num_founder_alumni',
            'num_founders',
            'num_funding_rounds',
            'num_funds',
            'num_investments',
            'num_investors',
            'num_lead_investments',
            'num_lead_investors',
            'num_past_positions',
            'num_portfolio_organizations',
            'num_sub_organizations',
            'operating_status',
            'override_layout_id',
            'owner_identifier',
            'permalink',
            'permalink_aliases',
            'phone_number',
            'program_application_deadline',
            'program_duration',
            'program_type',
            'rank_delta_d30',
            'rank_delta_d7',
            'rank_delta_d90',
            'rank_org',
            'rank_principal',
            'revenue_range',
            'school_method',
            'school_program',
            'school_type',
            'short_description',
            'status',
            'stock_exchange_symbol',
            'stock_symbol',
            'twitter',
            'updated_at',
            'uuid',
            'valuation',
            'valuation_date',
            'website',
            'website_url',
            'went_public_on'
        ).where(
           # num_employees_enum__includes=['c_00051_00100'],
            location_identifiers__includes=['f110fca2-1055-99f6-996d-011c198b3928'],
            facet_ids__includes=[org_facet_ids.company]
        ).execute()

        return apitooutput(cb_data), objectNamer()
