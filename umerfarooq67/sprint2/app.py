#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sprint2.sprint2_stack import Sprint2Stack


app = cdk.App()

cdk.Tags.of(app).add("Cohort","Orion")
cdk.Tags.of(app).add("Name","Umer67")



Sprint2Stack(app, "UmerFarooq67Sprint2Stack")

app.synth()

