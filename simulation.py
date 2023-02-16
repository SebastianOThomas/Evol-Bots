class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        # physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # add gravity
        p.setGravity(0,0,-9.8)
        # additional pyrosim setu
        pyrosim.Prepare_To_Simulate(robotId)

