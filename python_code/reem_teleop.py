from sot_ros_api import *

taskRW = createEqualityTask('rightWrist', 'arm_right_tool_joint',1000)
taskLW = createEqualityTask('leftWrist', 'arm_left_tool_joint',1000)

taskRE = createEqualityTask('rightElbow', 'arm_right_4_joint',1000)
taskLE = createEqualityTask('leftElbow', 'arm_left_4_joint',1000)

taskTORSO = createEqualityTask('torso', 'torso_2_joint',1000)
taskBASE = createEqualityTask('baseContact','base_joint',1000)

taskRW.feature.selec.value = '000111'
taskLW.feature.selec.value = '000111'
taskRE.feature.selec.value = '000100'
taskLE.feature.selec.value = '000100'

taskRW.task.add(taskLW.feature.name)
taskRE.task.add(taskLE.feature.name)

taskJL = createJointLimitsTask(gain = 1)
plug(robot.device.dt,taskJL.dt)

push(taskJL)
solver.addContact(taskBASE)
solver.addContact(taskTORSO)

createRosExport('matrixHomoStamped',taskRW.featureDes.position,'motion_adaption_sot/r_hand_goal_filt')
createRosExport('matrixHomoStamped',taskLW.featureDes.position,'motion_adaption_sot/l_hand_goal_filt')

createRosExport('matrixHomoStamped',taskRE.featureDes.position,'motion_adaption_sot/r_elbow_goal_filt')
createRosExport('matrixHomoStamped',taskLE.featureDes.position,'motion_adaption_sot/l_elbow_goal_filt')

push(taskRW)
push(taskRE)
