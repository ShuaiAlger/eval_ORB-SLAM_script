
import os

vocabulary_path = "./Vocabulary/ORBvoc.txt"


program_path = "./Examples/Monocular-Inertial/mono_inertial_euroc"
config_path = "./Examples/Monocular-Inertial/EuRoC.yaml"

data_path = "/media/ssmem/datasetdisk2/Euroc/MH_03_medium"
# data_path_root + "data_seqs"

timestamp_path = "./Examples/Monocular-Inertial/EuRoC_TimeStamps/MH03.txt"
# "./Examples/" + "pipeline" + "EuRoC_TimeStamps" + data_seqs + ".txt"

command = program_path+" "+vocabulary_path+" "+config_path+" "+data_path+" "+timestamp_path

print("COMMAND:\n", command)

os.system(command)

pipeline_list = [   "Monocular",
                    "Monocular-Inertial",
                    "Stereo",
                    "Stereo-Inertial",
                    ]

config_list = [
    "./Examples/Monocular/EuRoC.yaml",
    "./Examples/Monocular-Inertial/EuRoC.yaml",
    "./Examples/Stereo/EuRoC.yaml",
    "./Examples/Stereo-Inertial/EuRoC.yaml",
]

program_list = [
    "./Examples/Monocular/mono_euroc",
    "./Examples/Monocular-Inertial/mono_inertial_euroc",
    "./Examples/Stereo/stereo_euroc",
    "./Examples/Stereo-Inertial/stereo_inertial_euroc",
]

data_seqs_list = [
    "MH_01_easy",
    "MH_02_easy",
    "MH_03_medium",
    "MH_04_difficult",
    "MH_05_difficult",

    "V1_01_easy",
    "V1_02_medium",
    "V1_03_difficult",

    "V2_01_easy",
    "V2_02_medium",
    "V2_03_difficult",
]

data_path_root = "/media/ssmem/datasetdisk2/Euroc/"











