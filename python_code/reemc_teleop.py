from sot_ros_api import *

taskRW = createEqualityTask('rightWrist', 'arm_right_tool_joint',gain = 10)
taskLW = createEqualityTask('leftWrist', 'arm_left_tool_joint',gain = 10)

taskRE = createEqualityTask('rightElbow', 'arm_right_4_joint',gain = 10)
taskLE = createEqualityTask('leftElbow', 'arm_left_4_joint',gain = 10)

taskRS = createEqualityTask('rightSole', 'right_sole_joint',1)
taskLS = createEqualityTask('leftSole','left_sole_joint',1)
taskTORSO = createEqualityTask('torso', 'base_joint',1)

taskRW.feature.selec.value = '000111'
taskLW.feature.selec.value = '000111'
taskRE.feature.selec.value = '000100'
taskLE.feature.selec.value = '000100'

taskRW.task.add(taskLW.feature.name)
taskRE.task.add(taskLE.feature.name)

taskJL = createJointLimitsTask(gain = 200)
plug(robot.device.dt,taskJL.dt)

push(taskJL)
solver.addContact(taskRS)
solver.addContact(taskLS)
solver.addContact(taskTORSO)

createRosExport('matrixHomoStamped',taskRW.featureDes.position,'r_hand_goal_filt')
createRosExport('matrixHomoStamped',taskLW.featureDes.position,'l_hand_goal_filt')

createRosExport('matrixHomoStamped',taskRE.featureDes.position,'r_elbow_goal_filt')
createRosExport('matrixHomoStamped',taskLE.featureDes.position,'l_elbow_goal_filt')

push(taskRW)
push(taskRE)
