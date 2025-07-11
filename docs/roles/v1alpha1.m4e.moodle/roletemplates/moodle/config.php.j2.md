



# config.php.j2

---
```

<?php  // Moodle configuration file

unset($CFG);  // Ignore this line
global $CFG;  // This is necessary here for PHPUnit execution
$CFG = new stdClass();

{% if moodle_config_context_cache_max_size is defined %}
define('CONTEXT_CACHE_MAX_SIZE', {{ moodle_config_context_cache_max_size }});
{% endif %}
$CFG->dbtype    = '{{ moodle_config_dbtype | default('pgsql') }}';
$CFG->dblibrary = '{{ moodle_config_dblibrary | default('native') }}';
$CFG->dbhost    = '{{ moodle_config_dbhost }}';
$CFG->dbname    = '{{ moodle_config_dbname }}';
$CFG->dbuser    = '{{ moodle_config_dbuser }}';
$CFG->dbpass    = '{{ moodle_config_dbpass }}';
$CFG->prefix    = '{{ moodle_config_prefix | default('mdl_') }}';
$CFG->dboptions = array(
    'dbpersist' => {{ moodle_config_dbpersist | default('false') }},
    'dbsocket'  => {{ moodle_config_dbsocket | default('false') }},
    'dbport'    => '{{ moodle_config_dbport if moodle_config_dbport is defined else '' }}',
    'dbhandlesoptions' => {{ 'true' if moodle_config_dbhandlesoptions is defined and moodle_config_dbhandlesoptions else 'false' }},
    'dbcollation' => '{{ moodle_config_dbcollation | default('utf8mb4_unicode_ci') }}',
    {{ "'fetchbuffersize' => " + moodle_config_fetchbuffersize if moodle_config_fetchbuffersize is defined and moodle_config_fetchbuffersize else "// 'fetchbuffersize' => 100000" }},
);

$CFG->wwwroot   = '{{ moodle_config_wwwroot }}';
$CFG->dataroot  = '{{ moodle_config_dataroot }}';
$CFG->directorypermissions = {{ moodle_config_directorypermissions | default('02777') }};
$CFG->admin = '{{ moodle_config_admin | default('admin') }}';

{% if moodle_config_defaultblocks_override is defined %}
$CFG->defaultblocks_override = '{{ moodle_config_defaultblocks_override }}';
{% endif %}
{% if moodle_config_xsendfile is defined %}
$CFG->xsendfile = '{{ moodle_config_xsendfile }}';
{% endif %}
{% if moodle_config_yuislasharguments is defined %}
$CFG->yuislasharguments = {{ moodle_config_yuislasharguments }};
{% endif %}
{% if moodle_config_db_session is defined %}
$CFG->session_handler_class = '\core\session\database';
$CFG->session_database_acquire_lock_timeout = 120;
{% endif %}
{% if moodle_config_session_redis %}
/**** redis session store ****/
$CFG->session_handler_class = '\core\session\redis';
$CFG->session_redis_host = '{{ moodle_config_session_redis_host if moodle_config_session_redis_host is defined else '127.0.0.1' }}';
{{ '$CFG->session_redis_database = ' + moodle_config_session_redis_port | string + ';  // Optional.' if moodle_config_session_redis_port is defined else '//      $CFG->session_redis_port = 6379;  // Optional.' }}
{{ '$CFG->session_redis_database = ' + moodle_config_session_redis_database + ';  // Optional, default is db 0.' if moodle_config_session_redis_database is defined else '//      $CFG->session_redis_database = 0;  // Optional, default is db 0.' }}
{{ '$CFG->session_redis_auth = ' + "'" + moodle_config_session_redis_auth + "'" + '; // Optional, default is don\'t set one.' if moodle_config_session_redis_auth else "//      $CFG->session_redis_auth = ''; // Optional, default is don't set one." }}
{{ '$CFG->session_redis_prefix = ' + "'" + moodle_config_session_redis_prefix + "'" + "; // Optional, default is don't set one." if moodle_config_session_redis_prefix is defined else "//      $CFG->session_redis_prefix = ''; // Optional, default is don't set one." }}
{{ '$CFG->session_redis_acquire_lock_timeout = ' + moodle_config_session_redis_acquire_lock_timeout | string + ';' if moodle_config_session_redis_acquire_lock_timeout is defined else "//      $CFG->session_redis_acquire_lock_timeout = 120;" }}
{{ '$CFG->session_redis_lock_expire = ' + moodle_config_session_redis_lock_expire | string + ';' if moodle_config_session_redis_lock_expire is defined else "//      $CFG->session_redis_lock_expire = 7200;" }}
{{ '$CFG->session_redis_lock_retry = ' + moodle_config_session_redis_lock_retry  | string + ';' if moodle_config_session_redis_lock_retry is defined else "//      $CFG->session_redis_lock_retry = 100; // Optional wait between lock attempts in ms, default is 100." }}
{{ '$CFG->session_redis_serializer_use_igbinary = ' +  moodle_config_session_redis_serializer_use_igbinary | string | lower + '; // Optional, default is PHP builtin serializer.' if moodle_config_session_redis_serializer_use_igbinary is defined and moodle_config_session_redis_serializer_use_igbinary | bool else "//      $CFG->session_redis_serializer_use_igbinary = false; // Optional, default is PHP builtin serializer." }}
{{ '$CFG->session_redis_compressor = ' + "'" + moodle_config_session_redis_compressor + "'" + "; // Optional, possible values are: 'gzip', 'zstd'" if moodle_config_session_redis_compressor is defined and moodle_config_session_redis_compressor != 'none' else "//      $CFG->session_redis_compressor = 'none'; // Optional, possible values are: 'gzip', 'zstd'" }}

{% endif %}
{% if moodle_config_sslproxy is defined and moodle_config_sslproxy %}
$CFG->sslproxy = true;
{% endif %}
{% if moodle_config_profilingenabled is defined %}
$CFG->profilingenabled=true;
$CFG->earlyprofilingenabled = {{ moodle_config_profilingenabled.earlyprofilingenabled | default('true') }};
$CFG->profilingautofrec = {{ moodle_config_profilingenabled.profilingautofrec | default('20') }};
$CFG->profilingincluded = '{{ moodle_config_profilingenabled.profilingincluded | default('/*view.php,/*index.php') }}';
$CFG->profilinglifetime = {{ moodle_config_profilingenabled.profilinglifetime | default('480') }};
$CFG->pathtodot = '{{ moodle_config_profilingenabled.pathtodot | default('/usr/bin/dot') }}';
{{ "$CFG->profilingallowme = true;" if moodle_config_profilingenabled.profilingallowme is defined and moodle_config_profilingenabled.profilingallowme else '' }}
{{ "$CFG->profilingallowall = true;" if moodle_config_profilingenabled.profilingallowall is defined and moodle_config_profilingenabled.profilingallowall else '' }}
{{ "$CFG->profilingexcluded = '" + moodle_config_profilingenabled.profilingexcluded + "';" if moodle_config_profilingenabled.profilingexcluded is defined else '' }}
{% endif %}
{% if moodle_config_localcachedir is defined and moodle_config_localcachedir %}
$CFG->localcachedir = '{{ moodle_config_localcachedir }}';      // Intended for local node caching.
{% endif %}
{% if moodle_config_extramemorylimit is defined %}
$CFG->extramemorylimit = '{{ moodle_config_extramemorylimit }}';
{% endif %}
{% if moodle_config_disableupdateautodeploy is defined and moodle_config_disableupdateautodeploy %}
$CFG->disableupdateautodeploy = true;
{% endif %}
{% if moodle_config_tool_lockstats is defined %}
$CFG->lock_factory = "\\tool_lockstats\\proxy_lock_factory";
$CFG->proxied_lock_factory = "auto";
{% endif %}
{% if moodle_config_perfdebug is defined and moodle_config_perfdebug %}
$CFG->debug = 32767;
$CFG->perfdebug = 15;
define('MDL_PERF'  , true);
define('MDL_PERFDB'  , true);
define('MDL_PERFTOFOOT', true);
{% endif %}
{% if moodle_config_noemailever is defined and moodle_config_noemailever %}
$CFG->noemailever = '{{ moodle_config_noemailever }}';
{% endif %}
{% if moodle_config_forced_plugin_settings is defined and moodle_config_forced_plugin_settings %}
$CFG->forced_plugin_settings = array(
{%- for plugin, options in moodle_config_forced_plugin_settings.items() -%}
'{{ plugin }}' => array(
{%- for option, value in options.items() -%}
'{{ option }}' => {{ value if value is number else "'" + value + "'" }}
{%- if not loop.last -%}
,
{%- else -%}
)
{%- endif -%}
{%- endfor -%}
{%- if not loop.last -%}
,
{%- else -%}
);
{% endif %}
{% endfor %}
{% endif %}
{% if moodle_config_tool_generator_users_password is defined %}
$CFG->tool_generator_users_password = '{{ moodle_config_tool_generator_users_password }}';
{% endif %}
{% if moodle_config_additional_cfg is defined %}
{% for property, value in moodle_config_additional_cfg.items() %}
$CFG->{{ property }} = {{ value if value is number else "'" + value + "'" }};
{% endfor %}
{% endif %}
{% if moodle_config_additional_block is defined %}
{{ moodle_config_additional_block }}
{% endif %}

require_once(__DIR__ . '/lib/setup.php');

// There is no php closing tag in this file,
// it is intentional because it prevents trailing whitespace problems!

```