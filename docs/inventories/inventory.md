# inventory
Kubernetes \(K8s\) inventory source for operator sdk

## Synopsis

Fetch containers using a label selector and hash to match resources with it

Group containers \(hosts\) hierarchically by CR info\, pods\, and app\.kubernetes\.io labels


## Requirements

The below requirements are needed on the host that executes this module.

- python \>\= 2\.7
- openshift \>\= 0\.6
- PyYAML \>\= 3\.11


## Parameters

  plugin (True, any, None)
    token that ensures this is a source file for the \'inventory\' plugin\.

  cr_cwd (optional, any, None)
    custom resource directory where ansible run is stored

  connection (optional, any, None)
    Optional dict of cluster connection settings\. If no connection are provided\, the default <em>\~/\.kube/config</em> and active context will be used\, and objects will be returned for all namespaces the active user is authorized to access\.

    name (optional, any, None)
      Optional name to assign to the cluster\. If not provided\, a name is constructed from the server and port\.

    kubeconfig (optional, any, None)
      Path to an existing Kubernetes config file\. If not provided\, and no other connection options are provided\, the OpenShift client will attempt to load the default configuration file from <em>\~/\.kube/config\.json</em>\. Can also be specified via K8S\_AUTH\_KUBECONFIG environment variable\.

    context (optional, any, None)
      The name of a context found in the config file\. Can also be specified via K8S\_AUTH\_CONTEXT environment variable\.

    host (optional, any, None)
      Provide a URL for accessing the API\. Can also be specified via K8S\_AUTH\_HOST environment variable\.

    api_key (optional, any, None)
      Token used to authenticate with the API\. Can also be specified via K8S\_AUTH\_API\_KEY environment variable\.

    username (optional, any, None)
      Provide a username for authenticating with the API\. Can also be specified via K8S\_AUTH\_USERNAME environment variable\.

    password (optional, any, None)
      Provide a password for authenticating with the API\. Can also be specified via K8S\_AUTH\_PASSWORD environment variable\.

    client_cert (optional, any, None)
      Path to a certificate used to authenticate with the API\. Can also be specified via K8S\_AUTH\_CERT\_FILE environment variable\.

    client_key (optional, any, None)
      Path to a key file used to authenticate with the API\. Can also be specified via K8S\_AUTH\_KEY\_FILE environment variable\.

    ca_cert (optional, any, None)
      Path to a CA certificate used to authenticate with the API\. Can also be specified via K8S\_AUTH\_SSL\_CA\_CERT environment variable\.

    validate_certs (optional, bool, None)
      Whether or not to verify the API server\'s SSL certificates\. Can also be specified via K8S\_AUTH\_VERIFY\_SSL environment variable\.




## Examples

```yaml
    
    # File could be named inventory.yaml or inventory.yml

    # Authenticate with token, and return all pods and services for all namespaces
    plugin: krestomatio.k8s.inventory
    connection:
      host: https://192.168.64.4:8443
      api_key: xxxxxxxxxxxxxxxx
      validate_certs: false

    # Use a custom config file, and a specific context.
    plugin: krestomatio.k8s.inventory
    connection:
      kubeconfig: /path/to/config
      context: 'awx/192-168-64-4:8443/developer'

```


## Status


## Authors

- Job Cespedes \(\@jobcespedes\)
- Chris Houseknecht \<\@chouseknecht\>
- Fabian von Feilitzsch \<\@fabianvf\>
