#!/bin/bash
MOUNT=$1
#
# Copyright (c) 2017 LabKey Corporation. All rights reserved. No portion of this work may be reproduced in
# any form or by any electronic or mechanical means without written permission from LabKey Corporation.
#

pushd $MOUNT/.rstudio

find . -name session-persistent-state -type f -exec  sed -i 's/abend="1"/abend="0"/' {} +

popd
