import re

def isTimestamp(s):
  timestamp_regex = r'\d{1,2}:{1,2}'
  return re.match(timestamp_regex, s.strip()) != None

def addLeadingDigit(timestamps):
  """
  append leading 0 where digit is needed. Assumes structure.
  """
  timestamp_regex_digit_needed = r'\d{1}:{1,2}'
  return [f'0{t}' for t in timestamps if re.match(timestamp_regex_digit_needed, t.strip())]

with open('timestamps.txt') as f:
  lines = f.readlines()
  # assumes timestamp structure

with open('input.txt') as f:
  # setup
  lines = f.readlines()
  # extract timestamps
  timestamps = addLeadingDigit([l.strip() for l in lines if isTimestamp(l)])

  transcript_oneline = ' '.join([l.strip() for l in lines if not isTimestamp(l)])
  print(transcript_oneline)
