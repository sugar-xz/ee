# Configuration parameters

# Maximum number of SQL statements for a single interface
sql_max_number = 20

table_whitelist = ["perm_rolepolicy", "perm_resourcetype"]

# Tables that do not allow full table queries
table_blacklist = ["guard_case", "guard_casehistory", "guard_casemedium", "guard_guard", "guard_guardadmin",
                   "guard_guardcompany", "guard_incident", "guard_monitoringoperator", "guard_note",
                   "guard_siteoperation", "logic_box", "logic_camera", "logic_cameralocation", "logic_camerasavedvideo",
                   "logic_cameravideo", "logic_devicekey", "logic_event", "logic_eventbackup", "logic_inspection",
                   "logic_inspectmedium", "logic_medium", "logic_mediumbackup", "logic_patrol", "logic_person",
                   "logic_robot", "logic_robotsavedvideo", "logic_robotsnap", "logic_robotvideo", "logic_route",
                   "logic_rule", "logic_site", "logic_sitemanagement", "logic_sitemanager", "logic_snap", "logic_task",
                   "logic_waypoint", "logic_waypointhistory"]

# The error message
sql_repeat = "SQL statements have duplication."
sql_redundant = "SQL statement redundancy."
sql_black = "SQL statement query range is too large."
sql_much = "Interface calls SQL statements too many, the sql_number parameter value is exceeded."
sql_update_range = "SQL statements are updated too large."
sql_delete_range = "The entire table was deleted."

