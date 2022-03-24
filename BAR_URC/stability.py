from weis.aeroelasticse.runFAST_pywrapper import runFAST_pywrapper_batch
from weis.aeroelasticse.CaseGen_General import CaseGen_General
import numpy as np
import os
import sys

if __name__ == '__main__':


    if int(sys.argv[1]) == 0:
        aero_flag = False
    else:
        aero_flag = True
    if int(sys.argv[2]) == 0:
        tower_dt_dof = False
    else:
        tower_dt_dof = True
    if int(sys.argv[3]) == 0:
        controller = False
    else:
        controller = True


    fastBatch = runFAST_pywrapper_batch()

    use_cores = 36

    run_dir = os.path.dirname( os.path.realpath(__file__))
    fastBatch.FAST_InputFile = 'BAR_URC.fst'
    fastBatch.FAST_directory = '/home/pbortolo/BAR_Designs/BAR_URC/OpenFAST'

    folder_name = 'stability_bar_urc'
    if aero_flag:
        folder_name += 'a_'
    else:
        folder_name += 's_'

    if tower_dt_dof:
        folder_name += 'towdt_'
    else:
        folder_name += 'rotor_'
    if controller:
        folder_name += 'ctrl'
    else:
        folder_name += 'fixrpm'

    fastBatch.FAST_runDirectory = os.path.join(run_dir, '..', '..', 'outputs',folder_name)
    
    if aero_flag:
        traj = np.loadtxt(os.path.join(run_dir, 'trajectory.dat'))

        hws = traj[:,0]
        rot_speeds = traj[:,1]
        pitch = traj[:,2]
        TTDspFA = np.zeros_like(hws)
        TTDspSS = np.zeros_like(hws)
        hws_interp = np.arange(0., 28., 2.)
        rot_speeds_interp = np.interp(hws_interp, hws, rot_speeds)
        pitch_interp = np.interp(hws_interp, hws, pitch)
        TTDspFA_interp = np.interp(hws_interp, hws, TTDspFA)
        TTDspSS_interp = np.interp(hws_interp, hws, TTDspSS)
    else:
        rot_speeds_interp = np.arange(0., 9., 1.)
        pitch_interp = np.zeros_like(rot_speeds_interp)
        TTDspFA_interp = np.zeros_like(rot_speeds_interp)
        TTDspSS_interp = np.zeros_like(rot_speeds_interp)
    
    n_cores = np.min([use_cores, len(rot_speeds_interp)])

    trim_case = np.zeros(len(rot_speeds_interp), dtype=int)
    trim_gain = np.zeros(len(rot_speeds_interp))
    trim_tol = np.zeros(len(rot_speeds_interp))
    VS_SlPc = np.zeros(len(rot_speeds_interp))
    for i in range(len(rot_speeds_interp)):
        trim_tol[i] = 0.0001
        VS_SlPc[i] = 2.
        if rot_speeds_interp[i] < max(rot_speeds_interp):
            trim_case[i] = 2
            trim_gain[i] = 100
        else:
            trim_case[i] = 3
            trim_gain[i] = 0.00001

    VS_SlPc[2] = 20.
    
    if aero_flag:
        CompAero = np.ones_like(rot_speeds_interp, dtype=int) * 2
        CompInflow = np.ones_like(rot_speeds_interp, dtype=int)
        if hws_interp[0] == 0.:
            CompAero[0] = 0
            CompInflow[0] = 0
    else:
        CompAero = np.zeros_like(rot_speeds_interp, dtype=int)
        CompInflow = np.zeros_like(rot_speeds_interp, dtype=int)

    case_inputs = {}
    case_inputs[("ElastoDyn","FlapDOF1")] = {'vals':["True"], 'group':0}
    case_inputs[("ElastoDyn","FlapDOF2")] = {'vals':["True"], 'group':0}
    case_inputs[("ElastoDyn","EdgeDOF")] = {'vals':["True"], 'group':0}
    if controller:
        case_inputs[("ElastoDyn","GenDOF")] = {'vals':["True"], 'group':0}
    else:
        case_inputs[("ElastoDyn","GenDOF")] = {'vals':["False"], 'group':0}

    if tower_dt_dof:
        case_inputs[("ElastoDyn","DrTrDOF")] = {'vals':["True"], 'group':0}
        case_inputs[("ElastoDyn","TwFADOF1")] = {'vals':["True"], 'group':0}
        case_inputs[("ElastoDyn","TwFADOF2")] = {'vals':["True"], 'group':0}
        case_inputs[("ElastoDyn","TwSSDOF1")] = {'vals':["True"], 'group':0}
        case_inputs[("ElastoDyn","TwSSDOF2")] = {'vals':["True"], 'group':0}
    else:
        case_inputs[("ElastoDyn","TwFADOF1")] = {'vals':["False"], 'group':0}
        case_inputs[("ElastoDyn","TwFADOF2")] = {'vals':["False"], 'group':0}
        case_inputs[("ElastoDyn","TwSSDOF1")] = {'vals':["False"], 'group':0}
        case_inputs[("ElastoDyn","TwSSDOF2")] = {'vals':["False"], 'group':0}
        case_inputs[("ElastoDyn","DrTrDOF")] = {'vals':["False"], 'group':0}
    case_inputs[("ElastoDyn","TeetDOF")] = {'vals':["False"], 'group':0}
    case_inputs[("ElastoDyn","YawDOF")] = {'vals':["False"], 'group':0}
    case_inputs[("ElastoDyn","ShftTilt")] = {'vals':[0.], 'group':0}

    case_inputs[("Fst","Gravity")] = {'vals':[0.], 'group':0}
    case_inputs[("Fst","Echo")] = {'vals':["False"], 'group':0}
    case_inputs[("Fst","TMax")] = {'vals':[1000.], 'group':0}
    case_inputs[("Fst","DT")] = {'vals':[0.0002], 'group':0}
    case_inputs[("Fst","InterpOrder")] = {'vals':[1], 'group':0}
    case_inputs[("Fst","CompAero")] = {'vals':CompAero, 'group':1}
    case_inputs[("Fst","CompElast")] = {'vals':[2], 'group':0}
    case_inputs[("Fst","CompInflow")] = {'vals':CompInflow, 'group':1}
    if controller:
        case_inputs[("Fst","CompServo")] = {'vals':[1], 'group':0}
    else:
        case_inputs[("Fst","CompServo")] = {'vals':[0], 'group':0}
    case_inputs[("Fst","SumPrint")] = {'vals':["False"], 'group':0}
    case_inputs[("Fst","DT_Out")] = {'vals':[0.02], 'group':0}
    case_inputs[("Fst","OutFmt")] = {'vals':["ES16.9E2"], 'group':0}
    case_inputs[("Fst","OutFileFmt")] = {'vals':[2], 'group':0}
    case_inputs[("Fst","Linearize")] = {'vals':["True"], 'group':0}
    case_inputs[("Fst","CalcSteady")] = {'vals':["True"], 'group':0}
    case_inputs[("Fst","TrimCase")] = {'vals':trim_case, 'group':1}
    case_inputs[("Fst","TrimTol")] = {'vals':trim_tol, 'group':1}
    case_inputs[("Fst","TrimGain")] = {'vals':trim_gain, 'group':1}
    case_inputs[("Fst","Twr_Kdmp")] = {'vals':[1.e+2], 'group':0}
    case_inputs[("Fst","Bld_Kdmp")] = {'vals':[1.e+2], 'group':0}
    case_inputs[("Fst","NLinTimes")] = {'vals':[36], 'group':0}
    case_inputs[("Fst","LinInputs")] = {'vals':[0], 'group':0}
    case_inputs[("Fst","LinOutputs")] = {'vals':[0], 'group':0}
    case_inputs[("Fst","LinOutJac")] = {'vals':["False"], 'group':0}
    case_inputs[("Fst","LinOutMod")] = {'vals':["False"], 'group':0}
    case_inputs[("Fst","WrVTK")] = {'vals':[0], 'group':0}
    if aero_flag:
        case_inputs[("AeroDyn15","AFAeroMod")] = {'vals':[1], 'group':0}
        case_inputs[("AeroDyn15","TwrPotent")] = {'vals':[0], 'group':0}
        case_inputs[("AeroDyn15","TwrShadow")] = {'vals':[0], 'group':0}
        case_inputs[("AeroDyn15","FrozenWake")] = {'vals':["True"], 'group':0}
        case_inputs[("InflowWind","WindType")] = {'vals':[1], 'group':0}
        case_inputs[("InflowWind","HWindSpeed")]= {'vals': hws_interp, 'group': 1}
        case_inputs[("InflowWind","PLexp")] = {'vals':[0.], 'group':0}
    case_inputs[("ElastoDyn","RotSpeed")] = {'vals': rot_speeds_interp, 'group': 1}
    case_inputs[("ElastoDyn","BlPitch1")] = {'vals': pitch_interp, 'group': 1}
    case_inputs[("ElastoDyn","BlPitch2")] = case_inputs[("ElastoDyn","BlPitch1")]
    case_inputs[("ElastoDyn","BlPitch3")] = case_inputs[("ElastoDyn","BlPitch1")]
    case_inputs[("ElastoDyn","TTDspFA")] = {'vals': TTDspFA_interp, 'group': 1}
    case_inputs[("ElastoDyn","TTDspSS")] = {'vals': TTDspSS_interp, 'group': 1}
    if controller:
        case_inputs[("ServoDyn","PCMode")] = {'vals': [0], 'group': 0}
        case_inputs[("ServoDyn","VSContrl")] = {'vals': [1], 'group': 0}
        case_inputs[("ServoDyn","VS_SlPc")] = {'vals': VS_SlPc, 'group': 1}

    namebase='bar_urc_stab'

    case_list, case_name_list = CaseGen_General(case_inputs, dir_matrix=fastBatch.FAST_runDirectory, namebase=namebase)

    fastBatch.case_list = case_list
    fastBatch.case_name_list = case_name_list
    fastBatch.use_exe = True

    if n_cores > 1:
        fastBatch.run_multi(n_cores)
    else:
        fastBatch.run_serial()
