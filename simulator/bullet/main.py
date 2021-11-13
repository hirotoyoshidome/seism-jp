import pybullet as p
import time
import pybullet_data


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

obUids = p.loadMJCF("mjcf/humanoid.xml")
humanoid = obUids[1]

gravId = p.addUserDebugParameter("gravity", -10, 10, -1)
jointIds = []
paramIds = []

# planeId = p.loadURDF("plane.urdf")

p.setPhysicsEngineParameter(numSolverIterations=10)
p.changeDynamics(humanoid, -1, linearDamping=0, angularDamping=0)

# humanoid param.
for j in range(p.getNumJoints(humanoid)):
    p.changeDynamics(humanoid, j, linearDamping=0, angularDamping=0)
    info = p.getJointInfo(humanoid, j)
    jointName = info[1]
    jointType = info[2]
    if jointType == p.JOINT_PRISMATIC or jointType == p.JOINT_REVOLUTE:
        jointIds.append(j)
        paramIds.append(p.addUserDebugParameter(jointName.decode("utf-8"), -4, 4, 0))

# simulator
p.setRealTimeSimulation(1)
while 1:
    p.setGravity(0, 0, p.readUserDebugParameter(gravId))
    for i in range(len(paramIds)):
        c = paramIds[i]
        targetPos = p.readUserDebugParameter(c)
        p.setJointMotorControl2(
            humanoid, jointIds[i], p.POSITION_CONTROL, targetPos, force=5 * 240.0
        )
    time.sleep(0.01)

# startPos = [0,0,1]
# startOrientation = p.getQuaternionFromEuler([0,0,0])
# boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)

# #set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
# for i in range (10000):
#     p.stepSimulation()
#     time.sleep(1./240.)
# cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
# print("cubePos : ",cubePos,cubeOrn)

p.disconnect()