# Interface whitelist
interface_whitelist = {
    "GET": ['/api/v1/user/auth/change_password', '/api/v1/user/auth/login', '/api/v1/user/auth/register',
            '/api/v1/user/auth/reset_password', '/api/v1/box/boxes/box_dog_sr_50006/get_meta',
            '/api/v1/box/boxes/12312/get_meta', '/api/v1/box/boxes/qweasd/get_meta', '/api/v1/box/boxes/wqe@',
            '/api/v1/camera/cameras', '/api/v1/box/boxes/get_config', '/api/v1/box/boxes/get_stream_token',
            '/api/v1/box/boxes/get_token', '/api/v1/box/boxes', '/api/v1/camera_video/camera_videos',
            '/api/v1/camera_saved_video/camera_saved_videos', '/api/v1/box/boxes/box_dog_sr_50006',
            '/api/v1/box/boxes/err_box_id', '/api/v1/camera/cameras/1', '/api/v1/camera/cameras/aaa@@',
            '/api/v1/camera/cameras/box_no_exist', '/api/v1/camera/cameras/99999',
            '/api/v1/camera_video/camera_videos/slot', '/api/v1/snap/snaps/slot', '/api/v1/web/meta/all_event_types',
            '/api/v1/event/events/slot', '/api/v1/web/meta/get_agent', '/api/v1/web/meta/get_global',
            '/api/v1/web/meta/get_timezones', '/api/v1/event/events/all', '/api/v1/event/events',
            '/api/v1/inspection/inspections', '/api/v1/user/users/me', '/api/v1/user/users/monitor',
            '/api/v1/event/events/82', '/api/v1/inspection/inspections/183', '/api/v1/inspection/inspections/1111111',
            '/api/v1/inspection/inspections/@', '/api/v1/robot/robots/get_analytics_token',
            '/api/v1/robot/robots/get_config', '/api/v1/robot/robots/get_stream_token',
            '/api/v1/robot/robots/get_token', '/api/v1/robot/robots', '/api/v1/robot_video/robot_videos',
            '/api/v1/robot/robots/robot_dog_sr_20002', '/api/v1/robot/robots/aaa@@',
            '/api/v1/robot/robots/robot_no_exist', '/api/v1/robot/robots/99999', '/api/v1/route/routes/33',
            '/api/v1/robot/robots/robot_dog_sr_20002/get_meta', '/api/v1/robot_video/robot_videos/slot',
            '/api/v1/robot_snap/robot_snaps/slot', '/api/v1/domain_type/domain_types',
            '/api/v1/domain_type/domain_types/3', '/api/v1/domain_type/domain_types/4', '/api/v1/domain/domains',
            '/api/v1/domain/domains/3', '/api/v1/domain/domains/4', '/api/v1/user_node/user_nodes',
            '/api/v1/user_node/user_nodes/3', '/api/v1/user_node/user_nodes/4', '/api/v1/guard/guards',
            '/api/v1/guard_admin/guard_admins', '/api/v1/guard_company/guard_companies',
            '/api/v1/monitoring_operator/monitoring_operators', '/api/v1/guard/guards/21',
            '/api/v1/guard_admin/guard_admins/18', '/api/v1/guard_company/guard_companies/1',
            '/api/v1/monitoring_operator/monitoring_operators/22',
            '/api/v1/map/map/2', '/api/v1/map/map/3'],
    "POST": ['/api/v1/user/auth/login', '/api/v1/user/auth/change_password', '/api/v1/user/auth/register',
             '/api/v1/user/auth/reset_password', '/api/v1/box/boxes/initiate', '/api/v1/box/boxes/authenticate',
             '/api/v1/box/boxes/debug_login', '/api/v1/box/boxes/create_or_update_cameras',
             '/api/v1/camera_saved_video/camera_saved_videos', '/api/v1/box/boxes/delete_cameras',
             '/api/v1/box/boxes/differences', '/api/v1/camera/cameras/saving_video',
             '/api/v1/camera/cameras/auto_update', '/api/v1/camera/cameras/differences', '/api/v1/box/boxes/unclaim',
             '/api/v1/box/boxes/claim', '/api/v1/camera_video/camera_videos', '/api/v1/snap/snaps', '/api/v1/box/boxes',
             '/api/v1/camera_video/camera_videos/save_video', '/api/v1/box/boxes/update_state',
             '/api/v1/camera/cameras', '/api/v1/web/meta/all_event_types', '/api/v1/event/events/camera',
             '/api/v1/robot/robots/initiate', '/api/v1/robot/robots/authenticate', '/api/v1/event/events/robot',
             '/api/v1/user/users/me', '/api/v1/user/users/monitor', '/api/v1/robot/robot_dog_sr_20002/patrols',
             '/api/v1/robot_video/robot_videos', '/api/v1/route/routes', '/api/v1/robot/robots',
             '/api/v1/robot/robots/debug_login', '/api/v1/robot/robots/differences',
             '/api/v1/robot_video/robot_videos/save_video', '/api/v1/robot/robots/unclaim',
             '/api/v1/robot/robots/claim', '/api/v1/robot/robots/update_state', '/api/v1/robot_snap/robot_snaps',
             '/api/v1/device/apns', '/api/v1/device/gcm', '/api/v1/perm/validate_resource_scope',
             '/api/v1/perm/validate_cross_join', '/api/v1/domain_type/domain_types', '/api/v1/domain/domains',
             '/api/v1/domain/domains/4/attach_user', '/api/v1/user_node/user_nodes/create_user_roles',
             '/api/v1/user_node/user_nodes/4/edit_user_roles', '/api/v1/user_node/user_nodes/10/change_parent',
             '/api/v1/user_node/user_nodes/8/change_parent', '/api/v1/user_node/user_nodes/12/remove_user',
             '/api/v1/guard/guards', '/api/v1/guard_admin/guard_admins', '/api/v1/guard_company/guard_companies',
             '/api/v1/monitoring_operator/monitoring_operators'],
    "DELETE": ['/api/v1/camera/cameras/5', '/api/v1/event/events/90', '/api/v1/domain_type/domain_types/7',
               '/api/v1/domain/domains/7', '/api/v1/guard_admin/guard_admins/19'],
    "PUT": ['/api/v1/box/boxes/box_dog_sr_50006', '/api/v1/camera/cameras/1', '/api/v1/camera/cameras/4567895465',
            '/api/v1/camera/cameras/sakjdhsajk', '/api/v1/robot/robots/robot_dog_sr_20001',
            '/api/v1/robot/robots/update_robot_meta', '/api/v1/domain_type/domain_types/9', '/api/v1/domain/domains/8',
            '/api/v1/domain/domains/9', '/api/v1/guard/guards/21', '/api/v1/guard_admin/guard_admins/18',
            '/api/v1/guard_company/guard_companies/2', '/api/v1/monitoring_operator/monitoring_operators/22'],
    "PATCH": ['/api/v1/event/events/updates', '/api/v1/domain_type/domain_types/9']

}

