import os
import sys
sys.path.append("../../../../monk_v1/");
sys.path.append("../../../monk/");
import psutil

from pytorch_prototype import prototype
from compare_prototype import compare
from common import print_start
from common import print_status

import torch
import numpy as np
from pytorch.losses.return_loss import load_loss


def test_block_resnet_v1(system_dict):
    forward = True;

    test = "test_block_resnet_v1";
    system_dict["total_tests"] += 1;
    print_start(test, system_dict["total_tests"])
    if(forward):
        try:
            gtf = prototype(verbose=0);
            gtf.Prototype("sample-project-1", "sample-experiment-1");


            network = [];
            network.append(gtf.resnet_v1_block(output_channels=32, stride=1, downsample=True));
            network.append(gtf.resnet_v1_block(output_channels=32, stride=1, downsample=False));
            gtf.Compile_Network(network, data_shape=(1, 64, 64), use_gpu=False);

            x = torch.randn(1, 1, 64, 64);
            y = gtf.system_dict["local"]["model"](x);         

            system_dict["successful_tests"] += 1;
            print_status("Pass");

        except Exception as e:
            system_dict["failed_tests_exceptions"].append(e);
            system_dict["failed_tests_lists"].append(test);
            forward = False;
            print_status("Fail");
    else:
        system_dict["skipped_tests_lists"].append(test);
        print_status("Skipped");

    return system_dict
