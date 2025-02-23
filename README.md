## Ansible / RHACS CVE playbooks

A collection of Ansible playbooks that can be used to automate CVE management with Red Hat Advanced Cluster Security for Kubernetes (RHACS).

- `defer-cve.yml`: Uses the RHACS RESTful API to defer / waiver a single CVE, and optionally specify the number of days it should be deferred for
- `mark-cve.yml`: Uses the RHACS RESTful API to mark a single CVE as a false positive
- `defer-multiple.yml`: Takes a list of CVEs and marks each as deferred. Also showcases using an ansible filter plugin to map CVEs to RHSAs using the Red Hat Security Data API.