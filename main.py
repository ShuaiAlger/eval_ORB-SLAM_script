
import os



method_list = [   "Monocular",
                    "Monocular-Inertial",
                    "Stereo",
                    "Stereo-Inertial",
                    ]

program_list = [
    "mono_euroc",
    "mono_inertial_euroc",
    "stereo_euroc",
    "stereo_inertial_euroc",
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

data_seqs_list_v2 = [
    "MH01",
    "MH02",
    "MH03",
    "MH04",
    "MH05",

    "V101",
    "V102",
    "V103",

    "V201",
    "V202",
    "V203",
]

data_path_root = "/media/ssmem/datasetdisk2/Euroc/"



def mkdir_wcheck(_dir):
    if os.path.isdir(_dir):
        pass
    else:
        os.mkdir(_dir)



def run(method_id, seq_id):
    vocabulary_path = "./Vocabulary/ORBvoc.txt"
    dataset_name = "EuRoC"

    

    if method_id == 0:
        method_name = "Monocular"
        program_name = "mono_euroc"
    elif method_id == 1:
        method_name = "Monocular-Inertial"
        program_name = "mono_inertial_euroc"
    elif method_id == 2:
        method_name = "Stereo"
        program_name = "stereo_euroc"
    elif method_id == 3:
        method_name = "Stereo-Inertial"
        program_name = "stereo_inertial_euroc"



    seq_name = data_seqs_list[seq_id]
    seq_index = data_seqs_list.index(seq_name)
    simple_seq_name = data_seqs_list_v2[seq_index]



    data_path = "/media/ssmem/datasetdisk2/" + dataset_name + "/" + seq_name
    # data_path_root + "data_seqs"

    base_path = "./Examples"+"/" + method_name

    program_path = base_path + "/" + program_name
    config_path = base_path + "/" + dataset_name+".yaml"
    timestamp_path = base_path + "/" + dataset_name+"_TimeStamps" + "/" + simple_seq_name+".txt"

    command = program_path+" "+vocabulary_path+" "+config_path+" "+data_path+" "+timestamp_path

    print("COMMAND:\n", command)
    os.system(command)


    filename1 = "CameraTrajectory.txt"
    filename2 = "KeyFrameTrajectory.txt"

    save_root_dir = "results"


    mkdir_wcheck(save_root_dir)
    mkdir_wcheck(save_root_dir+"/"+dataset_name)
    mkdir_wcheck(save_root_dir+"/"+dataset_name+"/"+seq_name)

    save_dir = save_root_dir+"/"+dataset_name+"/"+seq_name+"/"+method_name
    mkdir_wcheck(save_dir)

    
    os.system("mv"+" "+filename1+" "+save_dir+"/")
    os.system("mv"+" "+filename2+" "+save_dir+"/")




def eval(method_id, seq_id):
    dataset_name = "EuRoC"

    

    if method_id == 0:
        method_name = "Monocular"
        program_name = "mono_euroc"
    elif method_id == 1:
        method_name = "Monocular-Inertial"
        program_name = "mono_inertial_euroc"
    elif method_id == 2:
        method_name = "Stereo"
        program_name = "stereo_euroc"
    elif method_id == 3:
        method_name = "Stereo-Inertial"
        program_name = "stereo_inertial_euroc"


    seq_name = seq_name = data_seqs_list[seq_id]
    seq_index = data_seqs_list.index(seq_name)
    simple_seq_name = data_seqs_list_v2[seq_index]

    filename1 = "CameraTrajectory.txt"
    filename2 = "KeyFrameTrajectory.txt"

    save_root_dir = "results"
    save_dir = save_root_dir+"/"+dataset_name+"/"+seq_name+"/"+method_name

    program_path = "python ./evaluation/evaluate_ate_scale.py"

    gt_file = "./evaluation/Ground_truth/EuRoC_left_cam/" + simple_seq_name + "_GT.txt"

    result_file = save_dir + "/" + "CameraTrajectory.txt"

    command = program_path+" "+gt_file+" "+result_file

    # print("COMMAND:\n", command)

    print("EVAL --->  " + method_name)
    os.system(command)






if __name__ == '__main__':

    for i in range(len(data_seqs_list)):
        for m in range(len(method_list)):
            run(m, i)

    for i in range(len(data_seqs_list)):
        for m in range(len(method_list)):
            eval(m, i)


