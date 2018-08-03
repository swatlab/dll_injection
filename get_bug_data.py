import csv
from libmozdata import bugzilla
from libmozdata import utils

bug_ids = []
with open('manual_classification/manual_classification.csv') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        if row[1] != 'no':
            bug_ids.append(row[0])

bugs = {}

def bughandler(bug):
    bug_id = str(bug['id'])

    if bug_id not in bugs:
        bugs[bug_id] = dict()

    for k, v in bug.items():
        bugs[bug_id][k] = v

def historyhandler(bug):
    bugid = str(bug['id'])

    if bugid not in bugs:
        bugs[bugid] = dict()

    bugs[bugid]['history'] = bug['history']

bugzilla.Bugzilla(bug_ids, bughandler=bughandler, historyhandler=historyhandler, include_fields=['id', 'creation_time', 'cf_last_resolved']).get_data().wait()

with open('bug_data.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['bug_id', 'fixing_time', 'fixing_time_since_blocking', 'fixing_time_since_tracked', 'tracked_or_blocking', 'which_blocking'])
    for bug_id, bug_data in bugs.items():
        tracked = False
        blocking = False
        which_blocking = []
        when_blocking = None
        when_tracked = None
        for entry in bug_data['history']:
            for change in entry['changes']:
                if change['field_name'].startswith('cf_tracking_firefox'):
                    if change['added'] == 'blocking':
                        blocking = True
                        which_blocking.append(change['field_name'][len('cf_tracking_firefox'):])
                        if when_blocking is None:
                            when_blocking = entry['when']
                    elif change['added'] == '+':
                        tracked = True
                        if when_tracked is None:
                            when_tracked = entry['when']

        tracking_value = 'blocking' if blocking else 'tracked' if tracked else 'never'

        if bug_data['cf_last_resolved'] is None:
            fixing_time = -1
            fixing_time_since_blocking = -1
            fixing_time_since_tracked = -1
        else:
            fixing_time = int((utils.get_date_ymd(bug_data['cf_last_resolved']) - utils.get_date_ymd(bug_data['creation_time'])).total_seconds())
            if blocking:
                fixing_time_since_blocking = int((utils.get_date_ymd(bug_data['cf_last_resolved']) - utils.get_date_ymd(when_blocking)).total_seconds())
            else:
                fixing_time_since_blocking = -1
            if tracked:
                fixing_time_since_tracked = int((utils.get_date_ymd(bug_data['cf_last_resolved']) - utils.get_date_ymd(when_tracked)).total_seconds())
            else:
                fixing_time_since_tracked = -1

        csv_writer.writerow([bug_id, fixing_time, fixing_time_since_blocking, fixing_time_since_tracked, tracking_value, '^'.join(which_blocking)])
