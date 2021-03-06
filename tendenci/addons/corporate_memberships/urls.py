from django.conf.urls.defaults import *

urlpatterns = patterns('tendenci.addons.corporate_memberships.views',
    url(r'^$', 'search', name="corp_memb"),
    url(r"^get_app_fields/$",
        "get_app_fields_json",
        name="corpmemberships.get_app_fields"),

    url(r"^applications/(?P<slug>[\w\-]+)/preview/$",
        "app_preview",
        name="corpmembership_app.preview"),
    url(r"^applications/add_pre/$",
        "corpmembership_add_pre",
        name="corpmembership.add_pre"),
    url(r"^applications/add/$",
        "corpmembership_add",
        name="corpmembership.add"),
    url(r"^(?P<slug>[\w\-]+)/add/$",
        "corpmembership_add",
        name="corpmembership.add"),
    url(r"^applications/add_conf/(?P<id>\d+)/$",
        "corpmembership_add_conf",
        name="corpmembership.add_conf"),
    url(r"^applications/edit/(?P<id>\d+)/$",
        "corpmembership_edit",
        name="corpmembership.edit"),
    url(r"^applications/view/(?P<id>\d+)/$",
        "corpmembership_view",
        name="corpmembership.view"),
    url(r"^applications/search/$",
        "corpmembership_search",
        name="corpmembership.search"),
    url(r"^applications/mycorps/$",
        "corpmembership_search", {'my_corps_only': True},
        name="corpmembership.mycorps"),
    url(r"^applications/index/$",
        "index",
        name="corpmembership.index"),
    url(r"^applications/delete/(?P<id>\d+)/$",
        "corpmembership_delete",
        name="corpmembership.delete"),
    url(r"^applications/approve/(?P<id>\d+)/$",
        "corpmembership_approve",
        name="corpmembership.approve"),
    url(r"^renewal/(?P<id>\d+)/$", "corp_renew",
        name="corpmembership.renew"),
    url(r"^renewal_conf/(?P<id>\d+)/$", "corp_renew_conf",
        name="corpmembership.renew_conf"),
    url(r'^roster/$', 'roster_search',
        name="corpmembership.roster_search"),
    url(r"^download/(?P<cm_id>\d+)/(?P<field_id>\d+)/$",
        "download_file",
        name="corpmembership.download_file"),

    # import to CorpMembership
    url(r"^import/$", "import_upload",
        name="corpmembership.import"),
    url(r"^import/download/$", "download_template",
        name="corpmembership.download_template"),
    url(r"^import/preview/(?P<mimport_id>\d+)/$",
        "import_preview",
        name="corpmembership.import_preview"),
    url(r"^import/check_preprocess_status/(?P<mimport_id>\d+)/$",
        "check_preprocess_status",
        name="corpmembership.check_preprocess_status"),
    url(r"^import/process/(?P<mimport_id>\d+)/$",
        "import_process",
        name="corpmembership.import_process"),
    url(r"^import/status/(?P<mimport_id>\d+)/$",
        "import_status",
        name="corpmembership.import_status"),
    url(r"^import/get_status/(?P<mimport_id>\d+)/$",
        "import_get_status",
        name="corpmembership.import_get_status"),

    # export CorpMembership
    url(r"^corp-export/$",
        "corpmembership_export",
        name="corpmembership.export"),

    # edit corp reps
    url(r"^edit_corp_reps/(?P<id>\d+)/$", "edit_corp_reps",
        name="corpmembership.edit_corp_reps"),
    url(r'^corp_reps_lookup/$', 'corp_reps_lookup',
        name="corp_membership.reps_lookup"),
    url(r'^delete_corp_rep/(?P<id>\d+)/$', 'delete_corp_rep',
        name="corp_membership.delete_rep"),

    # notice
    (r'^notices/', include('tendenci.addons.corporate_memberships.notices.urls')),

    # report
    url(r"^reports/summary/$", "summary_report",
        name="corp_membership.summary_report"),

# To Be Deleted
    url(r"^(?P<slug>.*)/add_pre/$", "add_pre", name="corp_memb.add_pre"),
    #url(r"^(?P<slug>.*)/add/$", "add", name="corp_memb.add"),
    url(r"^(?P<slug>.*)/add/(?P<hash>[\d\w]+)$", "add",
        name="corp_memb.anonymous_add"),
    url(r"^add_conf/(?P<id>\d+)/$", "add_conf", name="corp_memb.add_conf"),
    url(r"^edit/(?P<id>\d+)/$", "edit", name="corp_memb.edit"),
    url(r"^edit_reps/(?P<id>\d+)/$", "edit_reps", name="corp_memb.edit_reps"),
    #url(r"^list/$", "list_view", name="corp_memb.list"),
    url(r"^search/$", "search", name="corp_memb.search"),
    url(r"^index/$", "index", name="corp_memb.index"),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name="corp_memb.delete"),
    url(r'^delete_rep/(?P<id>\d+)/$', 'delete_rep',
        name="corp_memb.delete_rep"),
    url(r"^renew/(?P<id>\d+)/$", "renew", name="corp_memb.renew"),
    url(r"^renew_conf/(?P<id>\d+)/$", "renew_conf",
        name="corp_memb.renew_conf"),
    url(r"^approve/(?P<id>\d+)/$", "approve", name="corp_memb.approve"),
    url(r"^(?P<id>\d+)/$", "view", name="corp_memb.view"),
    url(r'^reps_lookup/$', 'reps_lookup', name="corp_memb.reps_lookup"),

#    # import
#    url(r"^import/$", "corp_import", name="corp_import"),
#    url(r"^import/upload-file/$", "corp_import",
#        kwargs={'step': (1, 'upload-file')},
#        name="corp_memb_import_upload_file"),
#    url(r"^import/map-fields/$", "corp_import",
#        kwargs={'step': (2, 'map-fields')},
#        name="corp_memb_import_map_fields"),
#    url(r"^import/preview/$", "corp_import",
#        kwargs={'step': (3, 'preview')},
#        name="corp_memb_import_preview"),
#    url(r"^import/confirm/$", "corp_import",
#        kwargs={'step': (4, 'confirm')},
#        name="corp_memb_import_confirm"),
#    url(r'^import/download-csv-template/$', 'download_csv_import_template',
#        name="corp_memb_import_download_template"),
#    url(r'^import/download-invalid_records/$',
#        'corp_import_invalid_records_download',
#        name="corp_memb_import_download_invalid"),

    # export
    url(r"^export/$", "corp_export", name="corp_export"),

    # reports
    url(r"^reports/corp_mems_over_time/$", "new_over_time_report",
        name="reports-corp-mems-over-time"),
    url(r"^reports/corp_mems_summary/$", "corp_mems_summary",
        name="reports-corp-mems-summary"),
)
