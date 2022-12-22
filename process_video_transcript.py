import re

DISALLOWED_CHARACTERS = set(['-', '*', ''])
DISABLE_TIMESTAMP_SECTIONS = False

def isTimestamp(s):
  timestamp_regex = r'\d{1,2}:{1,2}'
  return re.match(timestamp_regex, s.strip()) != None


def timestampNeedsLeadingDigit(t):
  timestamp_regex_digit_needed = r'\d{1}:{1,2}'
  return re.match(timestamp_regex_digit_needed, t.strip()) != None

def addLeadingDigit(timestamps):
  """
  append leading 0 where digit is needed. Assumes structure.
  """
  return [f'0{t}' if timestampNeedsLeadingDigit(t) else t for t in timestamps]


# timestamp, title
timestamped_titles = []
with open('timestamps.txt') as f:
  lines = f.readlines()
  # assumes timestamp structure
  for line in lines:
    timestamp, title = line.split(' ')[0], ' '.join(list(filter(lambda x: x.strip() not in DISALLOWED_CHARACTERS, line.split(' ')[1:]))).strip()
    timestamped_titles.append((timestamp, title))
if DISABLE_TIMESTAMP_SECTIONS:
  timestamped_titles = [('00:00', 'Default Title')]

timestamped_titles.sort(key=lambda x: x[0], reverse=True)

# title, content
sections = {title: '' for timestamp, title in timestamped_titles}
with open('input.txt') as f:
  # setup
  lines = f.readlines()
  # extract timestamps
  timestamps = addLeadingDigit([l.strip() for l in lines if isTimestamp(l)])
  timestamp_lines = [l.strip() for l in lines if not isTimestamp(l)]

  # print(f"{len(timestamps)=} {len(timestamp_lines)=}")

  for timestamp, line in zip(timestamps, timestamp_lines):
    for btimestamp, btitle in timestamped_titles:
      if timestamp >= btimestamp:
        # print(f"{timestamp} >= {btimestamp} {timestamp >= btimestamp} added to {btitle}")
        sections[btitle] += line
        break

  for section_title, content in reversed(sections.items()):
    print(f"# {section_title}\n{content}\n")
    pass

  # transcript_oneline = ' '.join([l.strip() for l in lines if not isTimestamp(l)])
  # print(transcript_oneline)
