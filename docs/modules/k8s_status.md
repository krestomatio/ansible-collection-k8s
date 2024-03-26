# k8s_status
Update the status for a Kubernetes API resource

## Synopsis

Sets the status field on a Kubernetes API resource\. Only should be used if you are using Ansible to implement a controller for the resource being modified\.


## Requirements

The below requirements are needed on the host that executes this module.

- python \>\= 3\.7
- openshift \>\= 0\.8\.1


## Parameters

  status (optional, dict, None)
    An object containing key\: value pairs that will be set on the status object of the specified resource\.

    One of <em>status</em> or <em>conditions</em> is required\.

    If you use <em>conditions</em>\, you cannot include a conditions field beneath status\.

    If you add a conditions field under status\, it will not be validated like conditions specified through <em>conditions</em> are\.

  conditions (optional, list, None)
    A list of condition objects that will be set on the status\.conditions field of the specified resource\.

    Unless <em>replace</em> is <code>true</code> the specified conditions will be merged with the conditions already set on the status field of the specified resource\.

    Each element in the list will be validated according to the conventions specified in the \[Kubernetes API conventions document\]\(https\://github\.com/kubernetes/community/blob/master/contributors/devel/api\-conventions\.md\#spec\-and\-status\)\.

    One of <em>status</em> or <em>conditions</em> is required\.\'

    type (True, str, None)
      The type of the condition\. Used to identify it uniquely\.

    status (True, str, None)
      The status of the condition\.

    reason (optional, str, None)
      The reason this condition has a particular status\. A single\, CamelCase word\.

    message (optional, str, None)
      A human readable message explaining the status of this condition\.

    lastHeartbeatTime (optional, str, None)
      An RFC3339 formatted datetime string

    lastTransitionTime (optional, str, None)
      An RFC3339 formatted datetime string


  replace (optional, bool, False)
    If set to <code>True</code>\, the status will be set using \`PUT\` rather than \`PATCH\`\, replacing the full status object\.

  replace_lists (optional, bool, False)
    If set to <code>True</code>\, any lists except \`conditions\` will be fully replaced if mismatched\.



## Examples

```yaml
    
    - name: Set custom status fields on TestCR
      k8s_status:
        api_version: apps.example.com/v1alpha1
        kind: TestCR
        name: my-test
        namespace: testing
        status:
          hello: world
          custom: entries

    - name: Update the standard condition of an Ansible Operator
      k8s_status:
        api_version: apps.example.com/v1alpha1
        kind: TestCR
        name: my-test
        namespace: testing
        conditions:
          - type: Running
            status: "True"
            reason: MigrationStarted
            message: "Migration from v2 to v3 has begun"
            lastTransitionTime: "{{ lookup('pipe', 'date --rfc-3339 seconds') }}"

    - name: |
        Create custom conditions. WARNING: The default Ansible Operator status management
        will never overwrite custom conditions, so they will persist indefinitely. If you
        want the values to change or be removed, you will need to clean them up manually.
      k8s_status:
        api_version: apps.example.com/v1alpha1
        kind: TestCR
        name: my-test
        namespace: testing
        conditions:
          - type: Available
            status: "False"
            reason: PingFailed
            message: "The service did not respond to a ping"

```


## Return Values

  result (success, complex, )
    If a change was made\, will return the patched object\, otherwise returns the instance object\.

    api_version (success, str, )
      The versioned schema of this representation of an object\.

    kind (success, str, )
      Represents the REST resource this object represents\.

    metadata (success, dict, )
      Standard object metadata\. Includes name\, namespace\, annotations\, labels\, etc\.

    spec (success, dict, )
      Specific attributes of the object\. Will vary based on the <em>api\_version</em> and <em>kind</em>\.

    status (success, dict, )
      Current status details for the object\.




## Status

- This module is not guaranteed to have a backwards compatible interface. *[preview]*

- This module is maintained by community.

## Authors

- Fabian von Feilitzsch \(\@fabianvf\)
- Job Céspedes Ortiz \(\@jobcespedes\)
