# This is a good idea for your indexer, especially if you are running Windows. 
# You will need to put this file in local/limits.conf
# This also fixes bug SPL-107253 (invalid vector<T> subscript) in Splunk 6.3.0
[lookup]
max_memtable_bytes = 100000000
