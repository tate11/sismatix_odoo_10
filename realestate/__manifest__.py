# -*- coding: utf-8 -*-
{
    'name': 'Realestate Management',
    'version': '1.0.1',
    'Author': "Eman Taha",
    'category': 'Other',
    'sequence': 20,
    'summary': 'Realestate Management',
    'depends': ['base','l10n_generic_coa','sale_crm','account','account_voucher','document','account_budget','account_asset','analytic','web_calendar','crm','portal','account_accountant','mail','report'],
    'data': [
        'security/property_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/property_views.xml',
        'views/asset_views.xml',
        'report/account_move_report_view.xml',
        'views/analytic_account_views.xml',
        'views/account_views.xml',
        'views/account_category_views.xml',
        'views/commesion_views.xml',
        'report/property_external_report.xml',
        'wizard/contract_expiry_report_view.xml',
        'wizard/send_mail_view.xml',
        'wizard/send_sms_view.xml',
        'wizard/tenancy_detail_by_tenant_report_view.xml',
        'wizard/tenancy_detail_property_report_view.xml',
        'wizard/tenancy_final_detail_property_report_view.xml',
        'wizard/tenancy_final_detail_property_report_view_ar.xml',
        'wizard/safety_certificate_expiry_view.xml',
        'wizard/income_report_view.xml',
        'wizard/document_expiry_view.xml',
        'wizard/property_per_location.xml',
        'wizard/book_to_available.xml',
        'wizard/crm_make_sale_view.xml',
        'wizard/renew_tenancy_view.xml',
        'report/contract_expiry_view.xml',
        'report/property_per_location_report.xml',
        'report/income_expenditure_view.xml',
        'report/safety_certificate_expiry_view.xml',
        'report/document_expiry_view.xml',
        'report/tenancy_detail_by_tenant_view.xml',
        'report/tenancy_detail_by_property_view.xml',
        'report/tenancy_final_detail_by_property_view.xml',
        'report/tenancy_final_detail_by_property_view_ar.xml',
        'report/report.xml',
        'report/gfa_report_view.xml',
        'report/operational_cost_report_view.xml',
        'report/investment_report_view.xml',
        'report/occupancy_performance_report_view.xml',
        'views/crm_lead_views.xml',
        'views/sale_views.xml',
        'views/wallet_views.xml',
        'report/report_realestate_wallet.xml',
        'wizard/realestate_wallet.xml',
    ],
    'demo': [
        'data/account_asset_demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
