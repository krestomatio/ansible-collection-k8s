



# sts-patch-pvc-size.yml


* save (nfs) ganesha server statefulset pvc current and new size

* Block: patch sts to allow statefulset pvc expansion

    * delete statefulset without removing pods and data

    * patch statefulset pvc(s)