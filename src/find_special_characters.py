# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This program searches for special characters in the Taxonomy.
"""


from oblib import taxonomy
import re

regex1 = re.compile('[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ]')
regex2 = re.compile('^[1234567890]')

tax = taxonomy.Taxonomy()

for type_ in tax.types.get_all_types():
    for e in tax.types.get_type_enum(type_):
        if regex1.search(e) != None or regex2.search(e) != None:
            print(type_, e)
