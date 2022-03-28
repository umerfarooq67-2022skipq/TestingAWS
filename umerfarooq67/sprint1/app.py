#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sprint1.sprint1_stack import Sprint1Stack


app = cdk.App()

# Adding Tags.
cdk.Tags.of(app).add("Cohort","Orion")
cdk.Tags.of(app).add("Name","Umer Farooq 67")


Sprint1Stack(app, "UmerFarooq67Sprint1Stack",
    )

app.synth()
