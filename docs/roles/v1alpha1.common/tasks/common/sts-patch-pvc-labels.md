



# sts-patch-pvc-labels.yml


* save (nfs) ganesha server statefulset pvc current and new labels

* Block: patch sts to allow statefulset update labels and annotations

    * delete statefulset without removing pods and data

    * patch statefulset pvc(s)