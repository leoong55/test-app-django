#!/usr/bin/env python

import ci_lib

batches = [
    [
        'aws ecr-public get-login-password | docker login --username AWS --password-stdin public.ecr.aws',
        'docker pull %s' % (ci_lib.image_for_distro(ci_lib.DISTRO),),
    ],
    [
        'curl https://dw.github.io/mitogen/binaries/ubuntu-python-2.4.6.tar.bz2 | sudo tar -C / -jxv',
    ]
]

ci_lib.run_batches(batches)
