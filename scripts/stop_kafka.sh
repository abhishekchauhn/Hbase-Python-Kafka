#!/bin/bash
#
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

set -e

cd ${HBASE_PYTHON_KAFKA_HOME}

# start zookeeper
${KAFKA_HOME}/bin/zookeeper-server-stop.sh ${HBASE_PYTHON_KAFKA_HOME}/conf/zookeeper.properties > /dev/null 2>&1 &
sleep 3

# start kafka-server
${KAFKA_HOME}/bin/kafka-server-stop.sh ${HBASE_PYTHON_KAFKA_HOME}/conf/server.properties > /dev/null 2>&1 &
sleep 3
