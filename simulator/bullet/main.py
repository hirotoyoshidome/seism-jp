import pybullet as p
import time
import pybullet_data

# init
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

gravId = p.addUserDebugParameter("gravity", -10, 10, -10)
p.setPhysicsEngineParameter(numSolverIterations=10)

# humanoid
obUids = p.loadMJCF("mjcf/humanoid.xml")
humanoid = obUids[1]
p.changeDynamics(humanoid, -1, linearDamping=0, angularDamping=0)

# humanoid param.
jointIds = []
paramIds = []
for j in range(p.getNumJoints(humanoid)):
    p.changeDynamics(humanoid, j, linearDamping=0, angularDamping=0)
    info = p.getJointInfo(humanoid, j)
    jointName = info[1]
    jointType = info[2]
    if jointType == p.JOINT_PRISMATIC or jointType == p.JOINT_REVOLUTE:
        jointIds.append(j)
        paramIds.append(p.addUserDebugParameter(jointName.decode("utf-8"), -4, 4, 0))

# cube
x = 4
y = 4
z = 4
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
for i in range(x):
    for j in range(y):
        for k in range(z):
            pos = [i + 1, j + 1, k + 1]
            p.loadURDF("cube.urdf", pos, startOrientation)

# R2D2 from star wars.
p.loadURDF("r2d2.urdf", [-1, -1, 1], startOrientation)

# simulator
p.setRealTimeSimulation(1)
while 1:
    p.setGravity(0, 0, -10)
    for i in range(len(paramIds)):
        c = paramIds[i]
        targetPos = p.readUserDebugParameter(c)
        p.setJointMotorControl2(
            humanoid, jointIds[i], p.POSITION_CONTROL, targetPos, force=5 * 240.0
        )
    time.sleep(0.01)

p.disconnect()
