import wpilib
from xbox import XboxController


class Robot(wpilib.IterativeRobot):
    def robotInit(self):
        self.joystick1 = wpilib.Joystick(0)
        self.xbox = XboxController(self.joystick1)
        self.motor0 = wpilib.Jaguar(0)
        self.motor1 = wpilib.Jaguar(1)
        self.robotdrive = wpilib.RobotDrive(self.motor0, self.motor1)
        self.robotdrive.setInvertedMotor(
            wpilib.RobotDrive.MotorType.kRearLeft, True)
        self.robotdrive.setInvertedMotor(
            wpilib.RobotDrive.MotorType.kRearRight, True)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.robotdrive.drive(
            self.xbox.left_joystick_axis_v(),
            self.xbox.left_joystick_axis_h(),
        )

    def testPeriodic(self):
        pass



if __name__ == "__main__":
    wpilib.run(Robot)
