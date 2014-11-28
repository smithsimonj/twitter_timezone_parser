__author__ = 'simonsmith'

import codecs
import re
import HTMLParser
import simplejson

column_headers = ['gmt_second_offset', 'place', 'timezone']

regex = re.compile('<option data-offset="(.*?)" value="(.*?)" >\((.*?)\) (.*?)</option>')
parser = HTMLParser.HTMLParser()

big_list = []

output_file = codecs.open('twitter_timezones.csv', 'w', encoding='utf8')
output_file_json = codecs.open('twitter_timezones.json', 'w', encoding='utf8')
output_file.write(','.join(column_headers)+'\n')

for line in codecs.open('twitter_timezones.xml', encoding='utf8'):
    bits = regex.search(line.strip()).groups()
    bits = [parser.unescape(bit) for bit in bits]
    output_file.write(','.join(bits[0:3])+'\n')

    big_list.append({})
    for i, header in enumerate(column_headers):
        big_list[-1][header] = bits[i]

output_file_json.write(simplejson.dumps(big_list, sort_keys=True, indent=4 * ' '))

output_file.close()
output_file_json.close()