# Interface‘SQL whitelist
sql_whitelist = {
    "sql_range": {
        "select": ["sql"]
    },
    "sql_repeat": {
        "select": [
            # #   /box/boxes/authenticate
            # 'SELECT (1) AS "a" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'box\' AND "algorithm_producttype"."type" = \'test_lee\') LIMIT 1',
            # #   /box/boxes/debug_login
            # 'SELECT (1) AS "a" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'box\' AND "algorithm_producttype"."type" = \'test_lee\') LIMIT 1',
            # #   /robot/robots/authenticate
            # 'SELECT (1) AS "a" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'robot\' AND "algorithm_producttype"."type" = \'test_li\') LIMIT 1',
            # 'SELECT "logic_customizedalgorithm"."id", "logic_customizedalgorithm"."algorithm_id", "logic_customizedalgorithm"."index", "logic_customizedalgorithm"."code_name", "logic_customizedalgorithm"."name", "algorithm_algorithm"."id", "algorithm_algorithm"."code_name" FROM "logic_customizedalgorithm" INNER JOIN "logic_organization" ON ("logic_customizedalgorithm"."organization_id" = "logic_organization"."id") INNER JOIN "algorithm_algorithm" ON ("logic_customizedalgorithm"."algorithm_id" = "algorithm_algorithm"."id") WHERE "logic_organization"."owner_id" = 1',
            # 'SELECT "algorithm_producttype"."id", "algorithm_producttype"."created_at", "algorithm_producttype"."updated_at", "algorithm_producttype"."category", "algorithm_producttype"."type", "algorithm_producttype"."meta" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'robot\' AND "algorithm_producttype"."type" = \'test_li\') ORDER BY "algorithm_producttype"."id" ASC LIMIT 1',
            # 'SELECT DISTINCT ON ("algorithm_algorithm"."id") "algorithm_algorithm"."id", "algorithm_algorithm"."created_at", "algorithm_algorithm"."updated_at", "algorithm_algorithm"."code_name", "algorithm_algorithm"."name", "algorithm_algorithm"."name_en", "algorithm_algorithm"."name_zh_hans", "algorithm_algorithm"."intro", "algorithm_algorithm"."index" FROM "algorithm_algorithm" INNER JOIN "algorithm_productalgorithm" ON ("algorithm_algorithm"."id" = "algorithm_productalgorithm"."algorithm_id") INNER JOIN "algorithm_producttype" ON ("algorithm_productalgorithm"."product_type_id" = "algorithm_producttype"."id") INNER JOIN "algorithm_productalgorithm" T4 ON ("algorithm_algorithm"."id" = T4."algorithm_id") INNER JOIN "algorithm_producttype" T5 ON (T4."product_type_id" = T5."id") WHERE ("algorithm_producttype"."category" = \'robot\' AND T5."type" = \'test_li\')',
            # #   /robot/robots/debug_login
            # 'SELECT "algorithm_producttype"."id", "algorithm_producttype"."created_at", "algorithm_producttype"."updated_at", "algorithm_producttype"."category", "algorithm_producttype"."type", "algorithm_producttype"."meta" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'robot\' AND "algorithm_producttype"."type" = \'test_li\') ORDER BY "algorithm_producttype"."id" ASC LIMIT 1',
            # 'SELECT (1) AS "a" FROM "algorithm_producttype" WHERE ("algorithm_producttype"."category" = \'robot\' AND "algorithm_producttype"."type" = \'test_li\') LIMIT 1',
            # 'SELECT "logic_customizedalgorithm"."id", "logic_customizedalgorithm"."algorithm_id", "logic_customizedalgorithm"."index", "logic_customizedalgorithm"."code_name", "logic_customizedalgorithm"."name", "algorithm_algorithm"."id", "algorithm_algorithm"."code_name" FROM "logic_customizedalgorithm" INNER JOIN "logic_organization" ON ("logic_customizedalgorithm"."organization_id" = "logic_organization"."id") INNER JOIN "algorithm_algorithm" ON ("logic_customizedalgorithm"."algorithm_id" = "algorithm_algorithm"."id") WHERE "logic_organization"."owner_id" = 1',
            # 'SELECT DISTINCT ON ("algorithm_algorithm"."id") "algorithm_algorithm"."id", "algorithm_algorithm"."created_at", "algorithm_algorithm"."updated_at", "algorithm_algorithm"."code_name", "algorithm_algorithm"."name", "algorithm_algorithm"."name_en", "algorithm_algorithm"."name_zh_hans", "algorithm_algorithm"."intro", "algorithm_algorithm"."index" FROM "algorithm_algorithm" INNER JOIN "algorithm_productalgorithm" ON ("algorithm_algorithm"."id" = "algorithm_productalgorithm"."algorithm_id") INNER JOIN "algorithm_producttype" ON ("algorithm_productalgorithm"."product_type_id" = "algorithm_producttype"."id") INNER JOIN "algorithm_productalgorithm" T4 ON ("algorithm_algorithm"."id" = T4."algorithm_id") INNER JOIN "algorithm_producttype" T5 ON (T4."product_type_id" = T5."id") WHERE ("algorithm_producttype"."category" = \'robot\' AND T5."type" = \'test_li\')',
        ]
    },
    "sql_much": {
        "endpoint": [
            "post path"
        ],
        "sql_max_number": 30
    },
    "sql_redundant": {
        "select": [
            # #   /user/auth/register
            # "select auth_user [] ['auth_user.id.=']",
            # #   /api/v1/perm/validate_resource_scope Post (Values are different and sorted)
            # "select perm_resourcetype [] ['perm_resourcetype.code_name.=', 1]",
            # #   /api/v1/user_node/user_nodes/10/change_parent
            # "select * org_usernode ['t'] ['t.id.=', 'org_usernode.id.=', 'sort:org_usernode.tree_id', 'sort:org_usernode.lft']",

        ], "update": [
            "update table [set.key]"
        ], "insert": [
            "insert table"
        ], "delete": [
            "delete table"
        ]
    }
}
