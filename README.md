# An Empirical Study of DLL Injection Bugs in the Firefox Ecosystem

### Research questions
- RQ1: What is the characteristics of the bugs caused by DLL injections?
- RQ2: Which factors triggered the DLL injection bugs?
- RQ3: Whatwouldbethepotentialsolutionstoreducesuch DLL injection bugs?

### Data explanation
- **print_bugzilla_query.py**: Script to query DLL injection related bugs from July 2015 to August 2017.
- **get_bug_data.py**: Script to calculate metrics.
- **manual_classification.csv**: Raw results from the above query and manual classification on the bugs.
- **bug_type.csv**: Manual classification on the types of the bugs.
- **bug_reproducibility.csv**: Manual classification on the reproducibility of the bugs.
- **machine_extracted_metrics.csv**: Metrics that were automatically extracted from bug reports.
