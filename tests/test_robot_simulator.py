import unittest

from ventura_robo import RobotState, command_speed, emergency_stop, reset_emergency_stop, simulate_forward


class RobotSimulatorTests(unittest.TestCase):
    def test_speed_is_safety_clamped(self):
        state = command_speed(RobotState(), requested_speed=4.0, max_speed=1.25)
        self.assertEqual(state.speed, 1.25)
        moved = simulate_forward(state, 2.0)
        self.assertEqual(moved.x, 2.5)

    def test_emergency_stop_prevents_motion(self):
        state = command_speed(RobotState(), 0.8)
        stopped = emergency_stop(state)
        self.assertTrue(stopped.emergency_stopped)
        self.assertEqual(stopped.speed, 0.0)
        self.assertEqual(simulate_forward(stopped, 10).x, 0.0)
        self.assertEqual(command_speed(stopped, 0.5).speed, 0.0)

    def test_reset_requires_explicit_new_speed_command(self):
        state = reset_emergency_stop(emergency_stop(RobotState(speed=0.8)))
        self.assertFalse(state.emergency_stopped)
        self.assertEqual(state.speed, 0.0)

    def test_negative_simulation_time_is_rejected(self):
        with self.assertRaises(ValueError):
            simulate_forward(RobotState(), -1)


if __name__ == "__main__":
    unittest.main()
