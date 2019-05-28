# Author: Abhishek Chauhan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# write a test table to HBase for Kafka Producer
import happybase

def main():
    # get a connection
    conn = happybase.Connection(host='localhost', port=9090)

    # create and populate 'books' table if it does not
    # already exists
    # get list of tables
    tables_list = conn.tables()

    if b'books' not in tables_list:
        # create 'books' table
        conn.create_table(
            'books',
            {'Author': dict(max_versions=2),
            'Info':dict(),
            }
        )

        # get instance of 'books' table
        table = conn.table('books')

        # populate the table with some records
        table.put(b'101', {b'Author:FirstName' : b'George',
                           b'Author:LastName'  : b'Orwell'})
        table.put(b'101', {b'Info:Title' : b'Animal Farm',
                           b'Info:Price' : b'100'})
        table.put(b'102', {b'Author:FirstName' : b'George',
                           b'Author:LastName'  : b'Orwell'})
        table.put(b'102', {b'Info:Title' : b'1984',
                           b'Info:Price' : b'150'})
        table.put(b'103', {b'Author:FirstName' : b'Albert',
                           b'Author:LastName'  : b'Camus'})
        table.put(b'103', {b'Info:Title' : b'The Fall',
                           b'Info:Price' : b'200'})
        table.put(b'104', {b'Author:FirstName' : b'Franz',
                           b'Author:LastName'  : b'Kafka'})
        table.put(b'104', {b'Info:Title' : b'The Trial',
                           b'Info:Price' : b'250'})

if __name__== "__main__":
    main()
