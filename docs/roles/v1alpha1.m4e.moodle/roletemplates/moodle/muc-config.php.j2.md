



# muc-config.php.j2

---
```

#!/usr/bin/env php
<?php
define('CLI_SCRIPT', true);
define('CACHE_DISABLE_ALL', true); // This prevents reading of existing caches.

$MOODLE_COMMIT = getenv('MOODLE_COMMIT') ?: false;
$MOODLE_APP = getenv('MOODLE_APP') ?: '/var/www/html';
require($MOODLE_APP . '/config.php');
require_once($CFG->libdir.'/clilib.php');
require_once($CFG->dirroot.'/cache/locallib.php');

list($options, $unrecognized) = cli_get_params([
    'help'  => false,
    'file' => false,
    'json' => false,
    'overwrite' => false,
    'reset' => false
], [
    'h' => 'help',
    'f' => 'file',
    'j' => 'json',
    'r' => 'reset'
]);

if ($unrecognized) {
    $unrecognized = implode(PHP_EOL.'  ', $unrecognized);
    cli_error(get_string('cliunknowoption', 'core_admin', $unrecognized));
}

if ($options['help'] or !($options['file'] or $options['json'])) {
    cli_writeln("Config a muc store
Options:
    -h, --help              Print out this help
    -f, --file              File to load (exclusive with option --json)
    -j, --json              Json content to load (exclusive with option --file)
    -r, --reset             Reset MUC config before creating and configuring store
Example:
php muc-config.php -r -f=muc-config.json

If adding a apcu store, use 'php -d apc.enable_cli=1' to bypass moodle 'are_requirements_met'. Example:
php -d apc.enable_cli=1 muc-config.php -r -f=muc-config.json");
    exit(2);
}

/**
 * Constants
 */
define('CACHE_STORE_MODES', array(
    'application' => cache_store::MODE_APPLICATION,
    'session' => cache_store::MODE_SESSION,
    'request' => cache_store::MODE_REQUEST
));

/**
 * Variables
 */
// cache config
$cache_config = array();
if ($options['file']) {
    load_json_file($options['file']);
} else {
    load_json($options['json']);
}
// whether to reset muc completely
$cache_config_reset = $options['reset'];
// whether to edit store config if changed
$cache_config_overwrite = $options['overwrite'];
// config writer
$cw = null;

/**
 * Logic
 */
if ($cache_config_reset) {
    reset_cache();
}

// config writer
$cw = cache_config_writer::instance();

write_stores();

write_rules();

/**
 * Functions
 */
function write_stores() {
    global $cw, $cache_config;
    if (array_key_exists('stores', $cache_config)){
        $stores = $cache_config["stores"];
        $all_stores = $cw->get_all_stores();
        foreach ($stores as $name => $store) {
            if(array_key_exists($name, $all_stores)){
                cli_writeln("Editing store: " . $name);
                $cw->edit_store_instance($name, $store['type'], $store['config']);
            }else{
                cli_writeln("Adding store: " . $name);
                $cw->add_store_instance($name, $store['type'], $store['config']);
            }
        }
    }
}

function write_rules() {
    global $cw, $cache_config;
    if (array_key_exists('rules', $cache_config)){
        $definitions = $cw->get_definitions();
        $rules = $cache_config["rules"];
        foreach ($rules as $mode => $mode_rules) {
            cli_writeln("Rules for mode: " . $mode);
            foreach ($mode_rules as $mode_rule) {
                $conditions = array();
                $stores = $mode_rule["stores"];
                if (array_key_exists('conditions', $mode_rule)){
                    $conditions = $mode_rule["conditions"];
                }
                foreach ($definitions as $definition_id => $definition) {
                    set_definition_mappings_if_matched($definition_id, $definition, $stores, $conditions, $mode);
                }
            }
        }
    }
}

function set_definition_mappings_if_matched($definition_id, $definition, $stores, $conditions, $mode) {
    global $cw;
    if ($definition["mode"] !==  CACHE_STORE_MODES[$mode]){
        return;
    }
    $name_present = false;
    $name_match = false;
    // handle name condition, if present
    if (array_key_exists("name", $conditions)){
        $name_present = true;
        $name_match = $definition_id === $conditions["name"];;
        unset($conditions["name"]);
    }
    // handle the rest of conditions
    $conditions_match = array_reduce(array_keys($conditions), function($carry, $condition_key) use ($conditions, $definition) {
        return $carry && array_key_exists($condition_key, $definition) && ($conditions[$condition_key]  === $definition[$condition_key]);
    }, true);
    $definition_match_all = $conditions_match && !($name_present xor $name_match);
    if($definition_match_all){
        $definition_class = cache_definition::load($definition_id, $definition);
        $suitable_stores = $cw->get_stores($definition_class->get_mode(), $definition_class->get_requirements_bin());
        $mapping_already_set = false;
        if ($suitable_stores){
            foreach ($stores as $store) {
                if (!array_key_exists($store, $suitable_stores)){
                    cli_writeln("Setting mapping '" . $store . "'->'" . $definition_id . "'");
                    cli_error("Store not suitable: '" . $store . "'");
                }
            }
            foreach ($cw->get_definition_mappings() as $mapping) {
                if ($mapping['definition'] == $definition_id){
                    $mapping_already_set = true;
                    break;
                }
            }
            if(!$mapping_already_set){
                cli_writeln("Setting mapping for: '" . $definition_id . "'");
                $cw->set_definition_mappings($definition_id, $stores);
            }
        }
    }
}

function load_json_file($file_path){
    // Check if the file exists
    if (file_exists($file_path)) {
        // Read the file contents
        $json_data = file_get_contents($file_path);

        // Parse the JSON data
        load_json($json_data);
    } else {
        cli_error("File not found.");
    }
}

function load_json($json_data){
    global $cache_config;
    // Parse the JSON data
    $data = json_decode($json_data, true);

    if ($data === null) {
        // An error occurred while decoding JSON
        cli_error("Error parsing JSON data.");
    } else {
        // JSON file successfully loaded and parsed
        // You can now work with the data
        // Example: Print the contents of the JSON file
        $cache_config = $data;
    }
}

function reset_cache() {
    global $CFG;
    cli_writeln("Resetting cache config");
    $muc_file = isset($CFG->altcacheconfigpath) ? $CFG->altcacheconfigpath : $CFG->dataroot.'/muc/config.php';
    unlink($muc_file);
    cache_factory::reset();
}

```