from sot_ros_api import *

def start():
    push(taskTORSO)
    push(taskRW)
    push(taskRE)

def stop():
    pop(taskTORSO)
    pop(taskRW)
    pop(taskRE)

# Create the tasks and set up the gains
taskJL = createJointLimitsTask(gain = 100)
taskBASE = createEqualityTask('baseContact','base_joint',10)
taskRW = createEqualityTask('rightWrist', 'arm_right_7_joint',10)
taskLW = createEqualityTask('leftWrist', 'arm_left_7_joint',10)
taskRE = createEqualityTask('rightElbow', 'arm_right_4_joint',10)
taskLE = createEqualityTask('leftElbow', 'arm_left_4_joint',10)
taskTORSO = createEqualityTask('torso', 'torso_2_joint',10)

# Track the z axis orientation and the position
taskRW.feature.selec.value = '100111'
taskLW.feature.selec.value = '100111'

# Track only the position
taskRE.feature.selec.value = '000111'
taskLE.feature.selec.value = '000111'

# Track only the orientation
taskTORSO.feature.selec.value = '111000'

# In this way RW and LW tasks have the same priority (same for RE and LE)
taskRW.task.add(taskLW.feature.name)
taskRE.task.add(taskLE.feature.name)

# Push the joint limits and base constraints
push(taskJL)
solver.addContact(taskBASE)

# Take the poses from ros topics
createRosExport('matrixHomoStamped',taskRW.featureDes.position,'motion_adaption_sot/r_hand_goal_filt')
createRosExport('matrixHomoStamped',taskLW.featureDes.position,'motion_adaption_sot/l_hand_goal_filt')
createRosExport('matrixHomoStamped',taskRE.featureDes.position,'motion_adaption_sot/r_elbow_goal_filt')
createRosExport('matrixHomoStamped',taskLE.featureDes.position,'motion_adaption_sot/l_elbow_goal_filt')
createRosExport('matrixHomoStamped',taskTORSO.featureDes.position,'motion_adaption_sot/torso_goal_filt')
