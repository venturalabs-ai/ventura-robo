from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RobotState:
    x: float = 0.0
    y: float = 0.0
    heading_deg: float = 0.0
    speed: float = 0.0
    emergency_stopped: bool = False


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def command_speed(state: RobotState, requested_speed: float, max_speed: float = 1.0) -> RobotState:
    if max_speed <= 0:
        raise ValueError("max_speed must be positive")
    if state.emergency_stopped:
        return RobotState(state.x, state.y, state.heading_deg, 0.0, True)
    speed = clamp(requested_speed, -max_speed, max_speed)
    return RobotState(state.x, state.y, state.heading_deg, speed, False)


def emergency_stop(state: RobotState) -> RobotState:
    return RobotState(state.x, state.y, state.heading_deg, 0.0, True)


def reset_emergency_stop(state: RobotState) -> RobotState:
    return RobotState(state.x, state.y, state.heading_deg, 0.0, False)


def simulate_forward(state: RobotState, seconds: float) -> RobotState:
    """Simulator-first 1D movement along x; deterministic safety baseline, not hardware control."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    if state.emergency_stopped:
        return RobotState(state.x, state.y, state.heading_deg, 0.0, True)
    return RobotState(
        x=state.x + state.speed * seconds,
        y=state.y,
        heading_deg=state.heading_deg,
        speed=state.speed,
        emergency_stopped=False,
    )
